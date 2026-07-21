import os
from dotenv import load_dotenv

load_dotenv()

APP_NAME = os.getenv("APP_NAME", "EnterpriseWorkspace")
DEBUG = os.getenv("DEBUG", "False") == "True"
DATABASE_NAME = os.getenv("DATABASE_NAME", "sqlite:///enterprise.db")