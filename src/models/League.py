from main import db     
from models.Category import Category
from models.Sprint import Sprint
from sqlalchemy.orm import backref, relationship
from models.Member import Member


leagues_categories = db.Table( "leagues_categories",
    db.Column('league_id', db.Integer, db.ForeignKey('leagues.id')),
    db.Column('category_id', db.Integer, db.ForeignKey('categories.id'))

)

class League(db.Model):                                                 
    __tablename__= "leagues"                                                   

    id = db.Column(db.Integer, primary_key=True)                                
    title = db.Column(db.String(), nullable=False, unique=True)                   
    description = db.Column(db.String(), nullable=False)                          
    owner = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)      
    leagues_categories = db.relationship('Category', secondary=leagues_categories, backref=db.backref('leagues_categories', lazy = 'dynamic'))
    sprints = db.relationship("Sprint", cascade="all, delete",backref=backref("league")) 
    members = relationship(
        "User", 
        secondary="members"
    )

    def __repr__(self):                                                 
        return f"<Title {self.title}>"                                 