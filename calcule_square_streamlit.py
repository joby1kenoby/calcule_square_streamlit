

import streamlit as st 

st.title("Calculate the surface of square/rectangle")
st.write ("Enter your dimensions below to calculate the surface of a square or rectangle.")

#Create input fields


length = input(st.number1("Enter the length in (m) : ", min_value=0.0))
width = input(st.number2("Enter the width in (m) : ", min_value=0.0))

# calculate button

if st.button("Calculate"):
    
    surface = length * width
    st.success(f"The surface of the area is: **{surface}**")


#st.write('Hello World!')







