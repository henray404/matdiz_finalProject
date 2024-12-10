import streamlit as st
from random import shuffle

# Initialize session state for lists
if "name_list" not in st.session_state:
    st.session_state.name_list = {"name": [], "ranking": []}

if "current_round" not in st.session_state:
    st.session_state.current_round = []

# Judul aplikasi
st.title("Bracket Generator")

# Subheader untuk input data
st.subheader("Masukkan Data Kompetitor")
option = st.selectbox(
    'Pilih jenis kompetitor:',
    ('Individu', 'Tim')
)

# Form untuk input data kompetitor
with st.form("competitor_form"):
    if option == 'Individu':
        col1, col2 = st.columns(2)
        with col1:
            name = st.text_input(
                "Nama Kompetitor", placeholder="Nama kompetitor")
        with col2:
            rating = st.number_input("Rating", min_value=0, step=1)
        button_name = 'Tambahkan kompetitor'
    elif option == 'Tim':
        col1, col2 = st.columns(2)
        with col1:
            team = st.text_input("Nama Tim", placeholder="Nama Tim")
        with col2:
            rating = st.number_input("Rating", min_value=0, step=1)
        button_name = 'Tambahkan tim'

    # Tombol untuk menambahkan kompetitor
    submitted = st.form_submit_button(f"{button_name}")
    if submitted:
        if option == 'Individu' and name.strip() and rating > 0:
            # Append to session state
            st.session_state.name_list["name"].append(name.strip())
            st.session_state.name_list["ranking"].append(rating)
            st.success(f"Kompetitor {name} berhasil ditambahkan!")
        elif option == 'Tim' and team.strip() and rating > 0:
            # Placeholder for team feature
            st.warning("Fitur tim belum diimplementasikan.")
        else:
            st.warning("Mohon isi data dengan benar.")

# Menampilkan daftar kompetitor yang sudah diinput
if st.session_state.name_list["name"]:
    st.subheader("Daftar Kompetitor")
    for idx, (name, rating) in enumerate(
        zip(st.session_state.name_list["name"],
            st.session_state.name_list["ranking"]),
        start=1,
    ):
        st.write(f"{idx}. Nama: {name}, Rating: {rating}")
else:
    st.info("Belum ada kompetitor yang ditambahkan.")

# Fitur pembuatan pasangan acak
st.subheader("Pasangkan Kompetitor")
if st.button("Buat Bracket Acak"):
    if len(st.session_state.name_list["name"]) < 2:
        st.warning("Minimal dua kompetitor diperlukan untuk membuat ronde.")
    else:
        # Reset current_round
        st.session_state.current_round = []
        competitors = list(
            zip(st.session_state.name_list["name"],
                st.session_state.name_list["ranking"])
        )
        shuffle(competitors)  # Acak daftar kompetitor

        # Jika jumlah kompetitor ganjil, tambahkan "Bye"
        if len(competitors) % 2 != 0:
            competitors.append(("Bye", 0))

        st.session_state.current_round = competitors

# Tampilkan ronde acak
if st.session_state.current_round:
    st.subheader("Hasil Acak")
    for i in range(0, len(st.session_state.current_round), 2):
        c1, c2 = st.session_state.current_round[i], st.session_state.current_round[i + 1]
        st.write(f"{c1[0]} (Rating: {c1[1]}) vs {c2[0]} (Rating: {c2[1]})")
