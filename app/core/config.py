import os
from dotenv import load_dotenv

load_dotenv()

APP_ENV = os.environ.get("APP_ENV", "development")