import streamlit as st
from data_ranges import bmi_ranges, body_fat_male, body_fat_female

def get_category(value, category_dict):
    for (low, high), label in category_dict.items(): 
        if low <= value <= high:
            return label
    return "Unknown"

    """  
    # parses each dictionary item 
    # each key is a tuple item (0, 18.4)
    # each value is a string category ex. "Overweight"
    # the tuple is unpacked into 'low', 'high'
    """
def get_display_type(category, styles):
    return styles.get(category, st.info) # find the function for that category, if that doesn't exist use st.info

display_types = {
    "Underweight": st.warning,
    "Healthy Weight": st.success,
    "Overweight": st.warning,
    "Obese Class I": st.error,
    "Obese Class II": st.error,
    "Obese Class III": st.error    
}

st.title("BMI Calculator")
st.subheader("For your BMI needs")

unit = st.radio("Choose your units: ", ["Metric", "Imperial"]) # button to select imperial or metric

bf_known = st.checkbox("I know my body fat %")
if bf_known:
    sex = st.radio("What is your sex: ", ['Male', "Female"])
    bf = st.number_input("Write your body fat %: ", min_value = 0.1, step = 0.1)   

if unit == "Metric":
    height = st.number_input("Height (cm): ", min_value = 0.1, step = 0.1)
    weight = st.number_input("Weight (kg): ", min_value = 0.1, step = 0.1)
    
else:
    height_imp = st.number_input("Height (inches): ", min_value = 0.1, step = 0.1)
    weight_imp = st.number_input("Weight (lbs): ", min_value = 0.1, step = 0.1)
    
if st.button("Calculate BMI"):
    
    # --- Calculate BMI ---
    if unit == "Metric":
        height_metres = height/100
        bmi = weight / height_metres**2
    else:
        bmi = (weight_imp/(height_imp**2)) * 703
    st.write(f"Your bmi is: {bmi:.1f}")
    
    bmi_category = get_category(bmi, bmi_ranges)
    bmi_display_fn = display_types.get(bmi_category, st.info)
    bmi_display_fn(f"BMI Category: {bmi_category}")
    
    #optional bf section  
    if bf_known:
        if sex == "Male":
            bf_dict = body_fat_male
        else:
            bf_dict = body_fat_female
            
        bf_category = get_category(bf, bf_dict) # classifying a number into a category based on the correct dictionary
        bf_display_fn = display_types.get(bf_category, st.info) #default to info if display type not gotten -> getting "regular 
        bf_display_fn(f"Body Fat Category: {bf_category}")
        
            
            
    






    
    
    

    
        
    

