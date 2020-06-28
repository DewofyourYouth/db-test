from os import getenv
from dotenv import load_dotenv
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

load_dotenv()

app = Flask(__name__)
user = getenv('DB_USER_NAME')
pwd = getenv('DB_PASSWORD')
host = getenv('DB_HOST')
database = getenv('DATABASE')


app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = f"mysql+pymysql://{user}:{pwd}@{host}/{database}"
db = SQLAlchemy(app)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String)


@app.route('/')
def hello():
    return "Hello, World!"


if __name__ == '__main__':
    app.run(debug=True)
