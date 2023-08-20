from flask import *
import datetime
from MongoDBHelper import MongoDBHelper
import hashlib
from bson.objectid import ObjectId


web_app = Flask("MatchMingle")


@web_app.route("/")
def index():
    return render_template('index.html')


def main():
    # In order to use session object in flask, we need to set some key as secret_key in app
    web_app.secret_key = 'MatchMingle-key-1'
    web_app.run(port=5001)


if __name__ == "__main__":
    main()
