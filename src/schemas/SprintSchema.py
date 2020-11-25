from main import ma                                                   
from models.Sprint import Sprint
from schemas.LeagueSchema import LeagueSchema                                      
from marshmallow.validate import Length                               
from schemas.UserSchema import UserSchema       


class SprintSchema(ma.SQLAlchemyAutoSchema):                          
    class Meta:
        model = Sprint                                               

    title = ma.String(required=True, validate=Length(min=1))          
    meeting_point = ma.String(required=True, validate=Length(min=1))    
    creation_time = ma.DateTime(required=True)  
    # league = ma.Nested(LeagueSchema)   
    
sprint_schema = SprintSchema()                                        
sprints_schema = SprintSchema(many=True)                              