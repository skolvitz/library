import sys
from datetime import datetime
from datetime import timedelta

from filemodel import FileModel

library = {"World War Z": "Max Brooks",
           "Astrophysics for People in a Hurry": "Neil deGrasse Tyson",
           "The Double": "Fyodor Dostoevsky",
           "The Prestige": "Christopher Priest",
           "Brave New World": "Aldous Huxley",
           "1985": "Anthony Burgess",
           "The Stand": "Stephen King",
           "Ready Player One": "Ernest Cline",
           "Automate the Boring Stuff with Python: Practical Programming for Total Beginners": "Al Sweigart",
           "The Shining": "Stephen King"
           }
checked_out = {}


class FileView(object):

    def __init__(self):
        # self._getFile()
        self._methods = {"1": self._in, "2": self._out, "3": self._search_author, "4": self._search_book,
                         "5": self._check_out, "6": self._check_in, "7": self._quit}  # Jump table for commands

    def run(self):
        """A menu-driven command processor for a user."""
        print("\nWelcome to the Wake Tech Library!!!")
        print("Choose from the Following Options :\n")
        while True:

            print("1  List checked-in books")
            print("2  List checked-out books")
            print("3  Search authors")
            print("4  Search available books")
            print("5  Check out a book")
            print("6  Check in a book")
            print("7  Exit System\n")
            number = input("Enter a number: ")
            theMethod = self._methods.get(number, None)
            if theMethod is None:
                print("Unrecognized number")
            else:
                theMethod()
            #   if self._model is None:
            #      break

    def _getFile(self):
        filename = library
        self._model = FileModel(filename)

    #        line = self._model.first()
    #        self._printLine(line)

    def _in(self):
        if len(library) == 0:
            print("All books checked out.\n")
        else:
            for book, author in library.items():
                print(book, "by", author)
            print(" ")

    def _out(self):
        if len(checked_out) == 0:
            print("All books checked in.\n")
        else:
            for book, author in checked_out.items():
                print(book, "by", author)

    def _search_author(self):
        name = input("Enter author's full name: ")
        bookCount = 0
        for book, author in library.items():
            if author.lower() == name.lower():
                print(book)
                bookCount += 1
        if bookCount == 0:
            print("This author doesn't have any books in the library.\n")

    def _search_book(self):
        name = input("Enter book's name: ")
        bookCount = 0
        for book, author in library.items():
            if book.lower() == name.lower():
                print(book, "by", author, "\n")
                bookCount += 1
        if bookCount == 0:
            print("This book is not currently checked in.\n")

    def _check_in(self):
        name = input("Enter book name (case-sensitive): ")
        if name in checked_out:
            library[name] = checked_out.get(name)
            del checked_out[name]
            print(name, "has been checked in.\n")
        elif name in library:
            print("This book is already checked in.\n")
        else:
            print("This book does not belong this library.\n")

    def _check_out(self):
        name = input("Enter book name (case-sensitive): ")
        if name in library:
            checked_out[name] = library.get(name)
            print(name, "has been checked out.\n")
            del library[name]
        elif name in checked_out:
            print("Book is already checked out.\n")
        else:
            print("Book is not available to check out.\n")

    def _quit(self):
        if len(checked_out) != 0:
            for book, author in checked_out.items():
                dueDate = datetime.now() + timedelta(days = 14)
                print(book, "by", author, "is due back on or before", dueDate.strftime("%A"), dueDate.strftime("%B"), dueDate.day)
        else:
            print("No books were checked out.")
        print("Have a nice day!")
        sys.exit(0)


# Launch the application
if __name__ == "__main__":
    FileView().run()
