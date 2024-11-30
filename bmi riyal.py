import streamlit as st #ini tempat naro kode (biar copas)
from streamlit_option_menu import option_menu

# Function to calculate BMI
def calculate_bmi(weight, height):
    return weight / (height / 100) ** 2

# Function to display BMI result
def display_bmi_result(bmi):
    if bmi < 18.5:
        st.write("KESIMPULAN: Underweight")
    elif 18.5 <= bmi < 24.9:
        st.write("KESIMPULAN: Normal weight")
    elif 25 <= bmi < 29.9:
        st.write("KESIMPULAN: Overweight")
    else:
        st.write("KESIMPULAN: Obesity")

# Main app
def main():
    st.title("BMI Calculator")

    # Navigation menu
    selected = option_menu(
        menu_title=None,
        options=["BMI", "Waist to Height Ratio", "Body Fat"],
        icons=["star", "ruler", "percent"],
        menu_icon="cast",
        default_index=0,
        orientation="horizontal",
    )

    if selected == "BMI":
        st.header("BMI Calculator")
        weight = st.number_input("Berat Badan (kg)", min_value=0.0, format="%.2f")
        height = st.number_input("Tinggi (cm)", min_value=0.0, format="%.2f")
        age = st.number_input("Umur", min_value=0)
        gender = st.radio("Gender", ("Perempuan", "Laki-Laki"))
        if st.button("HITUNG!"):
            if weight > 0 and height > 0:
                bmi = calculate_bmi(weight, height)
                st.write(f"Your BMI is: {bmi:.2f}")
                display_bmi_result(bmi)
            else:
                st.write("Please enter valid weight and height.")

    elif selected == "Waist to Height Ratio":
        st.header("Waist to Height Ratio Calculator")
        # Add your form fields and logic here

    elif selected == "Body Fat":
        st.header("Body Fat Calculator")
        # Add your form fields and logic here

if __name__ == "__main__":
    main()
