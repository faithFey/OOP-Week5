# Base class
class Book:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages

# Subclass
class EBook(Book):
    def __init__(self, title, author, pages, file_size):
        super().__init__(title, author, pages)
        self.file_size = file_size

# Creating objects
book1 = Book("The Journey", "Moses Bells", 310)
ebook1 = EBook("Python Statistics", "Faith", 150, 3)

# Printing details of the objects
print(book1.title, book1.author, book1.pages)
print(ebook1.title, ebook1.author, ebook1.pages, ebook1.file_size)
