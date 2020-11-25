from main import db 
from sqlalchemy.orm import backref     

class Sprint(db.Model):                                                                 # Creating a Users class inheriting from db.Model
    __tablename__= "sprints"    

    id = db.Column(db.Integer, primary_key=True)  
    meeting_point = db.Column(db.String(), nullable=False)
    creation_time = db.Column(db.DateTime, nullable=False)
    league_id = db.Column(db.Integer, db.ForeignKey("leagues.id"), nullable=False)

    def __repr__(self):                                                               # When printing the model we will see its email attribute
        return f"<Fine {self.creation_time}>"