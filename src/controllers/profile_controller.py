from models.Account import Account                                     # Importing the Account Model
from schemas.AccountSchema import account_schema                       # Importing the Account Schema
from main import db                                                    # This is the db instance created by SQLAlchemy
from main import bcrypt                                                # Import the hasing package from main
from flask_jwt_extended import create_access_token                     # Package for providing JWTs
from datetime import timedelta                                         # Function to calculate the difference in time
from flask import Blueprint, request, jsonify, abort                   # Import flask and various sub packages

