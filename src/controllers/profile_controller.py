from models.Profile import Profile                                     # Importing the Profile Model
from models.Account import Account                                     # Importing the Account Model
from schemas.ProfileSchema import profile_schema, profiles_schema      # Importing the Profile Schema
from main import db                                                    # This is the db instance created by SQLAlchemy
from main import bcrypt                                                # Import the hasing package from main
from services.auth_service import verify_account 
from sqlalchemy.orm import joinedload                                  # 
from flask_jwt_extended import jwt_required, get_jwt_identity          # Packages for authorization via JWTs
from flask import Blueprint, request, jsonify, abort                   # Import flask and various sub packages

profiles = Blueprint("profiles", __name__, url_prefix="/profile")      # Creating the profile blueprint 

@profiles.route("/", methods=["GET"])                                  # Route for the profile index
def profile_index():                                                   # This function will run when the route is matched
    profiles = Profile.query.options(joinedload("account")).all()      # Retrieving all profiles from the db
    return jsonify(profiles_schema.dump(profiles))                     # Returning all the profiles in json

@profiles.route("/", methods=["POST"])                                 # Route for the profile create
@jwt_required                                                          # JWT token is required for this route
@verify_account                                                        # Auth service to make sure the correct account owns this profile
def profile_create(account):                                           # This function will run when the route is matched

    if account.profile != []:                                          # If the account already has a profile
        return abort(400, description="User already has profile")      # Return the error "Email already in use"

    profile_fields = profile_schema.load(request.json)                 # Retrieving the fields from the request
    profile = Profile.query.filter_by(username=profile_fields["username"]).first() # Query the account table with the email and return the first account

    if profile:                                                        # If a account is returned 
        return abort(400, description="username already in use")       # Return the error "Email already in use"

    new_profile = Profile()                                            # Create a new profile object from the Profile model 
    new_profile.username = profile_fields["username"]                  # Add username to the new_profile 
    new_profile.firstname = profile_fields["firstname"]                # Add username to the new_profile 
    new_profile.lastname = profile_fields["lastname"]                  # Add username to the new_profile 
    new_profile.account_id = account.id                                # Add username to the new_profile 
    account.profile.append(new_profile)                                # Add profile to the account
    db.session.commit()                                                # Commit the DB session
      
    return jsonify(profile_schema.dump(new_profile))                   # Return the newly created profile

@profiles.route("/<int:id>", methods=["GET"])                          # Route for the profile create
def profile_show(id):                                                  # Auth service to make sure the correct account owns this profile
    profile = Profile.query.get(id)                                    # Query the account table with the id then return that account
    return jsonify(profile_schema.dump(profile))                       # Returb the profile in JSON
    

@profiles.route("/<int:id>", methods=["PUT", "PATCH"])                 # Route for the profile create
@jwt_required                                                          # JWT token is required for this route
@verify_account                                                        # Auth service to make sure the correct account owns this profile
def profile_update(account, id):                             
    
    profile_fields = profile_schema.load(request.json)                 # Retrieving the fields from the request
    profile = Profile.query.filter_by(id=id, account_id=account.id)     # Query the account table with the id and the account id then return the first account

    if profile.count() !=1:                                            # If there is any number other than 1
        return abort(401, description="Unauthorized to update this profile")  # Return this error

    profile.update(profile_fields)                                     # Update the fields with the data from the request
    db.session.commit()                                                # Commit the session to the db
    return jsonify(profile_schema.dump(profile[0]))                    # Return the recently committed profile


@profiles.route("/<int:id>", methods=["DELETE"])                       # Route for the profile create
@jwt_required        
@verify_account                                                        # Auth service to make sure the correct account owns this profile
def profile_delete(account, id):
    profile = Profile.query.filter_by(id=id, account_id=account.id)     # Query the account table with the id and the account id then return the first account
    # print(profile[0].__dict__)
    # return("bills")
    if not profile:                                                    # If there is any number other than 1
        return abort(400, description="Unauthorized to update this profile") # Return this error
    
    db.session.delete(profile[0])
    db.session.commit()                                                # Commit the session to the db
    return jsonify(profile_schema.dump(profile))                       # Return the deleted profile
