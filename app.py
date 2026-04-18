import streamlit as st

st.title("BMI Calculator")
st.subheader("For your BMI needs")

unit_select = st.radio("Choose your units: ", ["Metric", "Imperial"]) # button to select imperial or metric


if unit_select == "Metric":
    
    height = st.number_input("Enter your height in centimeters: ", min_value = 0.1, step = 0.1)
    #height_slider = st.slider("Pick a value between 0 and 250 cms")

    weight = st.number_input("Enter your weight in kilograms: ", min_value = 0.1, step = 0.1)
    #weight_slider = st.slider("Pick a weight between 0 and 250 kgs")
    
else:
    
    height_imp = st.number_input("Enter your height in inches: ", min_value = 0.1, step = 0.1)
    weight_imp = st.number_input("Enter your weight in lbs: ", min_value = 0.1, step = 0.1)



    

# metric calculation


if st.button("Calculate BMI"):
    
    if unit_select == "Metric":
    
        height_cms = height/100
        bmi = weight / (height_cms**2)
        
        st.write(f"Your bmi is: {bmi:.1f}")

        if bmi < 18.5:
            st.warning("You are underweight")
            
        elif bmi < 25:
            st.success("You are a healthy weight")
            
        elif bmi < 30:
            st.warning("You are overweight")

        else:
            st.warning("You are obese")
            
    elif unit_select == "Imperial":  # imperial 
        

        height_isq = height_imp**2
        bmi = weight_imp / (height_isq)*703

        st.write(f"Your bmi is {bmi:.1f}")
        
        if bmi < 18.5:
            st.warning("You are underweight")
            
        elif bmi < 25:
            st.success("You are a healthy weight")
            
        elif bmi < 30:
            st.warning("You are overweight")

        else:
            st.warning("You are obese")

        
        

        

    
    
        
        