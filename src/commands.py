from main import db                                             # This is the db instance created by SQLAlchemy
from flask import Blueprint                                     # Use blueprints instead of passing the app object around 

db_commands = Blueprint("db-custom", __name__)                  # Creating the blueprint

@db_commands.cli.command("drop")                                # this fronction will run when "flask db-custom drop" is run"
def drop_db():
    db.drop_all()                                               # Drop all tables  
    db.engine.execute("DROP TABLE IF EXISTS alembic_version;")  # Drop table for migrations
    print("Tables deleted")                                     # Print message to indicate tables are dropped



@db_commands.cli.command("seed")                                # this fronction will run when "flask db-custom seed" is run"
def seed_db():
    from models.Account import Account, account_leagues         # Importing the Account model
    from models.Profile import Profile                          # Importing the Profile model
    from models.League import League
    from main import bcrypt                                     # Hashing module for the passwords
    from faker import Faker                                     # Importing the faker module for fake data
    import random                                               # Importing random from the python standard library

    faker = Faker()
    accounts = []
    leagues = []

    for i in range(5):                                                             # Do this 5 times
        account = Account()                                                        # Create an account object from the Account model
        account.email = f"test{i+1}@test.com"                                      # Assign an email to the account object
        account.password = bcrypt.generate_password_hash("123456").decode("utf-8") # Assign ta hashed password to the account object
        db.session.add(account)                                                    # Add the account to the db session
        accounts.append(account)                                                   # Append the account to the accounts list

    db.session.commit()                                                            # Commit the seeion to the db 

    for i in range(5):
        profile = Profile()                                                        # Create a profile object from the Profile model                 

        profile.username = faker.first_name()                                      # Add a username to the profile object
        profile.firstname = faker.first_name()                                     # Add a firstname to the profile object
        profile.lastname = faker.last_name()                                       # Add a lastname to the profile object
        profile.account_id = accounts[i].id                                        # Add a account_id to the profile object. This comes from real ids from the accounts list

        db.session.add(profile)                                                    # Add the profile to the session

    db.session.commit()                                                            # Commit the session to the database

    for i in range(3):
        new_league = League()
        new_league.title = f"League title {i}"
        new_league.description = f"A nice league to the power of {i}"
        for i in range(3):
            new_league.account_leagues.append(accounts[i])
            leagues.append(new_league)
        db.session.commit() 

    for member in leagues[0].account_leagues:
        # print(f"League {i.title} => {i.account_id}") 
        print(member.email)
    print("Tables seeded")                                                         # Print a message to let the user know they 