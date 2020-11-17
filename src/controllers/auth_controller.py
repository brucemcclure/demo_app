from models.User import User                                           # Importing the User Model
from schemas.UserSchema import user_schema                             # Importing the USer Schema
from main import db                                                    # This is the db instance created by SQLAlchemy
from main import bcrypt                                                # Import the hasing package from main
from flask_jwt_extended import create_access_token                     # Package for providing JWTs
from datetime import timedelta                                         # Function to calculate the difference in time
from flask import Blueprint, request, jsonify, abort                   # Import flask and various sub packages

auth = Blueprint('auth', __name__, url_prefix="/auth")                 # Creating the auth blueprint, registered in __init__.py

@auth.route("/register", methods=["POST"])                             # Register route
def auth_register():
    user_fields = user_schema.load(request.json)                       # Getting the fields from the User Schema
    user = User.query.filter_by(email=user_fields["email"]).first()    # Query the user table with the email and return the first user
    
    if user:                                                           # If a user is returned 
        return abort(400, description="Email already in use")          # Return the error "Email already in use"

    user = User()                                                      # Re-init user as a new instance of the User model

    user.username = user_fields["username"]                            # Add username to the user
    user.firstname = user_fields["firstname"]                          # Add firstname to the user
    user.lastname = user_fields["lastname"]                            # Add lastname to the user
    user.email = user_fields["email"]                                  # Add email to the user

    user.password = bcrypt.generate_password_hash(user_fields["password"]).decode("utf-8") # Hash the password and add it to the user

    db.session.add(user)                                               # Add the user to rhe db session
    db.session.commit()                                                # Commit the session

    return jsonify(user_schema.dump(user))                             # Return the user that was just created