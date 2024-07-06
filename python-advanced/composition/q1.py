# Defining the Component classes
class Author:

    def __init__(self, name, nationality):
        self.name = name
        self.nationality = nationality

    def __str__(self):
        return f"{self.name} ({self.nationality})"
    

class Book:

    def __init__(self, title, author, publication_year):
        self.title = title
        self.author = author # this will be the instance of author 
        self.publication_year = publication_year

    def __str__(self):
        return f"{self.title} by {self.author}, published in {self.publication_year}"
    

# Defining the composite class 
class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def list_books(self):
        for i in self.books:
            print(i, " ")
    
# use the composite class
author1 = Author("George S. Clason", "American")
author2 = Author("Robert Kiyosaki", "American")

# Create books 
book1 = Book("The Richest Man in Bablyon", author1, 1926)
book2 = Book("Rich Dad Poor Dad", author2, 1997)


# Create a library and add books to it 
library = Library()
library.add_book(book1)
library.add_book(book2)


library.list_books()