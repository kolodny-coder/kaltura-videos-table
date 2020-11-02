from flask import Flask

from config import Config
# from flask_mongoengine import MongoEngine, Document
from flask_restplus import Api


app = Flask(__name__)
api = Api(app)

from application import routes
