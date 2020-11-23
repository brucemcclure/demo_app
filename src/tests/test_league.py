import unittest                                                            # This is the inbuilt python testing module
from main import create_app, db                                            # This is the create_app function from the factory pattern and the DB from main
from models.League import League                                           # The League module that is used to communicate data with the DB
from models.User import User                                               # The User module to be used to log in to retrieve a JWT

# NB The tests must run in isolation because we cant guarentee which tests run in which order.



class TestProfiles(unittest.TestCase):                                  # This is the Parent class that will test our Profile functionality.    
    @classmethod
    def setUp(cls):                                                     # This method will run before each and every class
        cls.app = create_app()                                          # Create a new instance of app
        cls.app_context = cls.app.app_context()                         # Creating context for which the app is in. The tests run in parrallel therefore we need to keep track of which instance of app we are using
        cls.app_context.push()                                          # Pushing context. Read the docs for more
        cls.client = cls.app.test_client()                              # Adding the test client to the client
        db.create_all()                                                 # Create all the 
        runner = cls.app.test_cli_runner()
        runner.invoke(args=["db-custom", "seed"])                       # This seeds the db

    @classmethod                                                        # This method will run after each and every class
    def tearDown(cls):                                                  # We want to delete all the data from the class tests
        db.session.remove()                                             # Remove the session from the db
        db.drop_all()                                                   # Drop all tables
        cls.app_context.pop()                                           # Remove the context of the app

    def test_league_index(self):
        response = self.client.get("/league/")                          # make a get request to the app the "/league/" url, save it to a response object
        data = response.get_json()                                      # jsonify the data
        self.assertEqual(response.status_code, 200)                     # Checking if the response code is 200 you can make it a range 200-299 too
        self.assertIsInstance(data, list)                               # Checking the data type of the response codedoc 

    def test_profile_show(self):
        response = self.client.post("/user/login",                      # Sending a post request to '/profile/'
        json = {                                                        # Data for login
            "email": "test5@test.com",
            "password": "123456"
        })                    

        data = response.get_json()                                      # converting the response to data

        response = self.client.get("/league/1",                         # Sending a get request to '/profile/1'
            headers = {                                                 # Building the dictionary for the auth header
            'Authorization': f"Bearer {data['token']}"
        }
        ) 
        data = response.get_json()                                      # Converting the response to json  
        self.assertEqual(response.status_code, 200)                     # Checking the status code is 200
        self.assertIsNotNone(data)     


    # def test_league_create(self):
    #     response = self.client.post("/user/login",                      # Logging in with the new user credentials
    #     json = {              
    #         "email": "test1@test.com",
    #         "password": "123456"
    #     })                    
    #     data = response.get_json()                                      # Turning the response to JSON
    #     headers_data= {                                                 # Creating the dictionary to be sent as an auth header 
    #         'Authorization': f"Bearer {data['token']}"
    #     }
    #     data = {                                                        # Creating a dictionary holding the data for the new profile
    #         "title" : "This is the new league which was created", 
    #         "description" : "description, hoomst hoomst", 
    #         "lastname" : "test"
    #     }
    #     response = self.client.post("/leage/",                        # Sending a post request to '/profile/'
    #     json = data,                                                    # Sending the data for the new  
    #     headers = headers_data)                                         # Auth header
    #     self.assertEqual(response.status_code, 200)                     # Checking if the response is 200
    #     # data = response.get_json()                                      # Converting the response to data
    #     # profile = Profile.query.get(data["user"]["id"])                 # Querying the db for the profile
    #     # self.assertIsNotNone(profile)                                   # Checking the profile exists
    #     # self.assertEqual(profile.username, "bruce")   