from main import ma                                                   
from models.Fine import Fine                                      
from marshmallow.validate import Length                               
from schemas.PointSchema import PointSchema

class PointSchema(ma.SQLAlchemyAutoSchema):                          
    class Meta:
        model = Fine                                                

    title = ma.String(required=True, validate=Length(min=1))          
    description = ma.String(required=True, validate=Length(min=1))    
    amount= ma.String(required=True)

point_schema = PointSchema()                                       
points_schema = PointSchema(many=True)     