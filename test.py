from book import Book
from user import User
#TC1
libro = Book("libro6", "George Orwell", 1949, "1234567890")
print(libro.title)

Usuario = User("Carlos", 1)
print(Usuario.name)
Usuario.register_borrow(libro)
print(Usuario.history)