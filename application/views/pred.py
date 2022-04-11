import pickle
import os
import pandas as pd

def load_model():
    print(os.path.abspath(__file__))
    model = None
    with open('application/model/model.pkl','rb') as pickle_file:
        model = pickle.load(pickle_file)

    return model 

def Predict(value):
    model = load_model()
    data = [value]
    pred = model.predict(data)
    return pred
    
