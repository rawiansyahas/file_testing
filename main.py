from flask import Flask, render_template, request
from tensorflow.keras.models import load_model
import numpy as np
from tensorflow.keras.preprocessing.image import load_img
from tensorflow.keras.applications.vgg16 import preprocess_input
import os
from tensorflow.keras.preprocessing import image

app = Flask(__name__)
model = load_model('potato_leafdisease_prediction_model.h5')
target_img = os.path.join(os.getcwd(), 'static/images')

labels = labels = ['Early_Blight', 'Healthy', 'Late_Blight']

@app.route('/')
def index_view():
    return render_template('index.html')

#Allow files with extension png, jpg and jpeg
ALLOWED_EXT = set(['jpg', 'jpeg', 'png'])
def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1] in ALLOWED_EXT
           

@app.route('/predict', methods=['GET', 'POST'])
def predict():
    if request.method == 'POST':
        file = request.files['file']
        if file and allowed_file(file.filename):
            filename = file.filename
            file_path = os.path.join('static/images', filename)
            file.save(file_path)
            img = image.load_img(file_path, target_size=(64, 64))
            x = image.img_to_array(img)
            x = np.expand_dims(x, axis=0)
            x /= 255

            # Use the loaded model to make predictions
            classes = model.predict(x)

            predicted_class_indices = np.argmax(classes)
            fruit = labels[predicted_class_indices]

            # Calculate probabilities
            probabilities = [f"{label} : {prob:.2f}%" for label, prob in zip(labels, classes[0])]

            # Extract the probability of the predicted class
            prob = probabilities[predicted_class_indices]

            return render_template('predict.html', fruit=fruit, prob=prob, user_image=file_path)
        else:
            return "Unable to read the file. Please check file extension"

if __name__ == '__main__':
    app.run(debug=True,use_reloader=False, port=8000)