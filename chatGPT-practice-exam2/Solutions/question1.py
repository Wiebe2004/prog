class Book:
    def __init__(self, title, author, year):
        self._title = title
        self.author = author
        self.__year = year

    @property
    def title(self):
        return self._title
    
    @title.setter
    def title(self, new_title):
        if type(new_title) == str:
            self._title = new_title
        else:
            raise ValueError("Title must be of type string")

    @property
    def year(self):
        return self.__year

    @year.setter
    def year(self, new_year):
        if new_year < 0:
            raise ValueError("Year must be positive")
        elif type(new_year) != int:
            raise ValueError("Year must be of type integer")
        else:
            self.__year = new_year

    def get_info(self):
        return '{} written by {} in the year {}'.format(self._title, self.author, self.__year)
    
    def update_info(self, title=None, author=None, year=None):
        if title is not None:
            self.title = title
        if author is not None:
            self.author = author
        if year is not None:
            self.year = year



class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        if book is not None and book not in self.books:
            self.books.append(book)
        else:
            raise ValueError(f'{book} is already in the library')
        
    def remove_book(self, title):
        if title is not None and any(book.title == title for book in self.books):
            for book in self.books:
                if book.title.lower() == title.lower():
                    self.books.remove(book)
                    break
        else:
            raise ValueError(f'{title} is not in the library, sorry!')


    def find_book_title(self, title):
        if title is not None and any(book.title == title for book in self.books):
            for book in self.books:
                if book.title.lower() == title.lower():
                    return book.get_info()
                    
        else:
            raise ValueError(f'{title} is not in the library, sorry!')

    def list_books_by_author(self, author):
        if author is not None and any(book.author == author for book in self.books):
            books_by_author = []
            for book in self.books:
                if book.author.lower() == author.lower():
                    books_by_author.append(book.get_info())

            if books_by_author:
                return books_by_author    
            else:
                raise ValueError(f'{author}\'s books are not in the library, sorry!')
        else:
            raise ValueError(f'{author}\'s books are not in the library, sorry!')



# Create a library instance
library = Library()

# Create some book instances
book1 = Book("1984", "George Orwell", 1949)
book2 = Book("Animal Farm", "George Orwell", 1945)
book3 = Book("To Kill a Mockingbird", "Harper Lee", 1960)
book4 = Book("Brave New World", "Aldous Huxley", 1932)

# Add books to the library
library.add_book(book1)
library.add_book(book2)
library.add_book(book3)
library.add_book(book4)

# List all books by George Orwell
print("Books by George Orwell:")
print(library.list_books_by_author("George Orwell"))

# Find a specific book by title
print("\nFinding '1984':")
print(library.find_book_title("1984"))

# Update the title of a book
book1.update_info(title="Nineteen Eighty-Four")
print("\nUpdated '1984' to 'Nineteen Eighty-Four':")
print(library.find_book_title("Nineteen Eighty-Four"))

# Remove a book by title
print("\nRemoving 'Animal Farm':")
library.remove_book("Animal Farm")
print(library.list_books_by_author("George Orwell"))

# Try to find a book that doesn't exist
try:
    print("\nFinding 'Animal Farm' after removal:")
    print(library.find_book_title("Animal Farm"))
except ValueError as e:
    print(e)

# List all books by an author not in the library
try:
    print("\nListing books by an unknown author:")
    print(library.list_books_by_author("J.K. Rowling"))
except ValueError as e:
    print(e)
