from os import getenv
from dotenv import  load_dotenv

load_dotenv()

API_KEY = getenv('API_KEY')
API_SECRET = getenv('API_SECRET')
ACCESS_TOKEN = getenv('ACCESS_TOKEN')
ACCESS_TOKEN_SECRET = getenv('ACCESS_TOKEN_SECRET')
