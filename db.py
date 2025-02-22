import os
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

from dotenv import load_dotenv
load_dotenv()


uri = os.getenv("MONGODB_URI")
cluster = MongoClient(uri, server_api=ServerApi('1'))

db = cluster['SIC-Stage2-Assignment2DB']
sensor_collection = db["SensorData"]

# Send a ping to confirm a successful connection
try:
    cluster.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")

    print(sensor_collection.find().to_list())
    sensor_collection.insert_one({"sensor": 123})

except Exception as e:
    print(e)