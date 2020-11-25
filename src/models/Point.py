from main import db 
from sqlalchemy.orm import backref     

class Point(db.Model):
    __tablename__="points"

    id = db.Column(db.Integer, primary_key=True)  
    creation_time = db.Column(db.DateTime, nullable=False)
    sprint_id = db.Column(db.Integer, db.ForeignKey("sprints.id"), nullable=False)
    fine_id = db.Column(db.Integer, db.ForeignKey("fines.id"), nullable=False)

    def __repr__(self):                                                               # When printing the model we will see its email attribute
        return f"<Point {self.id}>"