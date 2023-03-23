import os
from dotenv import load_dotenv

load_dotenv() 
#finds/loads the .env file

DATABASE = os.getenv('DATABASE')
DB_USER = os.getenv('DB_USER')