import sqlite3

def executar_consultas():
    
    conn = None
    try:
        conn = sqlite3.connect('escola_v2.db')
        cursor = conn.cursor()
        print("--- Conexão com escola_v2.db estabelecida com sucesso. ---")

        print("\n--- 2. Todos os registros da tabela Aluno ---")
        cursor.execute("SELECT * FROM Aluno;")
        alunos = cursor.fetchall()
        for aluno in alunos:
            print(aluno)

        print("\n--- 3. Top 10 maiores médias (nota1 + nota2) ---")
        query_media = """
            SELECT nome, (nota1 + nota2) / 2 AS media
            FROM Aluno
            ORDER BY media DESC
            LIMIT 10;
        """
        cursor.execute(query_media)
        top_10_medias = cursor.fetchall()
        
        for i, (nome, media) in enumerate(top_10_medias):
            print(f"{i+1}. Nome: {nome}, Média: {media:.2f}")

        print("\n--- 4. LEFT JOIN entre Aluno e Turma (Todos os dados) ---")
       
        query_join = """
            SELECT 
                Aluno.id, 
                Aluno.nome AS nome_aluno, 
                Aluno.nota1, 
                Aluno.nota2, 
                Turma.nome AS nome_turma, 
                Turma.semestre, 
                Turma.ano
            FROM Aluno
            LEFT JOIN Turma ON Aluno.id_turma = Turma.id;
        """
        cursor.execute(query_join)
        join_completo = cursor.fetchall()
        for linha in join_completo:
            print(linha)

        print("\n--- 5. LEFT JOIN (filtrando apenas Turma 2) ---")
        
        
        query_join_filtrado = """
            SELECT 
                Aluno.id, 
                Aluno.nome AS nome_aluno, 
                Aluno.nota1, 
                Aluno.nota2, 
                Turma.nome AS nome_turma, 
                Turma.semestre, 
                Turma.ano
            FROM Aluno
            LEFT JOIN Turma ON Aluno.id_turma = Turma.id
            WHERE Aluno.id_turma = ?; 
        """
        
        id_da_turma = (2,) 
        cursor.execute(query_join_filtrado, id_da_turma)
        join_filtrado = cursor.fetchall()
        
        if join_filtrado:
            for linha in join_filtrado:
                print(linha)
        else:
            print("Nenhum aluno encontrado para a turma 2.")

    except sqlite3.Error as e:
        print(f"Ocorreu um erro ao interagir com o banco de dados: {e}")
    
    finally:
        if conn:
            conn.close()
            print("\n--- Conexão com o banco de dados fechada. ---")

if __name__ == "__main__":
    executar_consultas()