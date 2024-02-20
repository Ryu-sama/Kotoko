import pymongo
import os

MONGO_URL = "mongodb+srv://enmu:enmu123@enmu.2cuev.mongodb.net/myFirstDatabase?retryWrites=true&w=majority"

database = pymongo.MongoClient(MONGO_URL)['notes']['notes']
