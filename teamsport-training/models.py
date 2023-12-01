from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Exercise(db.Model):
    __tablename__ = "exercises"
    #isbn = db.Column(db.String, primary_key=True)
    #title = db.Column(db.String, nullable=False)
    #author = db.Column(db.String, nullable=False)
    #year = db.Column(db.Integer, nullable=False)



