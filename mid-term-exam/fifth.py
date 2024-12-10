class Book:
    def __init__(self, book_id, title, author, availability=True):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.availability = availability

    def borrow_book(self):
        if self.availability:
            self.availability = False
            return f"The book '{self.title}' has been borrowed."
        else:
            return f"The book '{self.title}' is not available for borrowing."

    def return_book(self):
        if not self.availability:
            self.availability = True
            return f"The book '{self.title}' has been returned and is now available."
        else:
            return f"The book '{self.title}' was not borrowed."


book1 = Book(1, "Python Programming", "Author Z")

print(book1.borrow_book())
print(book1.return_book())
print(book1.return_book())
