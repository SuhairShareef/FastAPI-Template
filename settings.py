import os

from dotenv import load_dotenv

from utils.definitions import ENV_PATH

load_dotenv(ENV_PATH)

APP_NAME = os.getenv("APP_NAME")
