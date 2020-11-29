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
    import time

    faker = Faker()
    users = []
    leagues = []
    categories = []
    sprints = []
    points = []
    fines = []

    for i in range(5):     
        time.sleep(0.2)                                                       
        user = User()                                                          
        user.email = f"test{i+1}@test.com"                                      
        user.password = bcrypt.generate_password_hash("123456").decode("utf-8")
        db.session.add(user)                                                    
        users.append(user)                                                      

    db.session.commit()                                                        

    for i in range(5):
        # time.sleep(0.2)  
        profile = Profile()                                                                    

        profile.username = f"username{i}"                                
        profile.firstname = f"firstname{i}"                                     
        profile.lastname = f"lastname{i}"                                     
        profile.user_id = users[i].id                                           

        db.session.add(profile)                                                 

    db.session.commit()                                                         

    for i in range(5):
        # time.sleep(0.2)  
        new_league = League()
        new_league.title = f"League title {i}"
        new_league.description = f"A nice league to the power of {i}"
        new_league.owner = users[i].id
        leagues.append(new_league)
        db.session.add(new_league) 
    db.session.commit() 


    for i in range(5):
        # time.sleep(0.2)  
        owner = Member()
        owner.user_id = leagues[i].owner
        owner.league_id = i+1
        owner.active = True
        db.session.add(owner)

        new_member = Member()
        new_member.active = True
        new_member.league_id = i+1
        new_member.user_id = random.choice(users).id
        while new_member.user_id == owner.user_id:
            new_member.user_id = random.choice(users).id
        db.session.add(new_member)
    db.session.commit() 

    for i in range(5):
        new_sprint = Sprint()
        new_sprint.title = f"Sprint title #{i}"
        new_sprint.meeting_point = f"The Outback"
        new_sprint.creation_time = date.today()
        league = leagues[i]
        new_sprint.league = league
        sprints.append(new_sprint)
    db.session.commit() 

    for i in range(5):
        # time.sleep(0.2)  
        new_category = Category()
        new_category.title = f"category title {i}"
        new_category.description = f"category description {i}"
        if i % 2 == 0:
            private = True
        else:
            private = False
        new_category.private = private
        new_category.owner = random.choice(users).id
        new_category.leagues_categories.append(leagues[i])
        
        categories.append(new_category)
        db.session.commit() 
    	
    
    for i in range(5):
        # time.sleep(0.2)  
        new_fine = Fine()
        new_fine.title = f"Title {i}"
        new_fine.description = f"Description {i}"
        new_fine.amount = i
        if i % 2 == 0:
            style = "Award"
        else:
            style = "Fine"
        new_fine.style = style
        category = categories[i]
        new_fine.category = category
        fines.append(new_fine)
        db.session.commit() 

    for i in range(4):
        # time.sleep(0.2)  
        new_point = Point()
        new_point.creation_time = date.today()
        new_point.fine_id = random.choice(fines).id
        sprint = sprints[i]
        new_point.sprint = sprint
        new_point.giver_id = sprint.league.owner
        new_point.receiver_id = sprint.league.members[1].id
        db.session.commit() 

    print("Tables seeded")