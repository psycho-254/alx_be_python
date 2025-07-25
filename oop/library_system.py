# Objective: Deepen your understanding of inheritance and composition in Python by 
# creating a system that models a library with different types of books.

# Task Description:
# Develop two Python scripts: library_system.py and main.py. In library_system.py, 
# you’ll define a base class Book and two derived classes, EBook and PrintBook, showcasing inheritance. 
# Additionally, implement a Library class demonstrating composition by managing a collection of books.

# library_system.py:
# Base Class - Book:

# Attributes: title (str) and author (str).
# Method: __init__(self, title, author) for initializing book attributes.
# Derived Classes - EBook and PrintBook:

# Both classes inherit from Book.
# EBook additional attribute: file_size (int).
# PrintBook additional attribute: page_count (int).
# Each derived class should have its own __init__ method that properly calls 
# the base class __init__ while also initializing its unique attribute.
# Composition - Library:

# Attributes: books (a list to store instances of Book, EBook, and PrintBook).
# Methods:
# add_book(self, book): Adds a Book, EBook, or PrintBook instance to the library.
# list_books(self): Prints details of each book in the library.

# Expected Output:
# Your output should list the details of each book added to the library, 
# reflecting the specific attributes of EBook and PrintBook, as well as the common attributes inherited from Book.

# Book: Pride and Prejudice by Jane Austen
# EBook: Snow Crash by Neal Stephenson, File Size: 500KB
# PrintBook: The Catcher in the Rye by J.D. Salinger, Page Count: 234

class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
    def __str__(self):
        return F"Book: {self.title} by {self.author}"
    
class EBook(Book):
    def __init__(self, title, author, file_size):
        super().__init__(title, author)
        self.file_size = file_size

    def __str__(self):
        return f"EBook: {self.title} by {self.author}, File Size: {self.file_size}KB"
class PrintBook(Book):
    def __init__(self, title, author, page_count):
      super().__init__(title, author)
      self.page_count = page_count

    def __str__(self):
        return f"PrintBook: {self.title} by {self.author}, Page Count: {self.page_count}"
    
class Library:
    def __init__(self):
        self.books = []
    def add_book(self, book):
        self.books.append(book)

    def list_books(self):
        for book in self.books:
            print(book)