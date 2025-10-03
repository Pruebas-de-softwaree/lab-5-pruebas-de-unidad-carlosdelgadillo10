from book import Book
#TC1
libro = Book("libro6", "George Orwell", 1949, "1234567890")
print(libro.title)
#TC2
libro.borrow()
print(libro.borrowed)
#TC3
libro.return_book()
print(libro.borrowed)