
class Book:
    def __init__(self, title, author, publisher, publishing_year, price):
        self.title = title
        self.author = author
        self.publisher = publisher
        self.publishing_year = publishing_year
        self.price = price

class Library:
    def __init__(self):
        self.books = []

    def addbook(self, book):
        self.books.append(book)

    def displaybooks_author(self, authorname):
        author_books = [book for book in self.books if book.author == authorname]
        if author_books:
            for book in author_books:
                print(f"Title: {book.title}, Author: {book.author}, Publisher: {book.publisher}, Year: {book.publishing_year}, Price: {book.price}")
        else:
            print(f"No books found by {authorname}")

    def sorted_books(self, filename):
        sorted_books = sorted(self.books, key=lambda book: book.price)
        with open(filename, 'w') as file:
            for book in sorted_books:
                file.write(f"Title: {book.title}, Author: {book.author}, Publisher: {book.publisher}, Year: {book.publishing_year}, Price: {book.price}\n")

    def display_books_from_file(self, filename):
        try:
            with open(filename, 'r') as file:
                for line in file:
                    print(line.strip())
        except FileNotFoundError:
            print(f"File {filename} not found.")

    def check_book_price(self, book):
        if book.price > 10000:
            raise Exception("Price of the book is More than Rs 10000.")


library = Library()

book1 = Book("Computer Fundamental", "Ravi", "Dainik Publishing ", 2000, 500)
book2 = Book("Sciencifitcs Facts", "Aman", "Science Publishing", 2010, 400)
book3 = Book("A to Z Coding", "Naresh", "Coderhub Publishing", 2023, 15000)
book4 = Book("Rich Dad Poor Dad", "Robert", "Gold Mine Publishing", 2015, 250)

library.addbook(book1)
library.addbook(book2)
library.addbook(book3)
library.addbook(book4)

print("Books by Author1:")
library.displaybooks_author("Author1")


library.sorted_books("sorted_books.txt")
print("Contents of the sorted_books.txt file:")
library.display_books_from_file("sorted_books.txt")

try:
    library.check_book_price(book3)
except Exception as e:
    print(e)


