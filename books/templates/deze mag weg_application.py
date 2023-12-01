from flask import Flask, render_template

app = Flask(__name__)

@app.route("/book/<isbn>")
#def index():

#def book(isbn):
    #return render_template("bookpage.html")

def book(isbn):
    # """Book a flight."""
    # get the book with the right isbn from the database. 
    # Then pass on that book to the template and have the template render the title, isbn, etc.
    
    # Get form information.
    isbn = request.form.get("book")
    try:
        isbn = str(request.form.get("isbn"))
    except ValueError:
        return render_template("error.html", message="Invalid isbn")

    # Make sure isbn exists.
    if db.execute("SELECT * FROM books WHERE isbn = :isbn", {"isbn": isbn}).rowcount == 0:
        return render_template("error.html", message="No such book with that isbn")
    db.execute("INSERT INTO books (isbn) VALUES (:isbn)",
            {"isbn": isbn})
    db.commit()
    return render_template("bookpage.html")