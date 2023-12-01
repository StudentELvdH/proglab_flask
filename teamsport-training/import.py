import csv
import os

from flask import Flask, render_template, request
from models import *

# Check for environment variable
if not os.getenv("DATABASE_URL"):
    raise RuntimeError("DATABASE_URL is not set")

app = Flask(__name__)
# Tell Flask what SQLAlchemy databas to use.
app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("DATABASE_URL")
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
# Link the Flask app with the database (no Flask app is actually being run yet)
db.init_app(app)

def main():
    f = open("exercise.csv")
    reader = csv.reader(f)
    next(reader)
    
    #for book, title, author, year in reader:    
    #    exercise = Exercise(isbn=isbn, title=title, author=author, year=year)
    #    db.session.add(exercise)
    #    print(f"Added {isbn} with {title} from {author} published in {year}.")
    db.session.commit()

if __name__ == "__main__":
    # Allows for command line interaction with Flask application
    with app.app_context():
        main()
