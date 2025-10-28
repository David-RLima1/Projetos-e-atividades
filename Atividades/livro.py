class Livro:
    def __init__(self, titulo, autor, ano):
        self.titulo = titulo
        self.autor = autor
        self.ano = ano

    def __str__(self):
        return f"{self.titulo} - {self.autor} - {self.ano}"
    

livro = Livro("Harry Potter", "J.K Rowling", 1997)
print(livro)