

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



l1 = st.number_input("Enter the l1 in (m) : ", min_value=0.0)
l2 = st.number_input("Enter the l2 in (m) : ", min_value=0.0)

if st.button("Calculation"):
        
    perimeter = (l1 + l2) * 2
    st.success(f"The perimeter of the area is: **{perimeter}** (m)")
    


# 2 Calculate the surface of triangle#

st.title("Calculate the surface of triangle")
st.write("Enter your base(dimension) and height below to calculate the surface of a triangle.")

lb = st.number_input("Enter the base in (m) :", min_value=0.0)
lh = st.number_input("Enter the height in (m) :", min_value=0.0)

if st.button("Calculate"):
    
    surface_2 = (lb * lh) / 2
    st.success(f"The surface of the triangle is: **{surface_2}** (m²)")
# hight = float(input("Enter the hight in (m) : "))

# surface = (base * hight) / 2

# print("The surface is equal to : ", surface, "m²")




