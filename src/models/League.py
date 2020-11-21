from main import db                                                    # This is the db instance created by SQLAlchemy                                                                   

class League(db.Model):                                                 # Creating a League class inheriting from db.Model            
    __tablename__= "leagues"                                            # Explicitally providing the name of the table             

    id = db.Column(db.Integer, primary_key=True)                                     
    title = db.Column(db.String(), nullable=False, unique=True)                       
    description = db.Column(db.String(), nullable=False)                            

    def __repr__(self):                                                           
        return f"<Title {self.title}>"