
import streamlit as st
from streamlit_option_menu import option_menu


def calculate_bmi(weight, height):
    return weight / (height / 100) ** 2


def calculate_body(weight, height):
    return weight/height


def calculate_fat(weight, height, umur):
    return 1.2*(weight / (height / 100) ** 2)+0.23*umur - 16.2


def calculate_fatp(weight, height, umur):
    return 1.2*(weight / (height / 100) ** 2)+0.23*umur - 5.4


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


st.title("BMI")


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

    elif selected == "weight to Height Ratio":
        st.header("weight to Height Ratio Calculator")
        weight = st.number_input(
            "Lebar Pinggang (cm)", min_value=0.0, format="%.2f", key="<waist>")
        height = st.number_input(
            "Tinggi (cm)", min_value=0.0, format="%.2f", key="<height>")
        if st.button("HITUNG!"):
            if weight > 0 and height > 0:
                weightratio = calculate_body(weight, height)
                st.write(
                    f"Rasio weight/height anda adalah: {weightratio:.2f}")
                display_body_result(weightratio)
            else:
                st.write("Angka tidak valid!")

    elif selected == "Body Fat":
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
                    display_fat_result(fat)

                    with st.expander(f"Body Fat Result: {fat:.2f}%"):
                        # Displaying an image inside the expander
                        st.image("data:image/png;base64,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",
                                 caption="Body Fat Analysis Image")
                        st.write(
                            f"Details: The body fat percentage is {fat:.2f}%.")

                else:
                    st.write("Angka tidak valid!")
            if tombol == "Perempuan":
                if weight > 0 and height > 0 and umur > 0:
                    fat = calculate_fatp(weight, height, umur)
                    st.write(f"Persentase Body fat anda adalah: {fat:.2f}")
                    display_fat_result(fat)
                else:
                    st.write("Angka tidak valid!")


if __name__ == "__main__":
    main()
