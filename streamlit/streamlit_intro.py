import streamlit

streamlit.title("streamlit works")

# streamlit run streamlit_intro.py

streamlit.header("Machine Learning")

streamlit.subheader("streamlit used to convert python and ml into a web application")

name = streamlit.text_input("Enter your name : ") # take input from browser

print(name)       # result on console

streamlit.button("Say Hello")

streamlit.success(f" Hello {name}") # result need to show on browser

#=========================================

streamlit.subheader("Add two numbers")

number1 = streamlit.text_input("enter the first number : ")

number2 = streamlit.text_input("enter the second number : ")

if streamlit.button("Add"):

    result = int(number1) + int(number2)

    streamlit.success(f"{result}")

if streamlit.button("Sub"):

    result = int(number1) - int(number2)

    streamlit.success(f"{result}")

 

