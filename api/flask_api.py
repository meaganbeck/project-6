"""
Brevets RESTful API
"""
import os
import logging
import requests

import flask
from flask import Flask
from flask import request

from flask_restful import Api
from mongoengine import connect
 
from resources.brevet import Brevet
from resources.brevets import Brevets

# Connect MongoEngine to mongodb
connect(host=f"mongodb://{os.environ['MONGODB_HOSTNAME']}:27017/brevetsdb")
###
# Globals
###
app = Flask(__name__)
app.debug = True if "DEBUG" not in os.environ else os.environ["DEBUG"]
port_num = True if "PORT" not in os.environ else os.environ["PORT"]
app.logger.setLevel(logging.DEBUG)

api = Api(app)

api.add_resource(Brevet, "/api/brevet/<id>")
api.add_resource(Brevets, "/api/brevets")

#API_ADDR= os.environ["API_ADDR"]
#API_PORT = os.environ["API_PORT"]
#API_URL = f"http://{API_ADDR}:{API_PORT}/api/"


if __name__ == "__main__":
    app.run(port=port_num, host="0.0.0.0")


