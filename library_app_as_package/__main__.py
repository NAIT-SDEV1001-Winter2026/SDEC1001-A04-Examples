# Can be run from the terminal with: python -m package_name
# Usually should not be run with VS Code's normal "Run Python File" button,
# because that runs this file directly instead of running the package.
# Makes the package the application entry point instead of treating one file as the app.
# Gives you one official entry point: run the package, not random individual files.
# Keeps related code together in one self-contained unit.
# This structure also works better for command-line tools and code that may later be distributed.


from pathlib import Path
from .library_utilities.book import *#. means "from this package"
from .library_utilities.library import *

#base_dir = Path(__file__).parent #same folder as __main__
#base_dir = Path(__file__).parent.parent #parent folder of the folder where __main__ is (and so on)
#file_path = base_dir/"books.csv"
#instead of .parent.parent 
base_dir = Path.cwd() #Current Working Directory
#Current Working Directory is the location(folder) where you are running the application from
#Where am I now
#Path(__file__).parent.parent is the same as Path.cwd() 
file_path = base_dir/"books.csv"

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

    search_book = input("Enter a book to search for: ")
    found_book = library1.get_book_by_name(search_book.strip())
    if found_book is None:
        print(f"Sorry, {search_book} is not in the library")
    else:
        print(f"{found_book}")

    library1.write_books_to_csv(file_path)
    print("List books from the file")
    #NOTE: Each book will appear twice becuase the library already had 2 books in it from top of this file .....
    new_list = library1.import_books(file_path)
   
    for book in new_list:
        print(book)
    







