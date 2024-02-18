from book import Book

class Library:

    def __init__(self, db):
        self.db = db
        self.books = db.read_books()

    
    def get_books(self):
        return self.books


    def add_book(self, *args):
        book = Book(*args)
        self.books.append(book)
        self.db.write_books(self.books)


    def remove_book(self, name):
        length_before = len(self.books)
        self.books = [book for book in self.books if book.name != name]
        self.db.write_books(self.books)
        length_after = len(self.books)
        return length_before > length_after


    def search_book(self, search_value, find_exact_match):
        if find_exact_match:
            return [book for book in self.books if search_value.lower() == book.name.lower()]
        else:
            return [book for book in self.books if search_value.lower() in book.name.lower()]
