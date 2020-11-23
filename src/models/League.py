from main import db                                                    # This is the db instance created by SQLAlchemy                                                                   

class League(db.Model):                                                 # Creating a League class inheriting from db.Model            
    __tablename__= "leagues"                                            # Explicitally providing the name of the table             

    id = db.Column(db.Integer, primary_key=True)                        # Creates a column called id and sets it al the primary key             
    title = db.Column(db.String(), nullable=False, unique=True)         # Title, string, must be present, must be unique              
    description = db.Column(db.String(), nullable=False)                # Description, string, must be present, must be unique            
    owner = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)       # user_id is an integer and the Foreign key comes from the users table id. It is required

    def __repr__(self):                                                 # Reresentitive state          
        return f"<Title {self.title}>"                                  # When the League is printed it now shows the title instead of the id