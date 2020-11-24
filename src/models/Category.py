from main import db 
from models.Fine import Fine
from sqlalchemy.orm import backref     


class Category(db.Model):                                                 
    __tablename__= "categories"    

    id = db.Column(db.Integer, primary_key=True)  
    title = db.Column(db.String(), nullable=False, unique=True)  
    description = db.Column(db.String())  
    private = db.Column(db.Boolean(), nullable=False)
    owner = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)
    fine = db.relationship("Fine", backref=backref("category"))   

    def __repr__(self):                                                               # When printing the model we will see its email attribute
        return f"<Category {self.title}>"