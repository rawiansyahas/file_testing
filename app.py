from flask import Flask
from routes.model_routes import predict_blueprint
import os
import pymysql
from dotenv import load_dotenv
import sys

# Ensure the script can access the parent directory
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# Load environment variables from .env file
load_dotenv()

app = Flask(__name__)
app.register_blueprint(predict_blueprint)

# Configure database connection
DB_USER = os.getenv('DB_USER')
DB_PASSWORD = os.getenv('DB_PASSWORD')
DB_NAME = os.getenv('DB_NAME')
DB_CONNECTION_NAME = os.getenv('DB_CONNECTION_NAME')

def get_db_connection():
    # Check if running in Google Cloud environment
    if os.getenv('GAE_ENV', '').startswith('standard'):
        # Use Unix socket for connection
        unix_socket = f'/cloudsql/{DB_CONNECTION_NAME}'
        return pymysql.connect(user=DB_USER, password=DB_PASSWORD, database=DB_NAME, unix_socket=unix_socket)
    else:
        # Local testing with Cloud SQL Proxy
        return pymysql.connect(user=DB_USER, password=DB_PASSWORD, database=DB_NAME, host='127.0.0.1', port=3306)

@app.route('/db_test')
def db_test():
    connection = get_db_connection()
    with connection.cursor() as cursor:
        cursor.execute('SELECT NOW()')
        result = cursor.fetchone()
    connection.close()
    return f'Time from DB: {result[0]}'

if __name__ == '__main__':
    app.run(debug=True)
