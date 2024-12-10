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

    def view_book_info(self):
        availability_status = "Available" if self.availability else "Not Available"
        return (
            f"Book ID: {self.book_id}\n"
            f"Title: {self.title}\n"
            f"Author: {self.author}\n"
            f"Availability: {availability_status}"
        )

book1 = Book(1, "Jane Eyre", "Charlotte Brontë")

print(book1.view_book_info())
print(book1.borrow_book())
print(book1.view_book_info())
print(book1.return_book())
print(book1.view_book_info())
