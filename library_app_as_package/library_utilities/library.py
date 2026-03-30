from csv import DictWriter,DictReader
#When importing from within a package, they must use . (this package)
#the path will be relative to this package (.book)
#when code is inside a package python stops assuming the current folder is the import location
from .book import *

class Library:
    # A constructor that stores the library name and starts with an empty book collection
    def __init__(self,name):
        self.name = name
        self.books = []#list of book objects
    
    # A method to add a Book to the library
    def add_book(self,book):
        self.books.append(book)
    
    # A string representation that prints only the library name(using the __str__ dunder method)
    def __str__(self):
        print(self.name)

#     A method to list books with formatting:
#   - 'Current books in our library:' followed by a dash-prefixed list or a 'No books in our library' message
    def list_books(self):
        print("Current books in our library:")
        if len (self.books) == 0:#empty list
            print("No books in our library")
        else:
            for book in self.books:
                print (f"- {book}")

    def get_book_by_name(self, title):
        return_value = None
        for book in self.books:
            if book.title.lower() == title.lower():
                return_value = book
        return return_value
    
    def write_books_to_csv(self, file_path):
        with open(file_path,"w",newline="") as f:
            field_names = ["title","author", "pages"]
            writer = DictWriter(f,fieldnames = field_names)
            writer.writeheader()

            #write each object in the list to the file
            for book in self.books:
                #create a dictionary entry of the book object to write to the file using DictWriter
                writer.writerow(
                    {"title": book.title,
                    "author": book.author,
                    "pages": book.pages})
    #Write the file into a list and return the list
    def import_books(self, file_path):
        with open(file_path,"r", newline ="") as f:
            reader = DictReader(f)
            for row in reader:
                self.books.append(Book(row["title"],row["author"],row["pages"]))
        return self.books
                    
                
