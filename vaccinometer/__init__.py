import flask
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine

app = Flask(__name__, static_folder="build", static_url_path='/')

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///UsersDataBase.db'
app.config['SQLALCHEMY_BINDS'] = {'vac': 'sqlite:///VaccineDataBase.db'}
# app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://eorqpgbgzacvss:4964c9324320f39370bbae234d3be1a4fe2e5b184da15e6e33e2f05e4275e033@ec2-54-165-178-178.compute-1.amazonaws.com:5432/dec71qhll81qvg'
# app.config['SQLALCHEMY_BINDS'] = {'vac': 'postgres://eorqpgbgzacvss:4964c9324320f39370bbae234d3be1a4fe2e5b184da15e6e33e2f05e4275e033@ec2-54-165-178-178.compute-1.amazonaws.com:5432/dec71qhll81qvg'}
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


db = SQLAlchemy(app)


from vaccinometer import routes
db.create_all()