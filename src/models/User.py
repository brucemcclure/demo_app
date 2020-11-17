from main import db                                                                  # This is the db instance created by SQLAlchemy

class User(db.Model):                                                                # Creating a User class inheriting from db.Model
    __tablename__ = "users"                                                          # Explicitally providing the name of the table

    id = db.Column(db.Integer, primary_key=True)                                     # Creates a column called id and sets it al the primary key
    username = db.Column(db.String(), nullable=False, unique=True)                   # Username, string, must be present, must be unique
    firstname = db.Column(db.String(), nullable=False)                               # Firstname, string, must be present
    lastname = db.Column(db.String(), nullable=False)                                # Lastname, string, must be present
    account_id = db.Column(db.Integer, db.ForeignKey("accounts.id"), nullable=False) # account_id is an integer and the Foreign key comes from the accounts table id. It is required
    
    def __repr__(self):                                                              # Reresentitive state
        return f"<User {self.username}>"                                             # When the User is printed it now shows the username instead of the id