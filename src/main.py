from flask import Flask, jsonify                            # Import flask class and jsonify to send responses in JSON format
from marshmallow.exceptions import ValidationError          # Raises an error when validation fails on a field
from flask_sqlalchemy import  SQLAlchemy                    # This is the ORM
from flask_marshmallow import Marshmallow                   # Importing the Marshmallow class
from flask_bcrypt import Bcrypt                             # Hashing package
from flask_jwt_extended import JWTManager                   # Retrieves information form JWT
from flask_migrate import Migrate                           # Package to handle migrations

db = SQLAlchemy()                                           # New instance of SQLAlchemym named db
ma = Marshmallow()                                          # New instance of marshmallow named ma. This is for serialization
bcrypt = Bcrypt()                                           # New instance of Bcrypt, Hashing package
jwt = JWTManager()                                          # New instance of JWT Manager
migrate = Migrate()                                         # Makes new instance of migrate

def create_app():
    from dotenv import load_dotenv                          # Package to access environment variables
    load_dotenv()                                           # Retrieve the env variables from .env

    app = Flask(__name__)                                   # Creating an instnace of Flask named app
    app.config.from_object('default_settings.app_config')   # Loads the configuration for the app object from default_settings.py