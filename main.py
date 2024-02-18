from library import Library
from book_db import BookDb

class UI:
    possible_choices = ["1","2","3","4","q"]

    def menu():
        print("""
*** MENU ***
1) List Books
2) Add Book
3) Remove Book
4) Search Book
q) Quit
""")

        choice = input("Enter Your Choice: ")
        print("\n")

        if choice in UI.possible_choices:

            if choice == "1":
                UI.list_books()

            elif choice == "2":
                UI.add_book()

            elif choice == "3":
                UI.remove_book()

            elif choice == "4":
                UI.search_book()

            else:
                quit()

        else:
            print("Wrong Input! Try Again")


    def list_books():
        print("   Book, Author")
        print("   ------------")

        for book in UI.lib.get_books():
            print(book)


    def add_book():
        book_name = input("Book Name: ")
        author_name = input("Author: ")
        date = input("Date: ")
        pages = input("Pages: ")

        if UI.is_empty(book_name) or UI.is_empty(author_name) or UI.is_empty(date) or UI.is_empty(pages):
            print("\nNull value(s) can't assign!")
            return

        if not UI.is_integer(date) or not UI.is_integer(pages):
            print("\nDate and pages must be integer!")
            return

        if len(UI.lib.search_book(book_name, True)) != 0:
            print("\nBook already in library!")
            return

        UI.lib.add_book(book_name, author_name, date, pages)
        print("\nBook added to library!")


    def remove_book():
        remove_book = input("Write a book name to remove: ")
        if UI.lib.remove_book(remove_book):
            print("\nBook removed from library!")
        else:
            print("\nWrong book name! Try Again")


    def search_book():
        search_value = input("Write a book name to search: ")
        result = UI.lib.search_book(search_value, False)
        if len(result) == 0:
            print("\nNo book found")
            return
        for book in result:
            print(book.show_details())


    def is_empty(value):
        return len(value.strip()) == 0


    def is_integer(value):
        try:
            return isinstance(int(value), int)
        except:
            return False


if __name__ == '__main__':
    db = BookDb("books.txt")
    UI.lib = Library(db)

    while True:
        UI.menu()
