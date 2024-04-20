import streamlit as st
import helper
import pickle

model = pickle.load(open('model.pkl','rb'))

st.header('Duplicate Question Pairs')

q1 = st.text_input('Enter question 1')
q2 = st.text_input('Enter question 2')
q3 = st.text_input('Enter question 3')

if st.button('Find'):
    queries = [helper.query_point_creator(q1, q2), 
               helper.query_point_creator(q1, q3)]
    results = [model.predict(query)[0] for query in queries]

    if all(results):
        st.header('Duplicate')
    else:
        st.header('Not Duplicate')
# end of the code