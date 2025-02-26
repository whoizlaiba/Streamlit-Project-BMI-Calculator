import streamlit as st
from PIL import Image

st.title("This is My BMI Calculator")

image_path = "bmi.png"  


image = Image.open(image_path)


st.image(image)


weight = st.number_input("Enter your Weight in KG", step=0.1)
height = st.number_input("Enter your Height in Meters")


if height > 0:
    bmi = weight / (height ** 2)
    st.success(f"🎉Your BMI is {bmi:.2f}")
else:
    st.error("🧨Height must be greater than 0")
