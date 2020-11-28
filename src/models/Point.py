from main import db 
from sqlalchemy.orm import backref     

class Point(db.Model):
    __tablename__="points"

    id = db.Column(db.Integer, primary_key=True)  
    creation_time = db.Column(db.DateTime, nullable=False)
    sprint_id = db.Column(db.Integer, db.ForeignKey("sprints.id"), nullable=False)
    fine_id = db.Column(db.Integer, db.ForeignKey("fines.id"), nullable=False)

    giver_id = db.Column(db.Integer, db.ForeignKey("members.id"))
    receiver_id = db.Column(db.Integer, db.ForeignKey("members.id"))

    giver = db.relationship("Member", foreign_keys=[giver_id]) 
    receiver = db.relationship("Member", foreign_keys=[receiver_id]) 

    def __repr__(self):                                                               
        return f"<Point {self.id}>"