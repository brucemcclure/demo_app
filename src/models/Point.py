from main import db 
from sqlalchemy.orm import backref     

class Point(db.Model):
    __tablename__="points"

    id = db.Column(db.Integer, primary_key=True)  
    sprint_id = db.Column(db.Integer, db.ForeignKey("sprints.id"), nullable=False)