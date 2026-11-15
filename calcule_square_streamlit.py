

import streamlit as st 

st.title("Calculate the surface of square/rectangle")
st.write ("Enter your dimensions below to calculate the surface of a square or rectangle.")

#Create input fields


length = st.number1_input("Enter the length in (m) : ", min_value=0.0)
width = st.number2_input("Enter the width in (m) : ", min_value=0.0)

# calculate button
if st.button("Calculate"):
    
    surface = length * width
    st.success(f"The surface of the square/rectangle is: **{surface}**")








