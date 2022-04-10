import pickle
import os

def load_model():
    print(os.path.abspath(__file__))
    model = None
    with open('application/model/model.pkl','rb') as pickle_file:
        model = pickle.load(pickle_file)

    return model 

def Predict(value):
    model = load_model()
    
    y_pred = model.predict(value)
    return y_pred
    
