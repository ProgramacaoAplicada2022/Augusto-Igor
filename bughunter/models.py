from bughunter import db, login_manager
from bughunter import bcrypt
from flask_login import UserMixin

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class User(db.Model, UserMixin):
    id = db.Column(db.Integer(), primary_key=True)
    username = db.Column(db.String(length=30), nullable=False, unique=True)
    email_address = db.Column(db.String(length=50), nullable=False, unique=True)
    password_hash = db.Column(db.String(length=60), nullable=False)
    projects = db.relationship('Project', backref='owned_user', lazy=True)

    @property
    def password(self):
        return self.password

    @password.setter
    def password(self, plain_text_password):
         self.password_hash = bcrypt.generate_password_hash(plain_text_password).decode('utf-8')

    def check_password_correction(self, attempted_password):
        return bcrypt.check_password_hash(self.password_hash, attempted_password)

class Project(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(length=30), nullable=False, unique=True)
    image = db.Column(db.String(length=1024)) # url da imagem
    creation_date = db.Column(db.String(length=10), nullable=False)
    description = db.Column(db.String(length=1024), nullable=False, unique=True)
    owner = db.Column(db.Integer(), db.ForeignKey('user.id'))
    domain = db.relationship('Domain', backref='project_originated', lazy=True)
    
    def __repr__(self):
        return f'Project {self.name}'


class Domain(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(length=200), nullable=False, unique=True)
    description = db.Column(db.String(length=2048), default="")
    services = db.Column(db.Integer(), nullable=False, default=3)
    status = db.Column(db.Integer(), nullable=False, default=2)
    project = db.Column(db.Integer(), db.ForeignKey('project.id'))

    def __repr__(self):
        return f'{self.name}'

