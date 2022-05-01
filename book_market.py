

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
        if book.isbn in self.storage:
            self.storage[book.isbn]['count'] += 1
        else:
            self.storage[book.isbn] = {
                'count': 1,
                'book': book
            }

    def show(self):
        for idx, isnb, record in enumerate(self.storage.items(), start=1):
            print(idx, '.', record['book'].to_string(), '-', record(['count']))




def add_book():

    global collection


    collection = BookCollection()

    isbn = input("ISBN: ")
    title = input("Title: ")
    authors = input("Authors: ").strip().split(',')

    collection.add(Book(isbn, title, authors))


def borrow_book():
    pass


def remove_book():
    pass


def show_book():
    global collection

    collection.show()


def show_books():
    pass



if __name__ == "__main__":
    commands = (
        "add-book",
        "borrow-books",
        "show-book",
        "remove-book"
    )

    while True:
        cmd = input("Command: ").lower().strip()

        if cmd not in commands:
            print("[ERROR] - you should enter a valid command")
            continue

        globals()[cmd.replace("-", "_").lower()]()

