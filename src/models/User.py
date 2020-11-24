from main import db                                                                   # This is the db instance created by SQLAlchemy
from models.Profile import Profile                                                    # Importing the Profile model
from models.League import League
from sqlalchemy.orm import backref                                                    # Used to make references to other tables

users_leagues = db.Table('users_leagues',
    db.Column('user_id', db.Integer, db.ForeignKey('users.id')),
    db.Column('league_id', db.Integer, db.ForeignKey('leagues.id'))
    )

class User(db.Model):                                                                 # Creating a Users class inheriting from db.Model
    __tablename__= "users"                                                            # Explicitly naming the table "users"

    id = db.Column(db.Integer, primary_key=True)                                      # There is an id column and it is the primary key
    email = db.Column(db.String(), nullable=False, unique=True)                       # Email column, string andit must be unique
    password = db.Column(db.String(), nullable=False)                                 # The password is a string and must be present
    profile = db.relationship("Profile", backref=backref("user", uselist=False))      # Creating the relationship to the profile table
    league = db.relationship("League", backref=backref("user"))      # Creating the relationship to the profile table
    users_leagues = db.relationship('League', secondary=users_leagues, backref=db.backref('users_leagues', lazy = 'dynamic'))
    category = db.relationship("Category", backref=backref("user"))

    def __repr__(self):                                                               # When printing the model we will see its email attribute
        return f"<User {self.email}>"