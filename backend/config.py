import os
from dotenv import load_dotenv

load_dotenv()

MONGO_URI = os.getenv('MONGO_URI')
UPLOAD_FOLDER = os.getenv('UPLOAD_FOLDER')
