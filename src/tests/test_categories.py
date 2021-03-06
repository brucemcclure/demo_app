import unittest                                                            # This is the inbuilt python testing module
from main import create_app, db                                            # This is the create_app function from the factory pattern and the DB from main
from models.Category import Category                                       
from models.User import User                                               # The User module to be used to log in to retrieve a JWT



class TestCategories(unittest.TestCase):                                  # This is the Parent class that will test our Profile functionality.    
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

    def test_category_index(self):
        response = self.client.get("/categories/")                          
        data = response.get_json()                                      
        self.assertEqual(response.status_code, 200)                    
        self.assertIsInstance(data, list)                

    def test_category_show(self):
        response = self.client.get("/categories/1")                          
        data = response.get_json()                                      
        self.assertEqual(response.status_code, 200)                    

    def test_category_create(self):
        response = self.client.post("/user/login",                      
        json = {              
            "email": "test1@test.com",
            "password": "123456"
        })                    
        data = response.get_json()                                      
        headers_data= {                                                 
            'Authorization': f"Bearer {data['token']}"
        }
        data = {
        "title": "mkkk", 
        "description": "l", 
        "private" : False
        }
        response = self.client.post("/categories/",                        
        json = data,                                                    
        headers = headers_data)  
        self.assertEqual(response.status_code, 200) 

    def test_category_update(self):
        response = self.client.post("/user/login",                      # Sending a post request to '/profile/'
        json = {                                                        # Data for login
            "email": "test1@test.com",
            "password": "123456"
        })  

        token = response.get_json()['token']

        response = self.client.post("/categories/",                         # Sending a get request to '/profile/1'
            headers = {                                                 # Building the dictionary for the auth header
            'Authorization': f"Bearer {token}"
            }, 
            json = {
                "title" : "This is a category being created to be updated", 
                "description" : "whoop whoop whoop",
                "private" : False 
            }
        ) 
        category_id = response.get_json()['id']

        response = self.client.patch(f"/categories/{category_id}",
        headers = {                                                 
            'Authorization': f"Bearer {token}"
            }, 
            json = {
                "title" : "This has been updated, yep yep yep", 
                "description" : "whoop whoop whoop", 
                "private" : False 
            })
        data = response.get_json()
        self.assertEqual(response.status_code, 200) 
        self.assertEqual(data['title'], 'This has been updated, yep yep yep') 


    def test_category_delete(self):
        response = self.client.post("/user/login",                      # Sending a post request to '/profile/'
        json = {                                                        # Data for login
            "email": "test5@test.com",
            "password": "123456"
        })  

        token = response.get_json()['token']

        response = self.client.post("/categories/",                         # Sending a get request to '/profile/1'
            headers = {                                                 # Building the dictionary for the auth header
            'Authorization': f"Bearer {token}"
            }, 
            json = {
                "title" : "This is a category being created to be deleted", 
                "description" : "whoop whoop whoop",
                "private" : False 
            }
        ) 
        category_id = response.get_json()['id']

        response = self.client.delete(f"/categories/{category_id}",
        headers = {                                                 
            'Authorization': f"Bearer {token}"
            })

        deleted_category = Category.query.get(category_id)
        self.assertIsNone(deleted_category)