from main import ma                                                   # Import the serialization object from main
from models.League import League                                      # Importign the League model
from marshmallow.validate import Length                               # Import the length class that will allow us to validate the length of the string 
from schemas.UserSchema import UserSchema                             # User schema               

class LeagueSchema(ma.SQLAlchemyAutoSchema):                          # Generates Schema automatically
    class Meta:
        model = League                                                # Generate Schema using the Profile Model

    title = ma.String(required=True, validate=Length(min=1))          # username is required and the minimum length is 1
    description = ma.String(required=True, validate=Length(min=1))    # first_name is required and the minimum length is 1

league_schema = LeagueSchema()                                        # Schema for a single league
leagues_schema = LeagueSchema(many=True)                              # Schema for multiple leagues    