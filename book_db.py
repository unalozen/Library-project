from book import Book

class BookDb:
    def __init__(self, file_path):
        self.seperator = ","    
        self.file_path = file_path
    
        # Initialize an empty file if it doesn't exist
        with open(self.file_path, "a") as _:
            pass
    

    def read_books(self):
        books = []
        with open(self.file_path, "r") as f:
            for line in f.read().splitlines():
                books.append(self.parse_book(line))
        
        return books


    def write_books(self, books):
        with open(self.file_path, "w") as f:
            f.writelines(self.serialize_book(book) for book in books)
    

    def parse_book(self, line):
        columns = line.split(self.seperator)
        return Book(*columns)
    

    def serialize_book(self, book):
        return self.seperator.join([book.name, book.author, book.release_date, book.number_of_pages]) + "\n"
