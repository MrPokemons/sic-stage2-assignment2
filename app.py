from bson import json_util as bjson
from flask import Flask, request, Response
from pydantic import ValidationError

from udb import sensor_collection
from uconfig import HOST, PORT
from uschema import SensorData

app = Flask(__name__)

@app.get('/')
def home():
    return {"message": "home"}

@app.get('/sensor')
def get_sensor():
    query_result = sensor_collection.find({}, {'_id': 0})
    return Response(
        bjson.dumps([SensorData.model_validate(sensor).model_dump() for sensor in query_result]),
        status=200,
        mimetype="application/json"
    )

@app.post('/sensor')
def post_sensor():
    payload = request.json
    try:
        sensor_data = SensorData.model_validate(payload)
        sensor_collection.insert_one(sensor_data.model_dump())
        return Response(bjson.dumps({"message": "success"}), status=201, mimetype="application/json")
    except ValidationError as e:
        return Response(bjson.dumps({"error": str(e)}), status=400, mimetype="application/json")


if __name__ == "__main__":
    app.run(
        host=HOST,
        port=PORT,
        debug=False
    )