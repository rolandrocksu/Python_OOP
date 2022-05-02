

class Book:

    def __init__(self, isbn: str, title: str, authors: tuple):
        self.isbn = isbn
        self.title = title
        self.authors = authors

    def to_string(self) -> str:
        return f'ISBN : {self.isbn}, Title: {self.title}, Authors: {self.authors}'


class BookCollection:

    def __init__(self):
        self.storage = {}

    def add(self, book: Book):
        if not isinstance(book, Book):
            raise TypeError("You can only add book object")

        if book.isbn in self.storage:
            self.storage[book.isbn]['count'] += 1
        else:
            with open("bookMarket.db", "a") as file:
                file.write(''.join([book.to_string(), "\n"]))
            self.storage[book.isbn] = {
                'count': 1,
                'book': book
            }

    def show(self):
        for idx, (isbn, record) in enumerate(self.storage.items(), start=1):
            print(idx, '.', record['book'].to_string(), '-', record['count'])

    def remove(self, book_isbn: str):
        del self.storage[book_isbn]

    def show_books(self):
        with open("bookMarket.db", "r") as file:
            print(file.readlines())


class Application:

    def __init__(self):
        self.collection = BookCollection()
        self.__exit = True

    COMMANDS: tuple = (
            "add-book",
            "borrow-books",
            "show-book",
            "remove-book",
            "show-books",
            "exit"
    )


    def run(self):

        while self.__exit:
            cmd = input("Command: ").lower().strip()

            if cmd not in Application.COMMANDS:
                print("[ERROR] - you should enter a valid command")
                continue

            getattr(self, cmd.replace("-", "_").lower())()


    def add_book(self):

        isbn = input("ISBN: ")
        title = input("Title: ").title()
        authors = input("Authors: ").strip().split(',')

        self.collection.add(Book(isbn, title, authors))


    def borrow_book(self):
        pass


    def remove_book(self):
        self.collection.remove(input("Enter book ISBN: "))


    def show_book(self):
        self.collection.show()


    def show_books(self):
        self.collection.show_books()

    def exit(self):
        self.__exit = False


if __name__ == "__main__":
    Application().run()