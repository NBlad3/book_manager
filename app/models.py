from app import db

class User(db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key = True, auto_increment = True)
    username = db.Column(db.String(255), nullable = False, unique = True)
    password = db.Column(db.String(255), nullable = False)

class Book(db.Model):
    __tablename__ = "books"
    id = db.Column(db.Integer, primary_key = True, auto_increment = True)
    title = db.Column(db.String(255), nullable = False, unique = True)
    category = db.Column(db.String(255), nullable = False)

