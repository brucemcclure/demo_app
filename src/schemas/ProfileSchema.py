from main import ma                                                   # Import the serialization object from main
from models.Profile import Profile                                    # Importign the Profile model
from marshmallow.validate import Length                               # Import the length class that will allow us to validate the length of the string 
from schemas.AccountSchema import AccountSchema                       # Account schema               

class ProfileSchema(ma.SQLAlchemyAutoSchema):                         # Generates Schema automatically
    class Meta:
        model = Profile                                               # Generate Schema using the Profile Model

    username = ma.String(required=True, validate=Length(min=1))       # username is required and the minimum length is 1
    first_name = ma.String(required=True, validate=Length(min=1))     # first_name is required and the minimum length is 1
    last_name = ma.String(required=True, validate=Length(min=1))      # last_name is required and the minimum length is 1
    account = ma.Nested(AccountSchema)                                # Nesting the account schema in the profile Schema

profile_schema = ProfileSchema()                                      # Schema for a single profile
profiles_schema = ProfileSchema(many=True)                            # Schema for multiple profiles    