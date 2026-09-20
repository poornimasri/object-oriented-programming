class Book:

    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.is_borrowed = False

    def borrow(self):
        if self.is_borrowed:
            print(self.title, "is already borrowed.")
        else:
            self.is_borrowed = True
            print(self.title, "has been borrowed.")

    def return_book(self):
        if not self.is_borrowed:
            print(self.title, "was not borrowed.")
        else:
            self.is_borrowed = False
            print(self.title, "has been returned.")

    def __str__(self):
        if self.is_borrowed:
            status = "Borrowed"
        else:
            status = "Available"
        return self.title + " by " + self.author + " [" + status + "]"


book1 = Book("Python Crash Course", "Eric Matthes")
book2 = Book("Harry Potter", "J.K. Rowling")
book3 = Book("The Hobbit", "J.R.R. Tolkien")

print("=" * 42)
print("         📚  LIBRARY SYSTEM")
print("=" * 42)

print(book1)
print(book2)
print(book3)

book1.borrow()
book1.borrow()

book2.borrow()

book1.return_book()
book3.return_book()

print("=" * 42)
print("         UPDATED LIBRARY")
print("=" * 42)

print(book1)
print(book2)
print(book3)