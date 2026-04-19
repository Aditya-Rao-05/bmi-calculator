import streamlit as st
from data_ranges import bmi_ranges, body_fat_men, body_fat_women

st.title("BMI Calculator")
st.subheader("For your BMI needs")

unit = st.radio("Choose your units: ", ["Metric", "Imperial"]) # button to select imperial or metric


if unit == "Metric":
    height = st.number_input("Height (cm): ", min_value = 0.1, step = 0.1)
    weight = st.number_input("Weight (kg): ", min_value = 0.1, step = 0.1)
    
else:
    height_imp = st.number_input("Height (inches): ", min_value = 0.1, step = 0.1)
    weight_imp = st.number_input("Weight (lbs): ", min_value = 0.1, step = 0.1)
    
    
def get_category(value, category_dict):
    for (low, high), label in category_dict.items(): # parses and splits the brackets (ranges of bmis) and also the associated label
        if low <= value <= high:
            return label
    return "Unknown"


if st.button("Calculate BMI"):
    if unit == "Metric":
        height_metres = height/100
        height_sq = height_metres**2
        bmi = weight / height_sq 
    else:
        height_sq = height_imp**2
        bmi = (weight_imp/(height_sq)) * 703
        
    st.write(f"Your BMI is: {bmi:.1f}")
    
    bmi_category = get_category(bmi, bmi_ranges)
    
    if bmi_category == "Healthy Weight":
        st.success(bmi_category)
    else:
        st.warning(bmi_category)
    
    
    
    
    
    
    
        
    

