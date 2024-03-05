# save this as app.py
from flask import Flask, jsonify, request
from predict import predict_deffect
from PIL import Image

app = Flask(__name__)


@app.route("/")
def hello():
    return jsonify(greeting="Hello World!")


@app.route("/predict", methods=["POST"])
def predict():
    img_data = request.files["image"]
    img = Image.open(img_data.stream)
    deffect = predict_deffect(img)
    return jsonify(prediction=deffect)


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=8080)
