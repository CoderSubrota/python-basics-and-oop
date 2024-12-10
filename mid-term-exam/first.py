class Library:
    book_list = []

    @classmethod
    def entry_book(self, book):
        self.book_list.append(book)

class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def __repr__(self):
        return f"Book(title='{self.title}', author='{self.author}')"

b1 = Book("Physics", "Newton")
b2 = Book("To Kill a Mockingbird", "Harper Lee")

Library.entry_book(b1)
Library.entry_book(b2)

print(Library.book_list)
