""" database dependencies to support Users db examples """
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.exc import IntegrityError
from flask_migrate import Migrate

from __init__ import app

# Tutorial: https://www.sqlalchemy.org/library.html#tutorials, try to get into Python shell and follow along
# Define variable to define type of database (sqlite), and name and location of myDB.db
dbURI = 'sqlite:///model/myDB.db'
# Setup properties for the database
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = dbURI
app.config['SECRET_KEY'] = 'SECRET_KEY'
# Create SQLAlchemy engine to support SQLite dialect (sqlite:)
db = SQLAlchemy(app)
Migrate(app, db)


# Define the Users table within the model
# -- Object Relational Mapping (ORM) is the key concept of SQLAlchemy
# -- a.) db.Model is like an inner layer of the onion in ORM
# -- b.) Users represents data we want to store, something that is built on db.Model
# -- c.) SQLAlchemy ORM is layer on top of SQLAlchemy Core, then SQLAlchemy engine, SQL
class Users(db.Model):
    # define the Users schema
    userID = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), unique=False, nullable=False)
    email = db.Column(db.String(255), unique=True, nullable=False)
    password = db.Column(db.String(255), unique=False, nullable=False)

    # constructor of a User object, initializes of instance variables within object
    def __init__(self, name, email, password):
        self.name = name
        self.email = email
        self.password = password

    # CRUD create/add a new record to the table
    # returns self or None on error
    def create(self):
        try:
            # creates a person object from Users(db.Model) class, passes initializers
            db.session.add(self)  # add prepares to persist person object to Users table
            db.session.commit()  # SqlAlchemy "unit of work pattern" requires a manual commit
            return self
        except IntegrityError:
            db.session.remove()
            return None

    # CRUD read converts self to dictionary
    # returns dictionary
    def read(self):
        return {
            "userID": self.userID,
            "name": self.name,
            "email": self.email,
            "password": self.password,
        }

    # CRUD update: updates users name, password
    # returns self
    def update(self, name, email, password=""):
        """only updates values with length"""
        if len(name) > 0:
            self.name = name
        if len(email) > 0:
            self.email = email
        if len(password) > 0:
            self.password = password
        db.session.commit()
        return self

    # CRUD delete: remove self
    # None
    def delete(self):
        db.session.delete(self)
        db.session.commit()
        return None


"""Database Creation and Testing section"""


def model_tester():
    print("--------------------------")
    print("Seed Data for Table: users")
    print("--------------------------")
    db.create_all()
    """Tester data for table"""
    u1 = Users(name='Novak Djokovic', email='Djokovic@gmail.com', password='aaa')
    u2 = Users(name='Daniil Medvedev', email='Medvedev@gmail.com', password='bbb')
    u3 = Users(name='Alexander Zverev', email='Zverev@gmail.com', password='ccc')
    u4 = Users(name='Stefanos Tsitsipas', email='Tsitsipas@gmail.com', password='ddd')
    u5 = Users(name='Andrey Rublev', email='Rublev@gmail.com', password='eee')
    u6 = Users(name='Kevin Durant', email='KDTrey5@gmail.com', password='KD7')
    u7 = Users(name='Stephen Curry', email='Chef@gmail.com', password='SC30')
    u8 = Users(name='Kawhi Leonard', email='Klaw@gmail.com', password='kawhileonard')
    u9 = Users(name='Giannis Antetokounmpo', email='giannis@gmail.com', password='GIANNIS')
    u10 = Users(name='LeBron James', email='theKing@gmail.com', password='KING')
    # U7 intended to fail as duplicate key
    table = [u1, u2, u3, u4, u5, u6, u7, u8, u9, u10]
    for row in table:
        try:
            db.session.add(row)
            db.session.commit()
        except IntegrityError:
            db.session.remove()
            print(f"Records exist, duplicate email, or error: {row.email}")


def model_printer():
    print("------------")
    print("Table: users with SQL query")
    print("------------")
    result = db.session.execute('select * from users')
    print(result.keys())
    for row in result:
        print(row)


if __name__ == "__main__":
    model_tester()  # builds model of Users
    model_printer()
