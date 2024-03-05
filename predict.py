from ultralytics import YOLO

import numpy as np


def predict_deffect(img):
    model = YOLO("./model.pt")  # load a custom model
    results = model(img)
    names_dict = results[0].names
    probs = results[0].probs.data.tolist()
    prediction = names_dict[np.argmax(probs)]
    return prediction
