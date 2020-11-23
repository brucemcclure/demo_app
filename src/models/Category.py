from main import db 

class Category(db.Model):                                                 
    __tablename__= "categories"    

    id = db.Column(db.Integer, primary_key=True)  
    title = db.Column(db.String(), nullable=False, unique=True)  
    description = db.Column(db.String(), nullable=False)  
    private = db.Column(db.Boolean(), nullable=False)
    owner = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)

    def __repr__(self):                                                               # When printing the model we will see its email attribute
        return f"<Category {self.title}>"