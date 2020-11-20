from main import db                                                                   
from sqlalchemy.orm import backref                                                    

class League(db.Model):                                                             
    __tablename__= "leagues"                                                         

    id = db.Column(db.Integer, primary_key=True)                                     
    title = db.Column(db.String(), nullable=False, unique=True)                       
    description = db.Column(db.String(), nullable=False)                            

    def __repr__(self):                                                           
        return f"<Title {self.title}>"