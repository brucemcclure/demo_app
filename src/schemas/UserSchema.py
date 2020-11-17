from main import ma                                                   # Import the serialization object from main
from models.User import User                                          # Importign the User model
from marshmallow.validate import Length                               # Import the length class that will allow us to validate the length of the string 
from schemas.AccountSchema import AccountSchema                       # Account schema               
class UserSchema(ma.SQLAlchemyAutoSchema):                            # Generates Schema automatically
    class Meta:
        model = User                                                  # Generate Schema using the User Model

    username = ma.String(required=True, validate=Length(min=1))       # username is required and the minimum length is 1
    first_name = ma.String(required=True, validate=Length(min=1))     # first_name is required and the minimum length is 1
    last_name = ma.String(required=True, validate=Length(min=1))      # last_name is required and the minimum length is 1
    account = ma.Nested(AccountSchema)                                # Nesting the account schema in the User Schema

user_schema = UserSchema()                                            # Schema for single users
users_schema = UserSchema(many=True)                                  # Schema for multiple users    