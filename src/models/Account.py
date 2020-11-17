from main import db                                                              # This is the db instance created by SQLAlchemy
from sqlalchemy.orm import backref                                               # 

class Accounts(db.model):                                                        # Creating a Accounts class inheriting from db.Model
    __tablename__= "accounts"                                                    # Explicitly naming the table "accounts"

    id = db.Column(db.Integer, primary_key=True)                                 # There is an id column and it is the primary key
    email = db.Column(db.String(), nullable=False, unique=True)                  # Email column, string andit must be unique
    password = db.Column(db.String(), nullable=False)                            # The password is a string and must be present
    user_id = db.relationship("User", backref=backref("accounts", uselist=False)) # 

    def __repr__(self):                                                          #
        return f"<Account {self.email}>"