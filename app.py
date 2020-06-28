from os import getenv
from dotenv import load_dotenv
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt

load_dotenv()

user = getenv('DB_USER_NAME')
pwd = getenv('DB_PASSWORD')
host = getenv('DB_HOST')
database = getenv('DATABASE')


app = Flask(__name__)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = f"mysql+pymysql://{user}:{pwd}@{host}/{database}"
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)


tags = db.Table('domains',
                db.Column('user_id', db.Integer, db.ForeignKey('users.id'), primary_key=True),
                db.Column('domains', db.Integer, db.ForeignKey('domain.id'), primary_key=True)
                )


class Users(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String)
    level = db.Column(db.Integer)
    domains = db.relationship('Domain', secondary=tags, lazy='subquery',
                              backref=db.backref('users', lazy=True))


class Domain(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    address = db.Column(db.String(100))


@app.route('/')
def hello():
    return "Hello, World!"


if __name__ == '__main__':
    app.run(debug=True)
