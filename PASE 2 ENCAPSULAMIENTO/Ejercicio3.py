class Book:
    def __init__(self, title, author, pages):
        self.__title = title
        self.__author = author
        self.__pages = pages

    def show(self):
        print(f"Título: {self.__title}")
        print(f"Autor: {self.__author}")
        print(f"Número de páginas: {self.__pages}")

    def read(self):
        # TELL DON'T ASK
        print(f"Estás leyendo '{self.__title}' de {self.__author}.")

    def big_book(self):
        if self.__pages > 300:
            print("Este es un libro largo.")
        else:
            print("Este es un libro corto.")

    def all(self, list_books):
            print("Libros:")
            for books in list_books:
                books.show()
                books.big_book()
                print()

Book1 = Book("Cien Años de Soledad", "Gabriel García Márquez", 417)
Book2 = Book("El Principito", "Antoine de Saint-Exupéry", 96)
Book3 = Book("1984", "George Orwell", 328)

list_books = [Book1, Book2, Book3]


Book1.all(list_books)