# Objective: Solidify understanding of basic OOP concepts in Python by implementing a system that tracks books in a library, 
# focusing on classes, object instantiation, and method invocation.

# Your Task: library_management.py
# Implement a Book class with public attributes title and author, 
# and a private attribute _is_checked_out to track its availability.
# Implement a Library class with a private list _books to store instances of Book. 
# Include methods to add_book, check_out_book(title), return_book(title), and list_available_books.

# Note for you:
# Your Book class should provide methods to check a book out and return it, affecting its availability.
# Your Library class needs to manage a collection of books, including adding new books to the collection, 
# checking a book out (which marks it as unavailable), returning it (making it available again), 
# and listing all available books.
# Implementing these functionalities requires careful thought about how objects interact with each other 
# in terms of state and behavior.
# Use the provided main.py for testing your implementation. 
# The expected outputs give you a clear indication of how your program should behave if implemented correctly.


class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self._is_checked_out = False

    def check_out(self):
        if self._is_checked_out:
            return False
        else :
            self._is_checked_out = True
            return True
        
    def return_book(self):
        if self._is_checked_out :
            self._is_checked_out = False
            return True
        
        else:
            return False
        
class Library:
    def __init__(self):
        self._books = []

    def add_book(self, book):
        self._books.append(book)

    def check_out_book(self, title):
        for book in self._books:
            if book.title == title:
                return book.check_out()
        return False
    
    def return_book(self, title):
        for book in self._books:
            if book.title == title:
                return book.return_book()
        return False
    
    def list_available_books(self):
        for book in self._books:
            if book._is_checked_out == False:
        
             print(f"{book.title} by {book.author}")