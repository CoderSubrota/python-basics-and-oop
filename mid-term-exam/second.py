class Book:
    def __init__(self,book_id,title,author,availability=True):
        self.book_id=book_id
        self.title=title
        self.author=author
        self.availability=availability
        
    def __repr__(self):
        return f"{self.book_id} {self.title} {self.author} {self.availability}"
        
book_info = Book("10","Biology","Clark", True) 
book_info2 = Book("15","Physics","Newton", False) 
book_info3 = Book("18","Chemistry","Ball", True) 

print(book_info)
print(book_info2)
print(book_info3)


