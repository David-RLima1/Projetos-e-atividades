import sqlite3
from flask import Flask, request, jsonify, g

# --- Configuração ---
app = Flask(__name__)
DATABASE = 'escola_v2 (1).db' # O nome do seu arquivo de banco de dados

# --- Funções de Ajuda para o Banco de Dados ---

def get_db():
    """
    Cria uma conexão com o banco de dados para a requisição atual.
    Usamos 'g', que é um objeto especial do Flask para armazenar
    dados durante *uma* requisição. Isso evita reabrir a conexão
    várias vezes se precisarmos dela em vários lugares.
    """
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect(DATABASE)
        # Isso faz com que o banco de dados retorne os dados como dicionários
        # (ex: {'id': 1, 'nome': 'Medicina'}) em vez de tuplas. Facilita muito!
        db.row_factory = sqlite3.Row
    return db

@app.teardown_appcontext
def close_connection(exception):
    """
    Fecha a conexão com o banco de dados automaticamente
    quando a requisição termina (seja com sucesso ou erro).
    """
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()

# --- Rotas da API (Nosso CRUD) para Cursos ---

# [CREATE] - Criar um novo curso
@app.route('/cursos', methods=['POST'])
def create_curso():
    # Pega os dados JSON enviados na requisição (ex: {"nome": "Novo Curso", ...})
    data = request.get_json()
    
    # Validação simples
    if not data or 'nome' not in data or 'mensalidade' not in data or 'duracao' not in data:
        return jsonify({'error': 'Dados incompletos'}), 400

    try:
        nome = data['nome']
        mensalidade = data['mensalidade']
        duracao = data['duracao']
        
        db = get_db()
        cursor = db.cursor()
        
        # O SQL é baseado na estrutura da tabela Curso 
        cursor.execute(
            "INSERT INTO Curso (nome, mensalidade, duracao) VALUES (?, ?, ?)",
            (nome, mensalidade, duracao)
        )
        db.commit() # Importante: .commit() salva as mudanças
        
        # Retorna uma resposta de sucesso com o ID do novo curso
        return jsonify({'message': 'Curso criado com sucesso!', 'id': cursor.lastrowid}), 201
        
    except sqlite3.Error as e:
        # Se algo der errado no banco (ex: tipo de dado errado)
        return jsonify({'error': str(e)}), 500

# [READ] - Ler todos os cursos
@app.route('/cursos', methods=['GET'])
def get_all_cursos():
    db = get_db()
    cursor = db.execute("SELECT * FROM Curso")
    cursos = cursor.fetchall()
    
    # Converte a lista de 'sqlite3.Row' para uma lista de dicionários Python
    # que pode ser convertida para JSON.
    return jsonify([dict(curso) for curso in cursos])

# [READ] - Ler um curso específico pelo ID
@app.route('/cursos/<int:curso_id>', methods=['GET'])
def get_curso(curso_id):
    db = get_db()
    cursor = db.execute("SELECT * FROM Curso WHERE id = ?", (curso_id,))
    curso = cursor.fetchone() # Pega apenas o primeiro (e único) resultado
    
    if curso is None:
        return jsonify({'error': 'Curso não encontrado'}), 404
    
    return jsonify(dict(curso))

# [UPDATE] - Atualizar um curso existente
@app.route('/cursos/<int:curso_id>', methods=['PUT'])
def update_curso(curso_id):
    data = request.get_json()

    if not data or 'nome' not in data or 'mensalidade' not in data or 'duracao' not in data:
        return jsonify({'error': 'Dados incompletos'}), 400
    
    try:
        nome = data['nome']
        mensalidade = data['mensalidade']
        duracao = data['duracao']

        db = get_db()
        cursor = db.cursor()
        
        cursor.execute(
            "UPDATE Curso SET nome = ?, mensalidade = ?, duracao = ? WHERE id = ?",
            (nome, mensalidade, duracao, curso_id)
        )
        db.commit()
        
        # cursor.rowcount diz quantas linhas foram afetadas.
        # Se for 0, é porque não encontrou o ID.
        if cursor.rowcount == 0:
            return jsonify({'error': 'Curso não encontrado'}), 404
            
        return jsonify({'message': 'Curso atualizado com sucesso!'})

    except sqlite3.Error as e:
        return jsonify({'error': str(e)}), 500

# [DELETE] - Deletar um curso
@app.route('/cursos/<int:curso_id>', methods=['DELETE'])
def delete_curso(curso_id):
    try:
        db = get_db()
        cursor = db.cursor()
        cursor.execute("DELETE FROM Curso WHERE id = ?", (curso_id,))
        db.commit()
        
        if cursor.rowcount == 0:
            return jsonify({'error': 'Curso não encontrado'}), 404
            
        return jsonify({'message': 'Curso deletado com sucesso!'})
        
    except sqlite3.Error as e:
        # Isso vai dar erro se você tentar deletar um Curso que
        # já tem Turmas associadas (por causa da FOREIGN KEY )
        return jsonify({'error': f'Erro no banco de dados: {e}'}), 500

# --- Rodar a Aplicação ---
if __name__ == '__main__':
    # debug=True faz o servidor reiniciar automaticamente quando
    # você salvar o arquivo. Ótimo para desenvolver!
    app.run(debug=True)