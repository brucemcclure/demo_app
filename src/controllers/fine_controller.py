from models.Fine import Fine                                           # Importing the League Model
from models.User import User                                           # Importing the User Model
from schemas.FineSchema import fine_schema, fines_schema               # Importing the Profile Schema
from main import db                                                    # This is the db instance created by SQLAlchemy
from main import bcrypt                                                # Import the hasing package from main
from services.auth_service import verify_user 
from sqlalchemy.orm import joinedload                                  # 
from flask_jwt_extended import jwt_required, get_jwt_identity          # Packages for authorization via JWTs
from flask import Blueprint, request, jsonify, abort                   # Import flask and various sub packages

fines = Blueprint("fines", __name__, url_prefix="/fines")         

# Full crud unneseasry 

@fines.route("/", methods=["GET"])                                   
def fine_index():                                                   
    fines = Fine.query.all()                                         
    return jsonify(fines_schema.dump(fines))                         



@fines.route("/<int:id>", methods=["GET"])                         
@jwt_required 
@verify_user    
def fine_show(user, id):                                                  
    fines = Fine.query.get(id)                                    
    return jsonify(fines_schema.dump(fines))    