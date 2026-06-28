class Book:
    def __init__(self,title):
        self.title=title
class Library:
    def __init__(self):
        self.books=[]
    
    def borrow_book(self,book):
        self.books.append(book)
    
    def return_book(self):
        for book in self.books:
            print("book.title")


library=Library()
book1=Book("Tom Gates by Liz Pichon")
book2=Book("Harry Potter by JK Rowling")
book3=Book("The mcc by Sudha Murthy")

library.borrow_book(book1)
library.borrow_book(book2)
library.borrow_book(book2)

library.return_book()

