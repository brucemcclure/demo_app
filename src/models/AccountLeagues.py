# from flask_sqlalchemy import sqlalchemy
# from models.Account import Account
# from models.League import League
# from main import db

# class AccountLeagues(db.Model):                                                             
#     __tablename__= "account_leagues"                                                         

#     id = db.Column(db.Integer, primary_key=True)                                     
#     account_id = db.Column(db.String(), nullable=False)                       
#     league_id = db.Column(db.String(), nullable=False)                            

#     account = relationship(Account, backref=backref("account_leagues", cascade="all, delete-orphan"))
#     league = relationship(League, backref=backref("account_leagues", cascade="all, delete-orphan"))