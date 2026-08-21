import customdataset as cd
import streamlit as stream
import pandas as pd
import pickle
from sklearn.model_selection import train_test_split
from sklearn.svm import SVR as tempmodel, SVC as rainmodel

data=cd.data 

def train_save_model():
    df = pd.DataFrame(data)
    X = df[['Month', 'Humidity']] 
    ytemp = df['Temperature']
    yrain = df['Rainfall']
    
    X_train, X_test, ytemp_train, ytemp_test = train_test_split(X, ytemp, test_size=0.2, random_state=42)
    _, _, yrain_train, yrain_test = train_test_split(X, yrain, test_size=0.2, random_state=42)
    
    braintemp = tempmodel(kernel='rbf', C=100, epsilon=0.1)
    brainrain = rainmodel(kernel='linear')

    braintemp.fit(X_train, ytemp_train)
    brainrain.fit(X_train, yrain_train)

    accuracy_temp = braintemp.score(X_test, ytemp_test)
    accuracy_rain = brainrain.score(X_test, yrain_test)
    
    stream.success(f"Temperature Model ($R^2$ Score): {accuracy_temp:.4f}")
    stream.success(f"Rainfall Model Accuracy: {accuracy_rain:.2%}")

    with open('temperature_model.pkl', 'wb') as file:
        pickle.dump(braintemp, file)
    
    with open('rainfall_model.pkl', 'wb') as file:
        pickle.dump(brainrain, file)
    
    return braintemp, brainrain

def loadingmodel():
    try:
        with open('temperature_model.pkl', 'rb') as file:
            braintemp = pickle.load(file)
        with open('rainfall_model.pkl', 'rb') as file:
            brainrain = pickle.load(file)
    except FileNotFoundError:
        braintemp, brainrain = train_save_model()
    return braintemp, brainrain

def main():
    braintemp, brainrain = loadingmodel()

    stream.title("Weather Prediction Model Testing Interface")
    stream.write("### Input Month and Humidity to predict Temperature and Rainfall:")
    month = stream.number_input("Month (1-12)", min_value=1, max_value=12, value=6)
    humidity = stream.number_input("Humidity (%)", min_value=0, max_value=100, value=70)    

    if stream.button("Test Weather Model"):
        new_data = pd.DataFrame([[month, humidity]], columns=['Month', 'Humidity'])
        
        temp_prediction = braintemp.predict(new_data)
        rain_prediction = brainrain.predict(new_data)

        rpredict = {0: "No Rain", 1: "Rain"}

        stream.info(f"Predicted Temperature: {temp_prediction[0]:.2f}°C")
        stream.info(f"Rainfall Forecast: {rpredict[rain_prediction[0]]}")

if __name__ == "__main__":
    main()