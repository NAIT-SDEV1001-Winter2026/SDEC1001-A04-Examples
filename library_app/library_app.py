from book import *
from library import *

if __name__ == "__main__":
    library1 = Library("Library of Alexandria")

    book1 = Book("House of leaves","Mark Z Daniel.....",800)

    library1.add_book(book1)
    #Shortcut
    library1.add_book(Book("Good stuff", "Shane Bell",2))
    library1.list_books()
    
    #In the library class create a get_book_by_title(self, title) method
    #if the title is in the library, return the book object
    #if it does not exist return None

    #test in the mainline
    #Display "Not found" if not in the library
    #Display the title by Author if in the library