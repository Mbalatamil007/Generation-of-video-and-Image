import streamlit as st

st.title("My First Streamlit App")
st.write("Hello, welcome to my first Streamlit app!")


name = st.text_input("Enter your name:")
st.write(f"Hello, {name}!") if name else st.write("Please enter your name above.")

age = st.number_input("Enter your age:", min_value=0, max_value=120, step=1)
if age:
        st.write(f"You are {age} years old.")

if st.button("Submit"):
    st.write(f"Thank you, {name}, for submitting your information!")

number = st.slider("Select a number:", min_value=0, max_value=100, step=1)
st.write(f"You selected the number: {number}")

city = st.selectbox("Select your city:", ["New York", "Los Angeles", "Chicago", "Houston", "Phoenix"])
st.write(f"You selected: {city}")

agree = st.checkbox("I agree to the terms and conditions")
if agree:
    st.write("Thank you for agreeing to the terms and conditions.") 

st.success("This is a success message!")
st.info("This is an info message.") 
st.warning("This is a warning message.")
st.error("This is an error message!")