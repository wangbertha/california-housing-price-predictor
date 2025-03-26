from flask import Flask
import numpy as np
import pickle

app = Flask(__name__)

@app.route("/")
def hello_world():
    test_input = np.array([[-119.6, 35.6, 28.5, 7, 6, 7, 6, 4, 1, 0, 0, 0, 0, 0.8, 1.3]])
    with open('../model.pkl', 'rb') as file:
        data = pickle.load(file)
    
    regressor_loaded = data["model"]
    prediction = regressor_loaded.predict(test_input)
    prediction_as_str = str(prediction)
    print(prediction)
    return prediction_as_str