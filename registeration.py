from flask import *
import datetime
from MongoDBHelper import MongoDBHelper
import hashlib
from bson.objectid import ObjectId


web_app = Flask("MatchMingle")


@web_app.route("/")
def index():
    return render_template('index.html')