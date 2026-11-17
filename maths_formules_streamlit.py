

import streamlit as st 

st.title("Calculate the surface of square/rectangle")
st.write ("Enter your dimensions below to calculate the surface of a square or rectangle.")

#Create input fields


length = st.number_input("Enter the length in (m) : ", min_value=0.0)
width = st.number_input("Enter the width in (m) : ", min_value=0.0)

# calculate button

if st.button("Calculate"):
    
    surface = length * width
    st.success(f"The surface of the area is: **{surface}** (m²)")



# 1.2 Calculate the perimeter of square/rectangle#

st.title("The perimeter of square/rectangle")
st.write(" Enter your dimensions below to calculate the perimeter of a square or rectangle.")



length = st.number_input("Enter the length in (m) : ", min_value=0.0)
width = st.number_input("Enter the width in (m) : ", min_value=0.0)

perimeter = (length + width) * 2

st.success(f"The perimeter of the area is: **(perimeter)** (m)")




