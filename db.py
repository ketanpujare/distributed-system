from pymongo import MongoClient

def get_connection():
    mongo = MongoClient('mongodb',27017)
    return mongo

def close_connection(mongo):
    mongo.close()

