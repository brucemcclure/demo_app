from main import ma                                                       # Import the serialization object from main
from models.AccountLeagues import AccountLeagues                          # Importign the Account model
from marshmallow.validate import Length                                   # Import the length class that will allow us to validate the length of the string 

class AccountSchema(ma.SQLAlchemyAutoSchema):                             # Generates Schema automatically
    class Meta:
        model = AccountLeagues                                                   # Generate Schema using the Account Model
   

    account_id = ma.String(required=True))              # The email is required and must be at least 6 chars long
    league_id = ma.String(required=True)           # 


account_schema = AccountSchema()                                          # Schema for single accounts
accounts_schema = AccountSchema(many=True)                                # Schema for multiple accounts    