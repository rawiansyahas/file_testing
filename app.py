from flask import Flask
from routes.model_routes import predict_blueprint
import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

app = Flask(__name__)

app.register_blueprint(predict_blueprint)

if __name__ == '__main__':
    app.run(debug=True)
