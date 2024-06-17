import pymysql
from dotenv import load_dotenv
import os

load_dotenv()  # Load environment variables from .env file

def get_db_connection():
    connection = pymysql.connect(
        host=os.getenv('DB_HOST'),
        user=os.getenv('DB_USER'),
        password=os.getenv('DB_PASSWORD'),
        db=os.getenv('DB_NAME'),
        cursorclass=pymysql.cursors.DictCursor
    )
    return connection
