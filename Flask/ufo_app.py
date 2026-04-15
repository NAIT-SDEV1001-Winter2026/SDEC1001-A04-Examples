#read the sightings.csv file and display on the page

from flask import Flask, jsonify
import csv #or from csv import dictreader

app = Flask(__name__)

def load_ufo_data(filepath):
    sightings = []
    with open(filepath,"r",newline="") as f:
        reader = csv.DictReader(f)
        for row in reader:
            sightings.append(row)
    return sightings



#create a home page that displays a heading(h1) "UFO Sightings"
@app.route("/")
def home():
    #return a semantic webpage
    return """
    <html>
        <head>
            <title>UFO Sightings</title>
        </head>
        <body>
            <h1>UFO Sightings</h1>
        </head>
    <html>
    """

#enclosing the return string in """ allows us to write it out literaly like we would in an html file. Easier to read

#page to display contents of CSV file as json called ufo_sightings_file

#decorator
@app.route("/ufo_sightings_file")
#function header
def get_sightings_info():
#load data
    sightings = load_ufo_data("data/sightings.csv")
#return the json data
    return jsonify(sightings)





