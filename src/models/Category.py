from main import db 

class Category(db.Model):                                                 # Creating a League class inheriting from db.Model            
    __tablename__= "categories"    

    id = db.Column(db.Integer, primary_key=True)  
    title = db.Column(db.String(), nullable=False, unique=True)  
    description = db.Column(db.String(), nullable=False)  
    private = db.Column(db.Boolean(), nullable=False)
    owner = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)