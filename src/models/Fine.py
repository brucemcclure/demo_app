from main import db 
from models.Point import Point
from sqlalchemy.orm import backref     

class Fine(db.Model):                                                                 # Creating a Users class inheriting from db.Model
    __tablename__= "fines"    

    id = db.Column(db.Integer, primary_key=True)  
    title = db.Column(db.String(), nullable=False, unique=True)  
    description = db.Column(db.String(), nullable=False)  
    amount = db.Column(db.Integer(), nullable=False)
    style = db.Column(db.String(), nullable=False)
    category_id = db.Column(db.Integer, db.ForeignKey("categories.id"), nullable=False)
    point = db.relationship("Point", backref=backref("fine")) 

    def __repr__(self):                                                               # When printing the model we will see its email attribute
        return f"<Fine {self.title}>"