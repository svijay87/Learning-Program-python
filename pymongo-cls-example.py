from pymongo import MongoClient
from pprint import pprint

class MongoDBClient:
    def __init__(self, host="localhost", port=27017):
        self.host = host
        self.port = port
        self._connect()

    def _connect(self):
        self.client = MongoClient(f"mongodb://{self.host}:{self.port}")
        self.db     = self.client.rptutorials
        self.tutorial = self.client.tutorial

    def getData(self, **filter):
        #TBD convert filter into pymongo search string and apply
        # tutorials = self.client.tutorial.find()
        # return tutorials
         print(dir(self.tutorial))


    def updateData(self):
        pass

    def deleteData(self):
        pass


mongo_db_obj = MongoDBClient()
result = mongo_db_obj.getData()
pprint(result)