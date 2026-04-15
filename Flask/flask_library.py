# What is Flask?
# A lightweight/micro web server for development of web pages using Python along with HTML
# to start the server and load the home page ("/") flask --app flask_library run --reload
# --reload will restart the server whenever you refresh the browser (to show the current content)

from flask import Flask # import the Flask module  
from flask import jsonify # turns python data (lists,dictionaries) into json so it can be read 

app = Flask(__name__) #Create a flask object called app.   __name__ tells Flask where the file is
#app will be used to define routes(URLS/pages) of the site

#When the URL is visited , run the functions following this line
#Every route has a function that determines what to send to the browser
#@ us called a decorator. 
@app.route("/") # / is the root of the site. 
def home():#function called home (could be any name)
    return "<h1>Welcome to the Book Library!</h1>"

books  = [
    {"title":"1984","author":"George Orwell"},
    {"title":"Grilled Cheese","author":"Shane Bell"}
]

@app.route("/books")
def books_list():
    return jsonify(books)


