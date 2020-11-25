from main import ma                                                   
from models.Fine import Fine                                      
from marshmallow.validate import Length                               
from schemas.PointSchema import PointSchema

class PointSchema(ma.SQLAlchemyAutoSchema):                          
    class Meta:
        model = Fine                                                

    creation_time = ma.DateTime(required=True) 

point_schema = PointSchema()                                       
points_schema = PointSchema(many=True)     