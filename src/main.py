from flask import Flask
import swagger
from flask_swagger_ui import get_swaggerui_blueprint

app = Flask(__name__)

SWAGGER_URL = '/swagger'
API_URL = '/static'

swaggerui_blueprint = get_swaggerui_blueprint(
    SWAGGER_URL, 
    API_URL, 
    config={
        'app_name': "Bruces-python-Flask-rest-biolerplate"
    }
)


app.register_blueprint(swaggerui_blueprint, url_prefix=SWAGGER_URL) 

@app.route("/")
def home_page():
    return "This is my homepage! Pretty cool."