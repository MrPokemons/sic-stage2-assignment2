import os
from dotenv import load_dotenv
load_dotenv()

MONGODB_URI = os.getenv("MONGODB_URI")
HOST = os.getenv("HOST")
PORT = os.getenv("PORT")