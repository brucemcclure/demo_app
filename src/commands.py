from main import db                                             # This is the db instance created by SQLAlchemy
from flask import Blueprint                                     # Use blueprints instead of passing the app object around 

db_commands = Blueprint("db-custom", __name__)                  # Creating the blueprint

@db_commands.cli.command("drop")                                # this fronction will run when "flask db-custom drop" is run"
def drop_db():
    db.drop_all()                                               # Drop all tables  
    db.engine.execute("DROP TABLE IF EXISTS alembic_version;")  # Drop table for migrations
    print("Tables deleted")                                     # Print message to indicate tables are dropped

faker = Faker()
accounts = []

@db_commands.cli.command("seed")                                # this fronction will run when "flask db-custom seed" is run"
def seed_db():
    from models.Account import Account                          # Importing the Account model
    from models.Profile import Profile                          # Importing the Profile model
    from main import bcrypt                                     # Hashing module for the passwords
    from faker import Faker                                     # Importing the faker module for fake data
    import random                                               # Importing random from the python standard library

    for i in range(5):                                                             # Do this 5 times
        account = Account()                                                        # Create an account object from the Account model
        account.email = f"test{i}@test.com"                                        # Assign an email to the account object
        user.password = bcrypt.generate_password_hash("123456").decode("utf-8")    # Assign ta hashed password to the account object
        db.session.add(account)                                                    # Add the account to the db session
        accounts.append(account)                                                   # Append the account to the accounts list

    db.session.commit()


