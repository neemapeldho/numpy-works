import streamlit

streamlit.title("Calculate BMI")

username = streamlit.text_input("Enter the name : ")

height = streamlit.number_input("Enter the height : ")

weight = streamlit.number_input("Enter the weight : ")

# bmi = weight / (height)**2

if streamlit.button("BMI"):

    bmi = weight / (height)**2

    streamlit.success(bmi)



