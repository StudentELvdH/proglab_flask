import os

from flask import Flask, session, request, render_template
from flask_session import Session
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

from models import *

app = Flask(__name__)

# Check for environment variable
if not os.getenv("DATABASE_URL"):
    raise RuntimeError("DATABASE_URL is not set")

app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("DATABASE_URL")
db.init_app(app)

# Configure session to use filesystem
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"

Session(app)


@app.route("/")
def index():
    return "Project 1: TODO - deze stap uitwerken"

@app.route("/>", methods=["GET"])
def book(isbn):
   
    # Get form information.
    #isbn = request.form.get("isbn")
    #try:
    #    isbn = str(request.form.get("isbn"))
    #except ValueError:
    #    return render_template("error.html", message="Invalid isbn")
    # print(isbn)
    
    # Make sure isbn exists-> nu in ORM
    #if Book.query.filter_by(isbn=isbn)
    
    # Make sure isbn exists.
    #if db.execute("SELECT * FROM books WHERE isbn = :isbn", {"isbn": isbn}).rowcount == 0:
    #    return render_template("error.html", message="No such exercise with that code")
    #db.execute("INSERT INTO books (isbn) VALUES (:isbn)",
    #        {"isbn": isbn})
    db.commit()
    return render_template("exercise.html")

