"""
# metric calculation
if st.button("Calculate BMI"):
    
    if unit == "Metric":
    
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
            
    elif unit_select == "Imperial":  # imperial calculation
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

# optional bf % calculation


bf_known = st.checkbox("I know my bf percentage")
bf_unknown = st.checkbox("I don't know my body fat percentage")
if bf_known:
    if bmi > 30 and bf
"""

  