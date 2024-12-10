class Book:
    book_list = [] 

    def __init__(self, book_id, title, author, availability=True):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.availability = availability

    def entry_book(self):
        Book.book_list.append(self)

book1 = Book(1, "Don Quixote", "Miguel de Cervantes")
book2 = Book(2, "Alice's Adventures in Wonderland", "Lewis Carroll", False)
book3 = Book(3, "Treasure Island", "Robert Louis Stevenson")

book1.entry_book()
book2.entry_book()
book3.entry_book()

for book in Book.book_list:
    print(f"ID: {book.book_id}, Title: {book.title}, Author: {book.author}, Available: {book.availability}")
