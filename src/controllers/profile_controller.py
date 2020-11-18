from models.Profile import Profile                                     # Importing the Profile Model
from models.Account import Account                                     # Importing the Account Model
from schemas.ProfileSchema import profile_schema, profiles_schema      # Importing the Profile Schema
from main import db                                                    # This is the db instance created by SQLAlchemy
from main import bcrypt                                                # Import the hasing package from main
from sqlalchemy.orm import joinedload                                  # 
from flask_jwt_extended import jwt_required, get_jwt_identity          # Packages for authorization via JWTs
from flask import Blueprint, request, jsonify, abort                   # Import flask and various sub packages

profiles = Blueprint("profiles", __name__, url_prefix="/profile")      # Creating the profile blueprint 

@profiles.route("/", methods=["GET"])                                  # Route for the profile index
def profile_index():                                                   # This function will run when the route is matched
    profiles = Profile.query.options(joinedload("account")).all()      # Retrieving all profiles from the db
    return jsonify(profiles_schema.dump(profiles))                     # Returning the profiles in json