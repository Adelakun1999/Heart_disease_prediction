import streamlit as st 
import joblib 
import pandas as pd 


st.title("Heart Disease Prediction App")
model = joblib.load('rf.pkl')

cols = {
    'age' : st.number_input('Age'),
 'sex' : st.number_input('Sex'),
'cp' : st.number_input('Chest Pain Type'),
'trestbps' : st.number_input('Resting Blood Pressure'),
 'chol' : st.number_input('Cholesterol'),
 'fbs' : st.number_input('Fasting Blood Sugar'),
 'restecg' : st.number_input('Resting ECG'),
'thalach' : st.number_input('Max Heart Rate'),
 'exang' : st.number_input('Exercise Induced Angina'),
 'oldpeak' : st.number_input('ST Depression'),
 'slope' : st.number_input('Slope of ST Segment'),
 'ca' : st.number_input('Number of Vessels Colored by Fluoroscopy'),
 'thal' : st.number_input('Thalassemia')
}

df = pd.DataFrame([cols])

#st.table(df)

if st.button('Predict', type='primary'):
    prediction = model.predict(df)
    st.success(f"The predicted result is : {prediction[0]}", icon="✅")
