import pymongo


class MongoDBHelper:
    def __init__(self, collection = "user"):
        uri = "mongodb+srv://root:123456789123456789@gws.dywpisw.mongodb.net/?retryWrites=true&w=majority"
        client = pymongo.MongoClient(uri)
        self.db = client['MatchMingle']
        self.collection = self.db[collection]
        print("MongoDB Connected")
