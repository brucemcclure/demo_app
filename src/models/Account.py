from main import db                                                                   # This is the db instance created by SQLAlchemy
from models.Profile import Profile
from models.League import League
from sqlalchemy.orm import backref                                                    # 

account_leagues = db.Table('account_leagues',
    db.Column('account_id', db.Integer, db.ForeignKey('accounts.id')),
    db.Column('league_id', db.Integer, db.ForeignKey('leagues.id'))
    )
class Account(db.Model):                                                              # Creating a Accounts class inheriting from db.Model
    __tablename__= "accounts"                                                         # Explicitly naming the table "accounts"

    id = db.Column(db.Integer, primary_key=True)                                      # There is an id column and it is the primary key
    email = db.Column(db.String(), nullable=False, unique=True)                       # Email column, string andit must be unique
    password = db.Column(db.String(), nullable=False)                                 # The password is a string and must be present
    profile = db.relationship("Profile", backref=backref("account", uselist=False))   # 
    account_leagues = db.relationship('League', secondary=account_leagues, backref=db.backref('account_leagues', lazy = 'dynamic'))

    def __repr__(self):                                                               
        return f"<Account {self.email}>"