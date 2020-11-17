from main import ma                                             # Import the serialization object from main
from models.User import User                                    # Importign the User model
from marshmallow.validate import Length                             # Import the length class that will allow us to validate the length of the string 

class UserSchema(ma.SQLAlchemyAutoSchema):                          # Generates Schema automatically
    class Meta:
        model = User                                                # Generate Schema using the User Model

    email = ma.String(required=True, validate=Length(min=4))        # The email is required and must be at least 6 chars long
    password = ma.String(required=True, validate=Length(min=6))     # This must be moved 


user_schema = UserSchema()                                          # Schema for single users
users_schema = UserSchema(many=True)                                # Schema for multiple users    