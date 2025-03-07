from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from uconfig import MONGODB_URI


cluster = MongoClient(MONGODB_URI, server_api=ServerApi('1'), connect=False)
db = cluster['SIC-Stage2-Assignment2DB']
sensor_collection = db["SensorData"]


if __name__ == "__main__":
    try:
        cluster.admin.command('ping')
        print("Pinged your deployment. You successfully connected to MongoDB!")
    except Exception as e:
        print(e)