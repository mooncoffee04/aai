import streamlit as st
st.title("hii!")
st.subheader("i hope you're doing good!")

# Take input
name = st.text_input("your good name ~")
# display the input
st.write("Hello",name)

# takes math marks as input in the slidebar and display it with name of student
maths = st.slider("Enter your math marks",0,100)
st.write(name, "Scored", maths, 'marks in maths')

# Give radio button to choose either options
exam = st.radio('Choose an exam', ['GRE','GMAT'])
st.write('You Chose',exam)

subjects = st.multiselect(
    'Choose your subjects', ['Maths','Physics','Chemistry','Biology'])
st.write('You chose', subjects)

import pandas as pd
uploaded_file = st.file_uploader("Choose a filer", type = 'csv')

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    st.dataframe(df)

    