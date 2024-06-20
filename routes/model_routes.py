from flask import Blueprint, request, jsonify
from controller.model_controller import predict_banana, predict_apelsick, predict_corn, predict_orange, predict_potato, predict_rice, predict_cassava, predict_tomato
import io
from PIL import Image
from db import get_db_connection
from middleware.authentication_middleware import auth_required

predict_blueprint = Blueprint('predict_banana', __name__)
#Try Push Update Routes
def save_prediction_to_db(image_bytes, prediction, confidence, description, solution,user_id):
    connection = get_db_connection()
    with connection.cursor() as cursor:
        cursor.execute(
            'INSERT INTO predictions (image, prediction, confidence, description, solution,user_id) VALUES (%s, %s, %s, %s, %s, %s)',
            (image_bytes, prediction, confidence, description, solution,user_id)
        )
    connection.commit()
    connection.close()

@predict_blueprint.route('/predict/apple', methods=["POST"])
@auth_required
def predict_apelsick_route():
    file = request.files.get('file')
    if file is None or file.filename == "":
        return jsonify({"error": "no file input in request"})
    
    image_bytes = file.read()
    img = Image.open(io.BytesIO(image_bytes))
    img = img.resize((224, 224), Image.NEAREST)
    prediction, confidence, description, solution, _ = predict_apelsick(img)
    user_id = request.user_id
    save_prediction_to_db(image_bytes, prediction, confidence, description, solution,user_id)
    return jsonify({
        "user_id" : user_id,
        "prediction": prediction, 
        "confidence": confidence,
        "description": description,
        "solution": solution
    })

@predict_blueprint.route('/predict/banana', methods=["GET", "POST"])
@auth_required
def predict_banana_route():
    file = request.files.get('file')
    if file is None or file.filename == "":
        return jsonify({"error": "no file input in request"})
    
    image_bytes = file.read()
    img = Image.open(io.BytesIO(image_bytes))
    img = img.resize((150, 150), Image.NEAREST)
    prediction, confidence, description, solution, _ = predict_banana(img)
    user_id = request.user_id
    save_prediction_to_db(image_bytes, prediction, confidence, description, solution,user_id)
    return jsonify({
        "user_id" : user_id,
        "prediction": prediction, 
        "confidence": confidence,
        "description": description,
        "solution": solution
    })

@predict_blueprint.route('/predict/corn', methods=["GET", "POST"])
@auth_required
def predict_corn_route():
    file = request.files.get('file')
    if file is None or file.filename == "":
        return jsonify({"error": "no file input in request"})
    
    image_bytes = file.read()
    img = Image.open(io.BytesIO(image_bytes))
    img = img.resize((150, 150), Image.NEAREST)
    prediction, confidence, description, solution, _ = predict_corn(img)
    user_id = request.user_id
    save_prediction_to_db(image_bytes, prediction, confidence, description, solution,user_id)
    return jsonify({
        "user_id" : user_id,
        "prediction": prediction, 
        "confidence": confidence,
        "description": description,
        "solution": solution
    })

@predict_blueprint.route('/predict/orange', methods=["GET", "POST"])
@auth_required
def predict_orange_route():
    file = request.files.get('file')
    if file is None or file.filename == "":
        return jsonify({"error": "no file input in request"})
    
    image_bytes = file.read()
    img = Image.open(io.BytesIO(image_bytes))
    img = img.resize((64, 64), Image.NEAREST)
    prediction, confidence, description, solution, _ = predict_orange(img)
    user_id = request.user_id
    save_prediction_to_db(image_bytes, prediction, confidence, description, solution,user_id)
    return jsonify({
        "user_id" : user_id,
        "prediction": prediction, 
        "confidence": confidence,
        "description": description,
        "solution": solution
    })

@predict_blueprint.route('/predict/potato', methods=["GET", "POST"])
@auth_required
def predict_potato_route():
    file = request.files.get('file')
    if file is None or file.filename == "":
        return jsonify({"error": "no file input in request"})
    
    image_bytes = file.read()
    img = Image.open(io.BytesIO(image_bytes))
    img = img.resize((64, 64), Image.NEAREST)
    prediction, confidence, description, solution, _ = predict_potato(img)
    user_id = request.user_id
    save_prediction_to_db(image_bytes, prediction, confidence, description, solution,user_id)
    return jsonify({
        "user_id" : user_id,
        "prediction": prediction, 
        "confidence": confidence,
        "description": description,
        "solution": solution
    })

@predict_blueprint.route('/predict/rice', methods=["GET", "POST"])
@auth_required
def predict_rice_route():
    file = request.files.get('file')
    if file is None or file.filename == "":
        return jsonify({"error": "no file input in request"})
    
    image_bytes = file.read()
    img = Image.open(io.BytesIO(image_bytes))
    img = img.resize((224, 224), Image.NEAREST)
    prediction, confidence, description, solution, _ = predict_rice(img)
    user_id = request.user_id
    save_prediction_to_db(image_bytes, prediction, confidence, description, solution,user_id)
    return jsonify({
        "user_id" : user_id,
        "prediction": prediction, 
        "confidence": confidence,
        "description": description,
        "solution": solution
    })

@predict_blueprint.route('/predict/cassava', methods=["GET", "POST"])
@auth_required
def predict_cassava_route():
    file = request.files.get('file')
    if file is None or file.filename == "":
        return jsonify({"error": "no file input in request"})
    
    image_bytes = file.read()
    img = Image.open(io.BytesIO(image_bytes))
    img = img.resize((150, 150), Image.NEAREST)
    prediction, confidence, description, solution, _ = predict_cassava(img)
    user_id = request.user_id
    save_prediction_to_db(image_bytes, prediction, confidence, description, solution,user_id)
    return jsonify({
        "user_id" : user_id,
        "prediction": prediction, 
        "confidence": confidence,
        "description": description,
        "solution": solution
    })

@predict_blueprint.route('/predict/tomato', methods=["GET", "POST"])
@auth_required
def predict_tomato_route():
    file = request.files.get('file')
    if file is None or file.filename == "":
        return jsonify({"error": "no file input in request"})
    
    image_bytes = file.read()
    img = Image.open(io.BytesIO(image_bytes))
    img = img.resize((224, 224), Image.NEAREST)
    prediction, confidence, description, solution, _ = predict_tomato(img)
    user_id = request.user_id
    save_prediction_to_db(image_bytes, prediction, confidence, description, solution,user_id)
    return jsonify({
        "user_id" : user_id,
        "prediction": prediction, 
        "confidence": confidence,
        "description": description,
        "solution": solution
    })