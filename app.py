import streamlit as st

st.title("BMI Calculator")
st.subheader("For your BMI needs")

height = st.number_input("Enter your height in centimeters: ", min_value = 0.1, step = 0.1)
#height_slider = st.slider("Pick a value between 0 and 250 cms")

weight = st.number_input("Enter your weight in kilograms: ", min_value = 0.1, step = 0.1)
#weight_slider = st.slider("Pick a weight between 0 and 250 kgs")


if st.button("Calculate BMI"):
    height_cms = height/100
    bmi = weight/ (height_cms**2)
    
    st.write(f"Your bmi is: {bmi:.1f}")

    if bmi < 18.5:
        st.warning("You are underweight")
        
    elif bmi > 18.5 and bmi <= 24.9:
        st.success("You are a healthy weight")
        
    elif bmi >= 25 and bmi <= 29.9:
        st.info("You are overweight")

    else:
        st.info("You are obese")
        
        