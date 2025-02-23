# Samsung Innovation Campus: Stage 2 Assignment 2

| Group Informations  |   |
|---------------|---------------|
| Group Code  | UNI422  |
| Group Name  | rarevolution  |
| Team  | - Adeline Charlotte Augustinne<br>- Angeline Rachel<br>- Anastashia Ellena Widjaja<br>- Rowen Nicholas    |

---

# Flask IoT Sensor API

This repository provides a simple Flask API to act as an intermediate layer for IoT sensor data storage using MongoDB (via PyMongo). The API allows retrieving and storing sensor data, with optional support for global access through Ngrok.

## Features
- Retrieve sensor data from MongoDB.
- Store IoT sensor data via a RESTful API to MongoDB.
- Automatic Ngrok setup for public access if an authentication token is provided.

## Installation

### 1. Clone the Repository
```sh
git clone https://github.com/MrPokemons/sic-stage2-assignment2.git
cd sic-stage2-assignment2
```

### 2. Install Dependencies
Ensure you have Python installed, then install the required packages:
```sh
pip install -r requirements.txt
```

### 3. Setup the Environment Variables
Create a `.env` file in the project root with the following format:
```
MONGODB_URI = "your_mongodb_connection_string"

# Optional: Enable Ngrok for global API access
# NGROK_AUTHTOKEN = "your_ngrok_auth_token"

HOST="0.0.0.0"
PORT=8000
```
- Replace `MONGODB_URI` with your actual MongoDB connection string.
- (Optional) If you want to expose the API globally using Ngrok, provide your `NGROK_AUTHTOKEN` from [Ngrok's official site](https://ngrok.com/).

### 4. Run the Flask API
```sh
python app.py
```

If an `NGROK_AUTHTOKEN` is provided, Ngrok will automatically start and generate a public URL for accessing the API globally.

## API Endpoints

### Home
```http
GET /
```
**Response:**
```json
{
  "message": "home"
}
```

### Retrieve Sensor Data
```http
GET /sensor
```
**Response:**
```json
[
  {
    "timestamp": "2024-02-23T12:00:00",
    "humidity": 45.6,
    "ldr": 500.2,
    "temperature": 23.5
  }
]
```

### Store Sensor Data
```http
POST /sensor
```
**Request Body:**
```json
{
  "timestamp": "2024-02-23T12:00:00",
  "humidity": 45.6,
  "ldr": 500.2,
  "temperature": 23.5
}
```
**Response:**
```json
{
  "message": "success"
}
```

