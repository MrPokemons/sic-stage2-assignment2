# Samsung Innovation Campus: Stage 2 Assignment 2

| Group Informations  |   |
|---------------|---------------|
| Group Code  | UNI422  |
| Group Name  | rarevolution  |
| Team  | - Adeline Charlotte Augustinne<br>- Angeline Rachel<br>- Anastashia Ellena Widjaja<br>- Rowen Nicholas    |

---

## Flask IoT Sensor API

This repository provides a simple Flask API to act as an intermediate layer for IoT sensor data storage using MongoDB (via PyMongo). The API allows retrieving and storing sensor data, with optional support for global access through Ngrok.

### Features
- Retrieve sensor data from MongoDB.
- Store IoT sensor data via a RESTful API to MongoDB.
- Automatic Ngrok setup for public access if an authentication token is provided.

### Installation

#### 1. Clone the Repository
```sh
git clone https://github.com/MrPokemons/sic-stage2-assignment2.git
cd sic-stage2-assignment2
```

#### 2. Install Dependencies
Ensure you have Python installed, then install the required packages:
```sh
pip install -r requirements.txt
```

#### 3. Setup the Environment Variables
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

#### 4. Run the Flask API
```sh
python app.py
```

If an `NGROK_AUTHTOKEN` is provided, Ngrok will automatically start and generate a public URL for accessing the API globally.

### API Endpoints

#### Home
```http
GET /
```
**Response:**
```json
{
  "message": "home"
}
```

#### Retrieve Sensor Data
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

#### Store Sensor Data
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

## Running IoT MicroPython Script on ESP32 (Using Thonny IDE)
To send sensor data from an ESP32 running MicroPython, follow these steps:

### 1. Install Thonny IDE
Download and install [Thonny IDE](https://thonny.org/). Ensure you have the latest version with MicroPython support.

### 2. Flash MicroPython on ESP32
Follow the guide to install MicroPython firmware on your ESP32:
- Download the latest MicroPython firmware from [MicroPython Downloads](https://micropython.org/download/esp32/).
- Use Thonny IDE to flash the firmware (Tools > Options > Interpreter > Install or update firmware).

### 3. Upload and Run the ESP32 Script
Use the provided script `espmonitoring-rarevolution.py` in this repository.

1. Connect your ESP32 to your computer.
2. Open Thonny IDE and select **MicroPython (ESP32)** as the interpreter.
3. Open `espmonitoring-rarevolution.py` from this repository.
4. Click **Run** to execute the script on the ESP32.
