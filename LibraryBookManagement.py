'''Library Book Management

You are tasked with creating a library book management system using classes and the @dataclass decorator. Each book in the library should have the following properties: title, author, year of publication, and quantity.

Create a Book class using the @dataclass decorator to represent an individual book in the library. The class should have the following fields: title, author, year, quantity.

Implement a display_info method that prints information about the book in the following format: "Title: {title}, Author: {author}, Year of Publication: {year}, Quantity in Library: {quantity}".

Create a Library class that represents a library. It should have a list of Book objects called books.

Implement an add_book method that adds a new book to the library. The method should take arguments for each property of the book and create a new instance of the Book class. Then, this instance should be added to the books list in the Library object.

Implement a search_book method that searches for a book by its title. The method should take the book title as an argument and return a list of all books with that title.

Implement a borrow_book method that decreases the available quantity of a book in the library by 1 each time it is called. The method should take the book title as an argument.

Implement a return_book method that increases the available quantity of a book in the library by 1 each time it is called. The method should take the book title as an argument.

Your task is to:

Create the Book and Library classes using the @dataclass decorator.
Implement the display_info, add_book, search_book, borrow_book, and return_book methods in the Library class.
Create an instance of the Library class named library.
Add several books to the library using the add_book method.
Demonstrate the use of the search_book, borrow_book, and return_book methods to work with books in the library.
Successfully completing this task will help you better understand the usage of the @dataclass decorator, creating classes to store data, and their interactions.'''


from dataclasses import dataclass, field
from typing import List

@dataclass
class Book:
    title: str
    author: str
    year: int
    quantity: int

    def display_info(self):
        print(f"Title: {self.title}, Author: {self.author}, Year of Publication: {self.year}, Quantity in Library: {self.quantity}")

@dataclass
class Library:
    books: List[Book] = field(default_factory=list)

    def add_book(self, title, author, year, quantity):
        book = Book(title, author, year, quantity)
        self.books.append(book)

    def search_book(self, title):
        found_books = []
        for book in self.books:
            if book.title == title:
                found_books.append(book)
        return found_books

    def borrow_book(self, title):
        for book in self.books:
            if book.title == title:
                if book.quantity > 0:
                    book.quantity -= 1
                    print(f"Book '{book.title}' has been borrowed.")
                else:
                    print(f"No available copies of '{book.title}' in the library.")

    def return_book(self, title):
        for book in self.books:
            if book.title == title:
                book.quantity += 1
                print(f"Book '{book.title}' has been returned.")

library = Library()

library.add_book("Book 1", "Author 1", 2022, 5)
library.add_book("Book 2", "Author 2", 2020, 3)
library.add_book("Book 3", "Author 3", 2021, 2)
library.add_book("Book 4", "Author 4", 2019, 1)

for book in library.books:
    book.display_info()

found_books = library.search_book("Book 1")
if found_books:
    print("Found Books:")
    for book in found_books:
        book.display_info()
else:
    print("No books found with the given title.")

library.borrow_book("Book 1")

library.return_book("Book 1")
