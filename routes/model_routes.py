from flask import Blueprint, request, jsonify
from controller.model_controller import predict_banana, predict_apelsick, predict_corn, predict_orange, predict_potato, predict_rice, predict_cassava, predict_tomato
from db import get_db_connection
import io
from PIL import Image

predict_blueprint = Blueprint('predict_banana', __name__)

def save_prediction(image_name, model_name, prediction, confidence):
    connection = get_db_connection()
    with connection.cursor() as cursor:
        sql = "INSERT INTO predictions (image_name, model_name, prediction, confidence) VALUES (%s, %s, %s, %s)"
        cursor.execute(sql, (image_name, model_name, prediction, confidence))
        connection.commit()
    connection.close()

@predict_blueprint.route('/predict/apple', methods=["GET", "POST"])
def predict_apelsick_route():
    file = request.files.get('file')
    if file is None or file.filename == "":
        return jsonify({"error": "no file input in request"})
    
    image_bytes = file.read()
    img = Image.open(io.BytesIO(image_bytes))
    img = img.resize((224, 224), Image.NEAREST)
    pred_img, confidence = predict_apelsick(img)
    save_prediction(file.filename, "Apel", pred_img, confidence)
    return jsonify({
        "prediction": pred_img, 
        "confidence": confidence
        })

@predict_blueprint.route('/predict/banana', methods=["GET", "POST"])
def predict_banana_route():
    file = request.files.get('file')
    if file is None or file.filename == "":
        return jsonify({"error": "no file input in request"})
    
    image_bytes = file.read()
    img = Image.open(io.BytesIO(image_bytes))
    img = img.resize((150, 150), Image.NEAREST)
    pred_img, confidence = predict_banana(img)
    save_prediction(file.filename, "Pisang", pred_img, confidence)
    return jsonify({
        "prediction": pred_img, 
        "confidence": confidence
        })

@predict_blueprint.route('/predict/corn', methods=["GET", "POST"])
def predict_corn_route():
    file = request.files.get('file')
    if file is None or file.filename == "":
        return jsonify({"error": "no file input in request"})
    
    image_bytes = file.read()
    img = Image.open(io.BytesIO(image_bytes))
    img = img.resize((150, 150), Image.NEAREST)
    pred_img, confidence = predict_corn(img)
    save_prediction(file.filename, "Jagung", pred_img, confidence)
    return jsonify({
        "prediction": pred_img, 
        "confidence": confidence
        })

@predict_blueprint.route('/predict/orange', methods=["GET", "POST"])
def predict_orange_route():
    file = request.files.get('file')
    if file is None or file.filename == "":
        return jsonify({"error": "no file input in request"})
    
    image_bytes = file.read()
    img = Image.open(io.BytesIO(image_bytes))
    img = img.resize((64, 64), Image.NEAREST)
    pred_img, confidence = predict_orange(img)
    save_prediction(file.filename, "Jeruk", pred_img, confidence)
    return jsonify({
        "prediction": pred_img, 
        "confidence": confidence
        })

@predict_blueprint.route('/predict/potato', methods=["GET", "POST"])
def predict_potato_route():
    file = request.files.get('file')
    if file is None or file.filename == "":
        return jsonify({"error": "no file input in request"})
    
    image_bytes = file.read()
    img = Image.open(io.BytesIO(image_bytes))
    img = img.resize((64, 64), Image.NEAREST)
    pred_img, confidence = predict_potato(img)
    save_prediction(file.filename, "Kentang", pred_img, confidence)
    return jsonify({
        "prediction": pred_img, 
        "confidence": confidence
        })

@predict_blueprint.route('/predict/rice', methods=["GET", "POST"])
def predict_rice_route():
    file = request.files.get('file')
    if file is None or file.filename == "":
        return jsonify({"error": "no file input in request"})
    
    image_bytes = file.read()
    img = Image.open(io.BytesIO(image_bytes))
    img = img.resize((224, 224), Image.NEAREST)
    pred_img, confidence = predict_rice(img)
    save_prediction(file.filename, "Padi", pred_img, confidence)
    return jsonify({
        "prediction": pred_img, 
        "confidence": confidence
        })

@predict_blueprint.route('/predict/cassava', methods=["GET", "POST"])
def predict_cassava_route():
    file = request.files.get('file')
    if file is None or file.filename == "":
        return jsonify({"error": "no file input in request"})
    
    image_bytes = file.read()
    img = Image.open(io.BytesIO(image_bytes))
    img = img.resize((256, 256), Image.NEAREST)
    pred_img, confidence = predict_cassava(img)
    save_prediction(file.filename, "Singkong", pred_img, confidence)
    return jsonify({
        "prediction": pred_img, 
        "confidence": confidence
        })

@predict_blueprint.route('/predict/tomato', methods=["GET", "POST"])
def predict_tomato_route():
    file = request.files.get('file')
    if file is None or file.filename == "":
        return jsonify({"error": "no file input in request"})
    
    image_bytes = file.read()
    img = Image.open(io.BytesIO(image_bytes))
    img = img.resize((256, 256), Image.NEAREST)
    pred_img, confidence = predict_tomato(img)
    save_prediction(file.filename, "Tomat", pred_img, confidence)
    return jsonify({
        "prediction": pred_img, 
        "confidence": confidence
        })