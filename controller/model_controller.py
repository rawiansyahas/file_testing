import numpy as np
from PIL import Image
from tensorflow import keras
from information.model_info import apelsick_info, banana_info, corn_info, orange_info, potato_info, rice_info, cassava_info, tomato_info

# Load both models
apelsick_model_path = 'models/apelsick.h5'
apelsick_model = keras.models.load_model(apelsick_model_path)
apelsick_labels = ['Apple Scab', 'Black Rot', 'Cedar Apple Rust', 'Healthy']

banana_model_path = 'models/banana_inception_model.h5'
banana_model = keras.models.load_model(banana_model_path)
banana_labels = ['Cordana', 'Sigatoka', 'Pestalotiopsis', 'Healthy']

corn_model_path = 'models/ver2_corn_inception_model.h5'
corn_model = keras.models.load_model(corn_model_path)
corn_labels = ['Corn Healthy', 'Corn Gray Leaf Spot', 'Corn Common Rust', 'Corn Northern Leaf Blight']

orange_model_path = 'models/orange_fruitdisease_prediction_model.h5'
orange_model = keras.models.load_model(orange_model_path)
orange_labels = ['Blackspot', 'Cancer', 'Fresh', 'Greening']

potato_model_path = 'models/potato_leafdisease_prediction_model.h5'
potato_model = keras.models.load_model(potato_model_path)
potato_labels = ['Early Blight', 'Healthy', 'Late Blight']

rice_model_path = 'models/rice_disease.h5'
rice_model = keras.models.load_model(rice_model_path)
rice_labels = ['Brown Spot', 'Healthy', 'Leaf Blast', 'Neck_Blast']

cassava_model_path = 'models/cassava_inception_model.h5'
cassava_model = keras.models.load_model(cassava_model_path)
cassava_labels = ['Cassava Bacterial Blight', 'Cassava Brown Streak Disease', 'Cassava Green Mottle', 'Cassava Mosaic Disease', 'Healthy']

tomato_model_path = 'models/tomatodisease.h5'
tomato_model = keras.models.load_model(tomato_model_path)
tomato_labels = ['Tomato mosaic virus', 'Target Spot', 'Bacterial spot', 'Tomato Yellow Leaf Curl Virus', 'Late blight', 'Leaf Mold', 'Early blight', 'Spider mites Two-spotted spider mite', 'Tomato Healthy', 'Septoria leaf spot']

def predict_apelsick(img):
    i = np.array(img) / 255.0
    if len(i.shape) == 3:
        i = i.reshape(1, 224, 224, 3)
    else:
        i = i.reshape(1, 224, 224, 1)
    pred = apelsick_model.predict(i)
    pred_class = np.argmax(pred)
    confidence = pred[0][pred_class] * 100
    result = apelsick_labels[pred_class]
    info = apelsick_info[result]
    return result, confidence, info['description'], info['solution'], img


def predict_banana(img):
    i = np.array(img) / 255.0
    if len(i.shape) == 3:
        i = i.reshape(1, 150, 150, 3)
    else:
        i = i.reshape(1, 150, 150, 1)
    pred = banana_model.predict(i)
    pred_class = np.argmax(pred)
    confidence = pred[0][pred_class] * 100
    result = banana_labels[pred_class]
    info = banana_info[result]
    return result, confidence, info['description'], info['solution'], img

def predict_corn(img):
    i = np.array(img) / 255.0
    if len(i.shape) == 3:
        i = i.reshape(1, 150, 150, 3)
    else:
        i = i.reshape(1, 150, 150, 1)
    pred = corn_model.predict(i)
    pred_class = np.argmax(pred)
    confidence = pred[0][pred_class] * 100
    result = corn_labels[pred_class]
    info = corn_info[result]
    return result, confidence, info['description'], info['solution'], img

def predict_orange(img):
    i = np.array(img) / 255.0
    if len(i.shape) == 3:
        i = i.reshape(1, 64, 64, 3)
    else:
        i = i.reshape(1, 64, 64, 1)
    pred = orange_model.predict(i)
    pred_class = np.argmax(pred)
    confidence = pred[0][pred_class] * 100
    result = orange_labels[pred_class]
    info = orange_info[result]
    return result, confidence, info['description'], info['solution'], img

def predict_potato(img):
    i = np.array(img) / 255.0
    if len(i.shape) == 3:
        i = i.reshape(1, 64, 64, 3)
    else:
        i = i.reshape(1, 64, 64, 1)
    pred = potato_model.predict(i)
    pred_class = np.argmax(pred)
    confidence = pred[0][pred_class] * 100
    result = potato_labels[pred_class]
    info = potato_info[result]
    return result, confidence, info['description'], info['solution'], img

def predict_rice(img):
    i = np.array(img) / 255.0
    if len(i.shape) == 3:
        i = i.reshape(1, 224, 224, 3)
    else:
        i = i.reshape(1, 224, 224, 1)
    pred = rice_model.predict(i)
    pred_class = np.argmax(pred)
    confidence = pred[0][pred_class] * 100
    result = rice_labels[pred_class]
    info = rice_info[result]
    return result, confidence, info['description'], info['solution'], img

def predict_cassava(img):
    i = np.array(img) / 255.0
    if len(i.shape) == 3:
        i = i.reshape(1, 150, 150, 3)
    else:
        i = i.reshape(1, 150, 150, 1)
    pred = cassava_model.predict(i)
    pred_class = np.argmax(pred)
    confidence = pred[0][pred_class] * 100
    result = cassava_labels[pred_class]
    info = cassava_info[result]
    return result, confidence, info['description'], info['solution'], img

def predict_tomato(img):
    i = np.array(img) / 255.0
    if len(i.shape) == 3:
        i = i.reshape(1, 224, 224, 3)
    else:
        i = i.reshape(1, 224, 224, 1)
    pred = tomato_model.predict(i)
    pred_class = np.argmax(pred)
    confidence = pred[0][pred_class] * 100
    result = tomato_labels[pred_class]
    info = tomato_info[result]
    return result, confidence, info['description'], info['solution'], img


