

import streamlit as st 

st.title("1 Calculate the surface of square/rectangle")
st.write ("Enter your dimensions below to calculate the surface of a square or rectangle.")

#Create input fields


length = st.float_number_input("Enter the length in (m) : ", min_value=0.0)
width = st.float_number_input("Enter the width in (m) : ", min_value=0.0)

# calculate button
if st.button("Calculate"):
    
    surface = length * width
    st.success("The surface is equal to : ", surface, "m²")








