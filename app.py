from bson import json_util
from flask import Flask, request, jsonify
from udb import sensor_collection
from uconfig import HOST, PORT

app = Flask(__name__)

@app.get('/')
def home():
    return "home"

@app.get('/sensor')
def get_sensor():
    return jsonify(json_util.dumps(sensor_collection.find().to_list()))

@app.post('/sensor')
def post_sensor():
    payload = request.json
    sensor_collection.insert_one(payload)


if __name__ == "__main__":
    app.run(
        host=HOST,
        port=PORT,
        debug=False
    )