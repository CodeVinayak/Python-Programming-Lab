class Book:
    def __init__(self, title, author, publisher, publishing_year, price):
        self.title = title
        self.author = author
        self.publisher = publisher
        self.publishing_year = publishing_year
        self.price = price

    def display_details(self):
        print("Title:", self.title)
        print("Author:", self.author)
        print("Publisher:", self.publisher)
        print("Publishing Year:", self.publishing_year)
        print("Price:", self.price)

    def check_price(self):
        if self.price > 1000000:
            raise Exception("Price of book is beyond Rs 10000")

def display_books_by_author(books, author):
    print("Books written by", author)
    for book in books:
        if book.author == author:
            book.display_details()

def store_books_in_file(books, filename):
    books.sort(key=lambda book: book.price)
    with open(filename, "w") as f:
        for book in books:
            f.write(book.title + "," + book.author + "," + book.publisher + "," + str(book.publishing_year) + "," + str(book.price) + "\n")

def display_contents_of_file(filename):
    with open(filename, "r") as f:
        for line in f:
            print(line)


books = []
books.append(Book("The Lord of the Rings", "J.R Tolkien", "George", 1954, 500))
books.append(Book("The Hitchhiker's Guide to the Galaxy", "Adams", "Pan ", 1979, 100000))
books.append(Book("Harry Potter and the Sorcerer's Stone", "J.K. Rowling", "Bloom Publishing", 1997, 10000))

# Display books by author
display_books_by_author(books, "J.R.R. Tolkien")

# Check price of books
for book in books:
    book.check_price()

# Store books in file
store_books_in_file(books, "books.csv")

# Display contents of file
display_contents_of_file("books.csv")


