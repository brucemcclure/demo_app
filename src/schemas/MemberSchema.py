from main import ma 
from marshmallow.validate import Length                              
from models.Member import Member                                      

class MemberSchema(ma.SQLAlchemyAutoSchema):                          
    class Meta:
        model = Member                                                

    user_id = ma.Integer(required=True, validate=Length(min=1))          
    league_id = ma.Integer(required=True, validate=Length(min=1))    
    
member_schema = MemberSchema()                                        
members_schema = MemberSchema(many=True)                              