import streamlit as st

#1. Title
st.title("BMI Calculator")
st.write("enter your details to calculate your BMI")

#2. get input from user
weight = st.number_input("Enter your weight in kg:", min_value=0.0, step=0.1)
height = st.number_input("Enter your height in meters:", min_value=0.0, step=0.01)

#3. button to calculate BMI
if st.button("Calculate BMI"):
    if weight > 0 and height > 0:
        bmi = weight / (height ** 2)
        st.write(f"Your BMI is: {bmi:.2f}")
    else:
        st.write("Please enter valid weight and height values.")

#4. give a message based on BMI value
    if bmi < 18.5:
        st.warning("You are underweight. Consider consulting a healthcare professional.")   
    elif bmi < 25:
        st.success("You have a healthy weight.")   
    else:
        st.error("You are overweight. Consider consulting a healthcare professional.")   