from flask import Blueprint, request, jsonify
from controller.model_controller import predict_banana, predict_apelsick, predict_corn, predict_orange, predict_potato, predict_rice, predict_cassava, predict_tomato
import io
from PIL import Image
from app import get_db_connection

predict_blueprint = Blueprint('predict_banana', __name__)

def save_prediction_to_db(image_bytes, prediction, confidence, description, solution):
    connection = get_db_connection()
    with connection.cursor() as cursor:
        cursor.execute(
            'INSERT INTO predictions (image, prediction, confidence, description, solution) VALUES (%s, %s, %s, %s, %s)',
            (image_bytes, prediction, confidence, description, solution)
        )
    connection.commit()
    connection.close()

@predict_blueprint.route('/predict/apple', methods=["POST"])
def predict_apelsick_route():
    file = request.files.get('file')
    if file is None or file.filename == "":
        return jsonify({"error": "no file input in request"})
    
    image_bytes = file.read()
    img = Image.open(io.BytesIO(image_bytes))
    img = img.resize((224, 224), Image.NEAREST)
    prediction, confidence, description, solution, _ = predict_apelsick(img)
    save_prediction_to_db(image_bytes, prediction, confidence, description, solution)
    return jsonify({
        "prediction": prediction, 
        "confidence": confidence,
        "description": description,
        "solution": solution
    })

@predict_blueprint.route('/predict/banana', methods=["GET", "POST"])
def predict_banana_route():
    file = request.files.get('file')
    if file is None or file.filename == "":
        return jsonify({"error": "no file input in request"})
    
    image_bytes = file.read()
    img = Image.open(io.BytesIO(image_bytes))
    img = img.resize((150, 150), Image.NEAREST)
    prediction, confidence, description, solution, _ = predict_banana(img)
    save_prediction_to_db(image_bytes, prediction, confidence, description, solution)
    return jsonify({
        "prediction": prediction, 
        "confidence": confidence,
        "description": description,
        "solution": solution
    })

@predict_blueprint.route('/predict/corn', methods=["GET", "POST"])
def predict_corn_route():
    file = request.files.get('file')
    if file is None or file.filename == "":
        return jsonify({"error": "no file input in request"})
    
    image_bytes = file.read()
    img = Image.open(io.BytesIO(image_bytes))
    img = img.resize((150, 150), Image.NEAREST)
    prediction, confidence, description, solution, _ = predict_corn(img)
    save_prediction_to_db(image_bytes, prediction, confidence, description, solution)
    return jsonify({
        "prediction": prediction, 
        "confidence": confidence,
        "description": description,
        "solution": solution
    })

@predict_blueprint.route('/predict/orange', methods=["GET", "POST"])
def predict_orange_route():
    file = request.files.get('file')
    if file is None or file.filename == "":
        return jsonify({"error": "no file input in request"})
    
    image_bytes = file.read()
    img = Image.open(io.BytesIO(image_bytes))
    img = img.resize((64, 64), Image.NEAREST)
    prediction, confidence, description, solution, _ = predict_orange(img)
    save_prediction_to_db(image_bytes, prediction, confidence, description, solution)
    return jsonify({
        "prediction": prediction, 
        "confidence": confidence,
        "description": description,
        "solution": solution
    })

@predict_blueprint.route('/predict/potato', methods=["GET", "POST"])
def predict_potato_route():
    file = request.files.get('file')
    if file is None or file.filename == "":
        return jsonify({"error": "no file input in request"})
    
    image_bytes = file.read()
    img = Image.open(io.BytesIO(image_bytes))
    img = img.resize((64, 64), Image.NEAREST)
    prediction, confidence, description, solution, _ = predict_potato(img)
    save_prediction_to_db(image_bytes, prediction, confidence, description, solution)
    return jsonify({
        "prediction": prediction, 
        "confidence": confidence,
        "description": description,
        "solution": solution
    })

@predict_blueprint.route('/predict/rice', methods=["GET", "POST"])
def predict_rice_route():
    file = request.files.get('file')
    if file is None or file.filename == "":
        return jsonify({"error": "no file input in request"})
    
    image_bytes = file.read()
    img = Image.open(io.BytesIO(image_bytes))
    img = img.resize((224, 224), Image.NEAREST)
    prediction, confidence, description, solution, _ = predict_rice(img)
    save_prediction_to_db(image_bytes, prediction, confidence, description, solution)
    return jsonify({
        "prediction": prediction, 
        "confidence": confidence,
        "description": description,
        "solution": solution
    })

@predict_blueprint.route('/predict/cassava', methods=["GET", "POST"])
def predict_cassava_route():
    file = request.files.get('file')
    if file is None or file.filename == "":
        return jsonify({"error": "no file input in request"})
    
    image_bytes = file.read()
    img = Image.open(io.BytesIO(image_bytes))
    img = img.resize((150, 150), Image.NEAREST)
    prediction, confidence, description, solution, _ = predict_cassava(img)
    save_prediction_to_db(image_bytes, prediction, confidence, description, solution)
    return jsonify({
        "prediction": prediction, 
        "confidence": confidence,
        "description": description,
        "solution": solution
    })

@predict_blueprint.route('/predict/tomato', methods=["GET", "POST"])
def predict_tomato_route():
    file = request.files.get('file')
    if file is None or file.filename == "":
        return jsonify({"error": "no file input in request"})
    
    image_bytes = file.read()
    img = Image.open(io.BytesIO(image_bytes))
    img = img.resize((224, 224), Image.NEAREST)
    prediction, confidence, description, solution, _ = predict_tomato(img)
    save_prediction_to_db(image_bytes, prediction, confidence, description, solution)
    return jsonify({
        "prediction": prediction, 
        "confidence": confidence,
        "description": description,
        "solution": solution
    })