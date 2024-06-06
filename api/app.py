from flask import Flask
from flask import render_template
from flask_cors import CORS
import keras as ks
import numpy as np
import os
import io
from PIL import Image
from flask import request
from flask import jsonify
from werkzeug.utils import secure_filename

app = Flask(__name__)
CORS(app)

MODELS_DIR = '../modelo/'

models = {
    'efficientnet': {
        'morango': ks.models.load_model(os.path.join(MODELS_DIR, 'effnet_model_morangos.keras')),
        'pessego': ks.models.load_model(os.path.join(MODELS_DIR, 'effnet_model_pessegos.keras')),
        'roma': ks.models.load_model(os.path.join(MODELS_DIR, 'effnet_model_romas.keras'))
    },
    'resnet': {
        'morango': ks.models.load_model(os.path.join(MODELS_DIR, 'resnet_model_morangos.keras')),
        'pessego': ks.models.load_model(os.path.join(MODELS_DIR, 'resnet_model_pessegos.keras')),
        'roma': ks.models.load_model(os.path.join(MODELS_DIR, 'resnet_model_romas.keras'))
    }
}


def load_and_prepare_image(image):
    img = image.resize((300, 300))
    img_array = ks.preprocessing.image.img_to_array(img)
    img_array = np.array([img_array])
    return img_array


@app.route('/predict', methods=['POST'])
def predict():
    if 'file' not in request.files:
        return jsonify({'error': 'No file part'}), 400

    file = request.files['file']
    if file.filename == '':
        return jsonify({'error': 'No selected file'}), 400

    if file:
        filename = secure_filename(file.filename)
        img = Image.open(io.BytesIO(file.read()))
        model_name = request.form.get('model')
        fruit_name = request.form.get('fruit')

        if model_name not in models:
            return jsonify({'error': f'Model {model_name} is not supported'}), 400
        if fruit_name not in models[model_name]:
            return jsonify({'error': f'Fruit {fruit_name} is not supported for model {model_name}'}), 400

        model = models[model_name][fruit_name]

        processed_image = load_and_prepare_image(img)
        prediction = model.predict(processed_image)
        pred_label = (prediction > 0.5).astype("int32")[0][0]
        prediction = prediction[0][0]

        return jsonify({'prediction': float(prediction),
                        'label': int(pred_label),
                        'quality': 'Esta fruta é saudável' if pred_label == 0 else 'Esta fruta é podre'})


if __name__ == '__main__':
    app.run(debug=True)
