import sqlite3

conexao = sqlite3.connect("/workspaces/Projetos-e-atividades/Banco de dados/banco_dados.db")
cursor = conexao.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS aluno (
        id INTEGER PRIMARY KEY,
        nome TEXT NOT NULL,
        idade INTEGER
    )

''')

cursor.execute('''
INSERT INTO aluno (nome, idade) VALUES 
               ('Alice Silva', 22),
               ('Bruno Mendes', 19),
               ('Carla Oliveira', 25)
''')

# cursor.execute('''
# INSERT INTO aluno (nome, idade) VALUES ('Bruno Mendes', 19)
# ''')

# cursor.execute('''
# INSERT INTO aluno (nome, idade) VALUES ('Carla Oliveira', 25)
# ''')

conexao.commit()

cursor.execute('SELECT * FROM aluno')
for linha in cursor.fetchall():
    print(linha)


conexao.close()