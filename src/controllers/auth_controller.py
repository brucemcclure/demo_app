from models.Account import Account                                           # Importing the Account Model
from schemas.AccountSchema import account_schema                             # Importing the Account Schema
from main import db                                                          # This is the db instance created by SQLAlchemy
from main import bcrypt                                                      # Import the hasing package from main
from flask_jwt_extended import create_access_token                           # Package for providing JWTs
from datetime import timedelta                                               # Function to calculate the difference in time
from flask import Blueprint, request, jsonify, abort                         # Import flask and various sub packages

auth = Blueprint('auth', __name__, url_prefix="/auth")                       # Creating the auth blueprint, registered in __init__.py

@auth.route("/register", methods=["POST"])                                   # Register route
def auth_register():
    account_fields = account_schema.load(request.json)                       # Getting the fields from the Account Schema
    account = Account.query.filter_by(email=account_fields["email"]).first() # Query the account table with the email and return the first account
    
    if account:                                                              # If a account is returned 
        return abort(400, description="Email already in use")                # Return the error "Email already in use"

    account = Account()                                                      # Re-init account as a new instance of the Account model

    account.email = account_fields["email"]                                  # Add email to the account
    account.password = bcrypt.generate_password_hash(account_fields["password"]).decode("utf-8") # Hash the password and add it to the account

    db.session.add(account)                                                  # Add the account to rhe db session
    db.session.commit()                                                      # Commit the session

    return jsonify(account_schema.dump(account))                             # Return the account that was just created


@auth.route("/login", methods=["POST"])                                                             # Login route
def auth_login():
    account_fields = account_schema.load(request.json)                                              # Getting the fields from the Account Schema
    account = Account.query.filter_by(email=account_fields["email"]).first()                        # Query the account table with the email and return the first account

    if not account or not bcrypt.check_password_hash(account.password, account_fields["password"]): # If there is no account or the password is wrong
        return abort(401, description="Incorrect username or password")                             # Return the error "Incorrect username or password"

    expiry = timedelta(days=1)                                                                      # Time for the token to expire
    access_token = create_access_token(identity=str(account.id), expires_delta=expiry)              # The access token, with the account id and the expiration date

    return jsonify({ "token": access_token })                                                       # Return the token