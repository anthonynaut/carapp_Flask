from flask import Flask
from .api.routes import api
from .site.routes import site
from .authentication.routes import auth
from config import Config

app = Flask(__name__)
FLASK_APP= os.dotenv('FLASK_APP')
FLASK_ENV= os.dotenv('FLASK_ENV')
app.register_blueprint(api)
app.register_blueprint(site)
app.register_blueprint(auth)

app.config.from_object(Config)
