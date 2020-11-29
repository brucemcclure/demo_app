from main import db 
from sqlalchemy.orm import backref     

class Member(db.Model):
    __tablename__="members"

    id = db.Column(db.Integer, primary_key=True)  
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)
    league_id = db.Column(db.Integer, db.ForeignKey("leagues.id"), nullable=False)
    active = db.Column(db.Boolean(), nullable=False)
    # giver = db.relationship("Point", backref=backref("point")) 
    # receiver = db.relationship("Point", backref=backref("point")) 
    def __repr__(self):                                                               # When printing the model we will see its email attribute
        return f"<Member {self.id}>"