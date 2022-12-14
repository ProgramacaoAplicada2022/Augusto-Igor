from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_uploads import configure_uploads, IMAGES, UploadSet

app = Flask(__name__)


app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///bughunter.db'
app.config['SECRET_KEY'] = '777439glc6c896ae2029594d'
app.config['UPLOADED_IMAGES_DEST'] = 'bughunter/static'
images = UploadSet('images', IMAGES)
configure_uploads(app, images)

db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login_page'
login_manager.login_message_category = "info"
from bughunter import routes