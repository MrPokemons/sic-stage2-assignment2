from bson import json_util
from flask import Flask, request
from udb import sensor_collection
from uconfig import HOST, PORT

app = Flask(__name__)

@app.get('/')
def home():
    return "home"

@app.get('/sensor')
def get_sensor():
    dct = []
    for sensor in sensor_collection.find():
        dct.append({"timestamp": sensor.get("_id").generation_time.isoformat(), **sensor})
    return json_util.dumps(dct)

@app.post('/sensor')
def post_sensor():
    payload = request.json
    sensor_collection.insert_one(payload)
    return {"message": "success"}


if __name__ == "__main__":
    app.run(
        host=HOST,
        port=PORT,
        debug=False
    )