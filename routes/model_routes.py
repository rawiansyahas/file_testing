from flask import Blueprint, request, jsonify
from controller.model_controller import predict_banana, predict_apelsick, predict_corn, predict_orange, predict_potato, predict_rice, predict_cassava, predict_tomato
import io
from PIL import Image

predict_blueprint = Blueprint('predict_banana', __name__)

@predict_blueprint.route('/predict/apple', methods=["GET", "POST"])
def predict_apelsick_route():
    file = request.files.get('file')
    if file is None or file.filename == "":
        return jsonify({"error": "no file input in request"})
    
    image_bytes = file.read()
    img = Image.open(io.BytesIO(image_bytes))
    img = img.resize((224, 224), Image.NEAREST)
    pred_img, confidence, description, solution = predict_apelsick(img)
    return jsonify({
        "prediction": pred_img, 
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
    pred_img, confidence, description, solution = predict_banana(img)
    return jsonify({
        "prediction": pred_img, 
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
    pred_img, confidence, description, solution = predict_corn(img)
    return jsonify({
        "prediction": pred_img, 
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
    pred_img, confidence, description, solution = predict_orange(img)
    return jsonify({
        "prediction": pred_img, 
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
    pred_img, confidence, description, solution = predict_potato(img)
    return jsonify({
        "prediction": pred_img, 
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
    pred_img, confidence, description, solution = predict_rice(img)
    return jsonify({
        "prediction": pred_img, 
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
    pred_img, confidence, description, solution = predict_cassava(img)
    return jsonify({
        "prediction": pred_img, 
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
    pred_img, confidence, description, solution = predict_tomato(img)
    return jsonify({
        "prediction": pred_img, 
        "confidence": confidence,
        "description": description,
        "solution": solution
    })