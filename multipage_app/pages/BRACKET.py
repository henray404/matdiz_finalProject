import streamlit as st

# session state
if "name_list" not in st.session_state:
    st.session_state.name_list = {"name": [], "rating": []}

if "team_list" not in st.session_state:
    st.session_state.team_list = {"team": [], "rating": []}

if "current_round" not in st.session_state:
    st.session_state.current_round = []

# Merge sort function


def merge_sort(competitors):
    if len(competitors) > 1:
        mid = len(competitors) // 2
        left_half = competitors[:mid]
        right_half = competitors[mid:]

        merge_sort(left_half)
        merge_sort(right_half)

        i = j = k = 0
        while i < len(left_half) and j < len(right_half):
            # Sort by rating (descending)
            if left_half[i][1] >= right_half[j][1]:
                competitors[k] = left_half[i]
                i += 1
            else:
                competitors[k] = right_half[j]
                j += 1
            k += 1

        while i < len(left_half):
            competitors[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            competitors[k] = right_half[j]
            j += 1
            k += 1


st.title("Bracket Generator")

# Input data
st.subheader("Masukkan Data Kompetitor")
option = st.selectbox(
    'Pilih jenis kompetitor:',
    ('Individu', 'Tim')
)

# form
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

    # tambah orang
    submitted = st.form_submit_button(f"{button_name}")
    if submitted:
        if option == 'Individu' and name.strip() and rating > 0:
            st.session_state.name_list["name"].append(name.strip())
            st.session_state.name_list["rating"].append(rating)
            st.success(f"Kompetitor {name} berhasil ditambahkan!")
        elif option == 'Tim' and team.strip() and rating > 0:
            st.session_state.team_list["team"].append(team.strip())
            st.session_state.team_list["rating"].append(rating)
            st.success(f"Tim {team} berhasil ditambahkan!")
        else:
            st.warning("Mohon isi data dengan benar.")

# Nama tim
if st.session_state.name_list["name"] or st.session_state.team_list["team"]:
    st.subheader("Daftar Kompetitor")
    for idx, (name, rating) in enumerate(
        zip(st.session_state.name_list["name"],
            st.session_state.name_list["rating"]),
        start=1,
    ):
        st.write(f"{idx}. Nama: {name}, Rating: {rating}")

    st.subheader("Daftar Tim")
    for idx, (team, rating) in enumerate(
        zip(st.session_state.team_list["team"],
            st.session_state.team_list["rating"]),
        start=1,
    ):
        st.write(f"{idx}. Nama Tim: {team}, Rating: {rating}")
else:
    st.info("Belum ada kompetitor atau tim yang ditambahkan.")

# Bracket generation
st.subheader("Pasangkan Kompetitor")
if st.button("Buat Bracket Berdasarkan Rating"):
    combined_list = list(
        zip(st.session_state.name_list["name"],
            st.session_state.name_list["rating"])
    ) + list(
        zip(st.session_state.team_list["team"],
            st.session_state.team_list["rating"])
    )

    if len(combined_list) < 2:
        st.warning(
            "Minimal dua peserta (kompetitor atau tim) diperlukan untuk membuat ronde.")
    else:
        st.session_state.current_round = []

        # bagian dari merge sort
        merge_sort(combined_list)

        if len(combined_list) % 2 != 0:
            combined_list.append(("Bye", 0))

        high = combined_list[:len(combined_list)//2]
        low = combined_list[len(combined_list)//2:]
        low.reverse()

        st.session_state.current_round = list(zip(high, low))


if st.session_state.current_round:
    st.subheader("Hasil Pasangan")
    for pair in st.session_state.current_round:
        c1, c2 = pair
        st.write(f"{c1[0]} (Rating: {c1[1]}) vs {c2[0]} (Rating: {c2[1]})")
