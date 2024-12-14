
import streamlit as st
from streamlit_option_menu import option_menu


# function begin code

def calculate_bmi(weight, height):
    return (weight) / ((height/100) ** 2)  # Ubah Ke cm!


def calculate_body(waist, height):
    return waist/(height)


def calculate_fat(weight, height, umur):
    return 1.2*((weight) / ((height/100) ** 2))+(0.23*umur) - 16.2


def calculate_fatp(weight, height, umur):
    return 1.2*((weight) / ((height/100) ** 2))+(0.23*umur) - 5.4


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


def display_body_result(waistratio):
    if waistratio < 0.42:
        st.write("KESIMPULAN: Underweight")
    elif 0.43 <= waistratio < 0.52:
        st.write("KESIMPULAN: Normal")
    elif 0.53 <= waistratio < 0.62:
        st.write("KESIMPULAN: Overweight")
    else:
        st.write("KESIMPULAN: Obesity")


def display_fat_result(fat, Tombol):
    if Tombol == "Laki":
        if 2 <= fat < 6:
            st.write("KESIMPULAN: Essential Fat")
        elif 6 <= fat < 14:
            st.write("KESIMPULAN: Athletes")
        elif 14 <= fat < 18:
            st.write("KESIMPULAN: Fitness")
        elif 18 <= fat < 25:
            st.write("KESIMPULAN: Normal weight")
        elif fat > 24:
            st.write("KESIMPULAN: Obesity")
    elif Tombol == "Perempuan":
        if 10 <= fat < 14:
            st.write("KESIMPULAN: Essential Fat")
        elif 14 <= fat < 21:
            st.write("KESIMPULAN: Athletes")
        elif 21 <= fat < 25:
            st.write("KESIMPULAN: Fitness")
        elif 25 <= fat <= 31:
            st.write("KESIMPULAN: Normal weight")
        elif fat > 32:
            st.write("KESIMPULAN: Obesity")


# function end code


st.title("BMI")


# app
def main():
    st.subheader("Kalkulator Kesehatan!")

    # navigasi
    selected = option_menu(
        menu_title=None,
        options=["BMI", "waist to Height Ratio", "Body Fat"],
        icons=["star", "ruler", "percent"],
        menu_icon="cast",
        default_index=0,
        orientation="horizontal",
    )

    if selected == "BMI":  # bmi
        st.header("BMI Calculator")
        weight = st.number_input(
            "Berat Badan (kg)", min_value=0.0, format="%.2f", key="<weight>")
        height = st.number_input(
            "Tinggi (cm)", min_value=0.0, format="%.2f", key="<height>")
        if st.button("HITUNG!"):
            if weight > 0 and height > 0:
                bmi = calculate_bmi(weight, height)
                st.write(f"Your BMI is: {bmi:.2f}")
                display_bmi_result(bmi)
            else:
                st.write("Please enter valid weight and height.")

    elif selected == "waist to Height Ratio":  # waist height
        st.header("waist to Height Ratio Calculator")
        waist = st.number_input(
            "Lebar Pinggang (cm)", min_value=0.0, format="%.2f", key="<waist>")
        height = st.number_input(
            "Tinggi (cm)", min_value=0.0, format="%.2f", key="<height>")
        if st.button("HITUNG!"):
            if waist > 0 and height > 0:
                waistratio = calculate_body(waist, height)
                st.write(
                    f"Rasio waist/height anda adalah: {waistratio:.2f}")
                display_body_result(waistratio)
            else:
                st.write("Angka tidak valid!")

    elif selected == "Body Fat":  # select body fat
        st.header("Body Fat Calculator")
        weight = st.number_input(
            "Berat Badan (kg)", min_value=0.0, format="%.2f", key="<weight>")
        height = st.number_input(
            "Tinggi (cm)", min_value=0.0, format="%.2f", key="<height>")
        umur = st.number_input("Umur (Tahun)", min_value=0,  key="<umur>")
        gender = ["Laki", "Perempuan"]
        tombol = st.radio("Gender?", gender, key="<Gender>")

        if st.button("HITUNG!"):
            if tombol == "Laki":
                if weight > 0 and height > 0 and umur > 0:
                    fat = calculate_fat(weight, height, umur)
                    st.write(f"Persentase Body fat anda adalah: {fat:.2f}")
                    display_fat_result(fat, tombol)
                    st.write(
                        f"Details: The body fat percentage is {fat:.2f}%.")
                else:
                    st.write("Angka tidak valid!")
            if tombol == "Perempuan":
                if weight > 0 and height > 0 and umur > 0:
                    fat = calculate_fatp(weight, height, umur)
                    st.write(f"Persentase Body fat anda adalah: {fat:.2f}")
                    display_fat_result(fat, tombol)
                else:
                    st.write("Angka tidak valid!")


if __name__ == "__main__":
    main()
