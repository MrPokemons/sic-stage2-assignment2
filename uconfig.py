import os
import ngrok
from dotenv import load_dotenv
load_dotenv()

HOST = os.getenv("HOST")
PORT = os.getenv("PORT")

MONGODB_URI = os.getenv("MONGODB_URI")
NGROK_TOKEN = os.getenv("NGROK_AUTHTOKEN")

if NGROK_TOKEN is not None:
    listener = ngrok.forward(PORT, authtoken_from_env=True)  # forwarding to localhost:PORT
    print(f"Ingress established at: {listener.url()}")