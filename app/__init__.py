from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
from flask_admin import Admin
from app.dbDefault import init_db

app = Flask(__name__)
app.config.from_object(Config)
app.static_folder = 'static'
db = SQLAlchemy(app)
init_db(db)
migrate = Migrate(app, db)
login = LoginManager(app)
login.login_view = "login"
admin = Admin(app)

from app import routes, models

if __name__ == '__main__':
	app.run() # for debug mode, Modify to app.run(debug=True).
	