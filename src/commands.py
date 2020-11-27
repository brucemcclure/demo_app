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
    from datetime import date
    from models.User import User                          # Importing the User model
    from models.Profile import Profile                          # Importing the Profile model
    from models.League import League
    from models.Member import Member
    from models.Fine import  Fine
    from models.Point import Point
    from models.Category import Category
    from models.Sprint import Sprint
    from main import bcrypt                                     # Hashing module for the passwords
    from faker import Faker                                     # Importing the faker module for fake data
    import random                                               # Importing random from the python standard library
    import copy

    faker = Faker()
    users = []
    leagues = []
    categories = []
    sprints = []
    points = []
    fines = []

    for i in range(5):                                                           # Do this 5 times
        user = User()                                                           # Create an user object from the User model
        user.email = f"test{i+1}@test.com"                                      # Assign an email to the user object
        user.password = bcrypt.generate_password_hash("123456").decode("utf-8") # Assign ta hashed password to the user object
        db.session.add(user)                                                    # Add the user to the db session
        users.append(user)                                                      # Append the user to the users list

    db.session.commit()                                                         # Commit the seeion to the db 

    for i in range(5):
        profile = Profile()                                                     # Create a profile object from the Profile model                 

        profile.username = faker.first_name()                                   # Add a username to the profile object
        profile.firstname = faker.first_name()                                  # Add a firstname to the profile object
        profile.lastname = faker.last_name()                                    # Add a lastname to the profile object
        profile.user_id = users[i].id                                           # Add a user_id to the profile object. This comes from real ids from the users list

        db.session.add(profile)                                                 # Add the profile to the session

    db.session.commit()                                                         # Commit the session to the database

    for i in range(5):
        new_league = League()
        new_league.title = f"League title {i}"
        new_league.description = f"A nice league to the power of {i}"
        new_league.owner = users[i].id
        leagues.append(new_league)
        db.session.add(new_league) 
    db.session.commit() 

    # for i in range(5):
    #     copy_users = copy.deepcopy(users)                           # Make a copy of users each time  
    #     league = leagues[i]                                         # For each league

    #     for i in range(3):
    #         new_member = Member()                                   # Create a new member
    #         random_user = random.choice(copy_users)                 # choose a random user
    #         copy_users.remove(random_user)                   # Remove it from the list
    #         new_member.user_id = random_user.id
    #         new_member.league_id = league.id
    #         db.session.add(new_member)
    #         db.session.commit() 
    #         print("******")

    for i in range(5):
        owner = Member()
        owner.user_id = leagues[i].owner
        owner.league_id = i+1
        db.session.add(owner)

        new_member = Member()
        new_member.league_id = i+1
        new_member.user_id = random.choice(users).id
        while new_member.user_id == i:
            new_member.user_id = random.choice(users).id
        db.session.add(new_member)
    db.session.commit() 


    for i in range(5):
        new_sprint = Sprint()
        new_sprint.title = f"Sprint title #{i}"
        new_sprint.meeting_point = f"The Outback"
        new_sprint.creation_time = date.today()
        league = League.query.get(i)
        new_sprint.league = league
        sprints.append(new_sprint)
    db.session.commit() 

    
    for i in range(5):
        new_category = Category()
        new_category.title = f"category title {i}"
        new_category.description = f"category description {i}"
        if i % 2 == 0:
            private = True
        else:
            private = False
        new_category.private = private
        new_category.owner = random.choice(users).id
        new_category.leagues_categories.append(leagues[1])
        
        categories.append(new_category)
        db.session.commit() 

    for i in range(5):
        new_fine = Fine()
        new_fine.title = f"Title {i}"
        new_fine.description = f"Description {i}"
        new_fine.amount = i
        if i % 2 == 0:
            style = "Award"
        else:
            style = "Fine"
        new_fine.style = style
        category = Category.query.get(i)
        new_fine.category = category
        fines.append(new_fine)
        db.session.commit() 

    for i in range(5):
        new_point = Point()
        new_point.creation_time = date.today()
        new_point.fine_id = random.choice(fines).id
        sprint = Sprint.query.get(i)
        new_point.sprint = sprint
        db.session.commit() 

    print("Tables seeded")