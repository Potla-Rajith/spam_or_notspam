import string
import streamlit as st
import nltk
import pandas as pd
import pickle
from nltk.corpus import stopwords
nltk.download('stopwords')

# Load the trained model and vectorizer
my_scaler = pickle.load(open("spam_model.pkl", "rb"))
tfidf = pickle.load(open('message_tfid.pkl', "rb"))
stop_words = set(stopwords.words('english'))

# Text preprocessing function
def message_text_process(mess):
    no_punctuation = ''.join(char for char in mess if char not in string.punctuation)
    return ' '.join([word for word in no_punctuation.split() if word.lower() not in stop_words])

# Streamlit app UI
st.title('Email Spam Classifier')
input_sms = st.text_area('Enter a message')
option = st.selectbox('You got message from:', ['Mail', 'SMS', 'Others'])

#if st.checkbox('Check Me'):
   # st.write("Nothing, please enter another sentence")

if st.button('Click to predict'):
    processed_sms = message_text_process(input_sms)
    vector_input = tfidf.transform([processed_sms])
    vector_input_dense = vector_input.toarray()
    result = my_scaler.predict(vector_input_dense)[0]

    if result == 1:
        st.header('Spam')
    else:
        st.header('Not Spam')
