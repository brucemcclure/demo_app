from main import ma                                                   
from models.Fine import Fine                                      
from marshmallow.validate import Length                               
from schemas.CategorySchema import CategorySchema


class FineSchema(ma.SQLAlchemyAutoSchema):                          
    class Meta:
        model = Fine                                                

    title = ma.String(required=True, validate=Length(min=1))          
    description = ma.String(required=True, validate=Length(min=1))    
    amount= ma.String(required=True)
    category = ma.Nested(CategorySchema)                                      # Nesting the user schema in the profile Schema

fine_schema = FineSchema()                                       
fines_schema = FineSchema(many=True)     