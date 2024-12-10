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
            f"Availability: {availability_status}\n"
        )

class Library:
    book_list = []

    @classmethod
    def entry_book(self, book):
        self.book_list.append(book)

    @classmethod
    def view_all_books(self):
        if not self.book_list:
            return "No books in the library."
        return "\n".join(book.view_book_info() for book in self.book_list)

    @classmethod
    def find_book(self, book_id):
        for book in self.book_list:
            if book.book_id == book_id:
                return book
            else:
                print("Book not found !!")
        return None

Library.entry_book(Book(1, "Python Programming", "Author A"))
Library.entry_book(Book(2, "Data Science Essentials", "Author B"))
Library.entry_book(Book(3, "Machine Learning", "Author C"))

def menu():
    while True:
        print("\nLibrary Menu:")
        print("1. View All Books")
        print("2. Borrow Book")
        print("3. Return Book")
        print("4. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            print("\nAll Books:")
            print(Library.view_all_books())

        elif choice == "2":
            try:
                book_id = int(input("Enter the Book ID to borrow: "))
                book = Library.find_book(book_id)
                if book:
                    print(book.borrow_book())
                else:
                    print("Book not found.")
 
            except:
                print("Invalid input. Please enter a valid Book ID.")

        elif choice == "3":
            try:
                book_id = int(input("Enter the Book ID to return: "))
                book = Library.find_book(book_id)
                if book:
                    print(book.return_book())
                else:
                    print("Book not found.")
            except ValueError:
                print("Invalid input. Please enter a valid Book ID.")

        elif choice == "4":
            print("Exiting the library system. Goodbye!")
            break

        else:
            print("Invalid choice. Please select a valid option.")

menu()
