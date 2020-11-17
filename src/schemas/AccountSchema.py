from main import ma                                                       # Import the serialization object from main
from models.Account import Account                                        # Importign the Account model
from marshmallow.validate import Length                                   # Import the length class that will allow us to validate the length of the string 

class AccountSchema(ma.SQLAlchemyAutoSchema):                             # Generates Schema automatically
    class Meta:
        model = Account                                                   # Generate Schema using the Account Model

    email = ma.String(required=True, validate=Length(min=4))              # The email is required and must be at least 6 chars long
    password = ma.String(required=True, validate=Length(min=6))           # This must be moved 


account_schema = AccountSchema()                                          # Schema for single accounts
accounts_schema = AccountSchema(many=True)                                # Schema for multiple accounts    