from main import db                                                # This is the db instance created by SQLAlchemy

class User(db.Model):                                              # Creating a User class inheriting from db.Model
    __tablename__ = "users"                                        # Explicitally providing the name of the table

    id = db.Column(db.Integer, primary_key=True)                   # Creates a column called id and sets it al the primary key
    username = db.Column(db.String(), nullable=False, unique=True) # Username, string, must be present, must be unique
    firstname = db.Column(db.String(), nullable=False)             # Firstname, string, must be present
    lastname = db.Column(db.String(), nullable=False)              # Lastname, string, must be present
    email = db.Column(db.String(), nullable=False, unique=True)    # Email column, string andit must be unique
    password = db.Column(db.String(), nullable=False)              # The password is a string and must be present
    
    def __repr__(self):                                            # Reresentitive state
        return f"<User {self.username}>"                           # When the User is printed it now shows the username instead of the id