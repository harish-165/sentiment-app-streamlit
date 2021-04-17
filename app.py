import streamlit as st
import joblib
model =joblib.load('Project_Data')
st.title("""  Sentiment Analysis""")
st.write(""" # **Sentiment** Prediction App """)
st.write(" #Predicts the Sentiment of the sentence-Positive,Negative and Neutral")
ip = st.text_input('Enter your message')
op = model.predict([ip])
if st.button('predict'):
  st.title(op[0])