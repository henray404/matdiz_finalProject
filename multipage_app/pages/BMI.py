import streamlit as st
from streamlit_option_menu import option_menu
 #ini biar ada update
st.title("BMI")


def calculate_bmi(weight, height):
    return weight / (height / 100) ** 2
def calculate_body(weight, height):
    return weight/height
def calculate_fat(weight, height,umur):
    return 1.2*(weight / (height / 100) ** 2)+0.23*umur -16.2
def calculate_fatp(weight, height,umur):
    return 1.2*(weight / (height / 100) ** 2)+0.23*umur -5.4


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
def display_body_result(weightratio):
    if weightratio < 0.42:
        st.write("KESIMPULAN: Underweight")
    elif 0.43 <= weightratio < 0.52:
        st.write("KESIMPULAN: Normal")
    elif 0.53 <= weightratio < 0.62:
        st.write("KESIMPULAN: Overweight")
    else:
        st.write("KESIMPULAN: Obesity")
def display_fat_result(fat):
    if fat < 18.5:
        st.write("KESIMPULAN: Underweight")
    elif 18.5 <= fat < 24.9:
        st.write("KESIMPULAN: Normal weight")
    elif 25 <= fat < 29.9:
        st.write("KESIMPULAN: Overweight")
    else:
        st.write("KESIMPULAN: Obesity")

# Main app
def main():
    st.subheader("Kalkulator Kesehatan!")

    # Navigation menu
    selected = option_menu(
        menu_title=None,
        options=["BMI", "weight to Height Ratio", "Body Fat"],
        icons=["star", "ruler", "percent"],
        menu_icon="cast",
        default_index=0,
        orientation="horizontal",
    )

    if selected == "BMI":
        st.header("BMI Calculator")
        weight = st.number_input("Berat Badan (kg)", min_value=0.0, format="%.2f",key = "<weight>")
        height = st.number_input("Tinggi (cm)", min_value=0.0, format="%.2f",key ="<height>")
        if st.button("HITUNG!"):
            if weight > 0 and height > 0:
                bmi = calculate_bmi(weight, height)
                st.write(f"Your BMI is: {bmi:.2f}")
                display_bmi_result(bmi)
            else:
                st.write("Please enter valid weight and height.")

    elif selected == "weight to Height Ratio":
        st.header("weight to Height Ratio Calculator")
        weight = st.number_input("Lebar Pinggang (cm)", min_value=0.0, format="%.2f", key = "<waist>")
        height = st.number_input("Tinggi (cm)", min_value=0.0, format="%.2f", key = "<height>")
        if st.button("HITUNG!"):
            if weight > 0 and height > 0:
                weightratio = calculate_body(weight, height)
                st.write(f"Rasio weight/height anda adalah: {weightratio:.2f}")
                display_body_result(weightratio)
            else:
                st.write("Angka tidak valid!")

    elif selected == "Body Fat":
        st.header("Body Fat Calculator")
        weight = st.number_input("Berat Badan (kg)", min_value=0.0, format="%.2f", key = "<weight>")
        height = st.number_input("Tinggi (cm)", min_value=0.0, format="%.2f", key = "<height>")
        umur = st.number_input("Umur (Tahun)", min_value=0,  key = "<umur>")
        gender= ["Laki","Perempuan"]
        tombol= st.radio ("Gender?", gender, key = "<Gender>")
        
        if st.button("HITUNG!"):
            if tombol =="Laki":
                if weight > 0 and height > 0 and umur > 0:
                    fat = calculate_fat(weight, height,umur)
                    st.write(f"Persentase Body fat anda adalah: {fat:.2f}")
                    display_fat_result(fat)
                else:
                    st.write("Angka tidak valid!")
            if tombol =="Perempuan":
                if weight > 0 and height > 0 and umur > 0:
                    fat = calculate_fatp(weight, height,umur)
                    st.write(f"Persentase Body fat anda adalah: {fat:.2f}")
                    display_fat_result(fat)
                else:
                    st.write("Angka tidak valid!")
            

        

if __name__ == "__main__":
    main()