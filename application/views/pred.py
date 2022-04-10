import pickle

def load_model():
    with open('model/model.pkl','rb') as pickle_file:
        model = pickle.load(pickle_file)

    return model 

def Predict(value):
    model = load_model()
    
    y_pred = model.predict(value)
    return y_pred
    
