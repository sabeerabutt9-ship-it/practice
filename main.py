import streamlit as st
import PIL.Image as Image

st.title("Sabeera")
st.header("about me")


upload_file = Image.open("img.jpeg")

st.image(upload_file, caption='ME', width=250)
st.success("image upload succesfully")

st.text("i am 26 years old ")
st.text("i am a student")
st.text("i like programing")
st.success("Welcome to my first Streamlit app")