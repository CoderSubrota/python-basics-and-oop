class Book:
    def __init__(self, book_id, title, author, availability=True):
        self.__book_id = book_id      
        self.__title = title          
        self.__author = author        
        self.__availability = availability

    @property
    def book_id(self):
        return self.__book_id

    @property
    def title(self):
        return self.__title

    @property
    def author(self):
        return self.__author

    @property
    def availability(self):
        return self.__availability

    def borrow_book(self):
        if not self.__availability:
            raise ValueError(f"The book '{self.__title}' is already borrowed.")
        self.__availability = False
        return f"The book '{self.__title}' has been borrowed successfully."

    def return_book(self):
        if self.__availability:
            raise ValueError(f"The book '{self.__title}' is not currently borrowed.")
        self.__availability = True
        return f"The book '{self.__title}' has been returned successfully."

    def view_book_info(self):
        availability_status = "Available" if self.__availability else "Not Available"
        return (
            f"Book ID: {self.__book_id}\n"
            f"Title: {self.__title}\n"
            f"Author: {self.__author}\n"
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
                if not book:
                    raise ValueError("Invalid Book ID.")
                print(book.borrow_book())
            except ValueError as e:
                print(f"Error: {e}")

        elif choice == "3":
            try:
                book_id = int(input("Enter the Book ID to return: "))
                book = Library.find_book(book_id)
                if not book:
                    raise ValueError("Invalid Book ID.")
                print(book.return_book())
            except ValueError as e:
                print(f"Error: {e}")

        elif choice == "4":
            print("Exiting the library system. Goodbye!")
            break

        else:
            print("Invalid choice. Please select a valid option.")

menu()
