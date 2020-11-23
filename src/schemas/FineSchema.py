from main import ma                                                   
from models.Fine import Fine                                      
from marshmallow.validate import Length                               
from schemas.UserSchema import UserSchema


class FineSchema(ma.SQLAlchemyAutoSchema):                          
    class Meta:
        model = Fine                                                

    title = ma.String(required=True, validate=Length(min=1))          
    description = ma.String(required=True, validate=Length(min=1))    
    amount= ma.String(required=True, validate=)

fine_schema = FineSchema()                                       
fines_schema = FineSchema(many=True)     