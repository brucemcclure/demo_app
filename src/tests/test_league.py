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