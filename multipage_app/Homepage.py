import streamlit as st
st.set_page_config(
    page_title="FP Matdis",
    page_icon="😜",
)
st.title("Halaman Utama")
st.sidebar.success("Cap cip cup")


st.markdown("""
    <style>
    .rounded-img {
        border-radius: 50%;
        width: 100%;
        height: 100%;
    }
    </style>
""", unsafe_allow_html=True)


# Custom CSS for styling
st.markdown("""
    <style>
        .header {
            display: flex;
            justify-content: space-between;
            align-items: center;
            padding: 16px;
        }
        .header .title {
            font-size: 1.25rem;
            font-weight: bold;
        }
        .header nav a {
            margin-right: 16px;
            color: #4A5568;
            text-decoration: none;
        }
        .header nav button {
            background-color: #000;
            color: #fff;
            padding: 8px 16px;
            border-radius: 4px;
            border: none;
        }
        .section {
            margin-bottom: 48px;
        }
        .section h1, .section h2 {
            font-weight: bold;
        }
        .section p {
            color: #4A5568;
            line-height: 1.75;
        }
        .project-choice {
            display: flex;
            gap: 32px;
        }
        .project-choice div {
            background-color: #F7FAFC;
            padding: 16px;
            border-radius: 8px;
            text-align: center;
            flex: 1;
        }
        .project-choice img {
            margin: 0 auto 16px;
        }
        .team {
            display: flex;
            flex-direction: column;
            gap: 32px;
        }
        .team div {
            display: flex;
            align-items: center;
            gap: 16px;
        }
        .team img {
            width: 96px;
            height: 96px;
            border-radius: 50%;
        }
        .footer {
            background-color: #F7FAFC;
            padding: 32px;
            margin-top: 48px;
        }
        .footer .footer-content {
            display: flex;
            justify-content: space-between;
            align-items: center;
            margin-bottom: 32px;
        }
        .footer .footer-content div {
            font-weight: bold;
        }
        .footer .footer-content a {
            color: #4A5568;
            margin-right: 16px;
        }
        .footer .footer-links {
            display: flex;
            justify-content: space-between;
        }
        .footer .footer-links div {
            font-weight: bold;
        }
    </style>
""", unsafe_allow_html=True)

# Header
st.markdown("""
    <div class="header">
        <div class="title">FP MATDIS</div>
        <nav>
            <a href="#">What is?</a>
            <a href="#">Our Team</a>
            <button>Next</button>
        </nav>
    </div>
""", unsafe_allow_html=True)

# Main content

# Main content
st.markdown("""
    <div class="section">
        <h1>About Our Final Project</h1>
        <p>Pada final project matematika diskrit kali ini kami membuat sebuah program untuk menghitung body mass index dan membuat sistem bracket. Hal ini kami lakukan karena kami merasa kedua hal tersebut banyak di temui di kehidupan sehari-hari. Jadi kami sangat berharap final project kali ini dapat dipergunakan dalam dunia nyata dan semoga dengan project ini kami dapat mengembangkan kemampuan kami lebih jauh lagi.</p>
    </div>
""", unsafe_allow_html=True)

# Using st.columns to arrange the project choices side by side
col1, col2 = st.columns(2)

with col1:
    st.image("https://storage.googleapis.com/a1aa/image/O5ATwXKjBFbdOtPlS8tO9xeQapVmhPOqnjFHc4y4MKtt2v6JA.jpg",
             caption="Colorful BMI meter", width=200)
    st.markdown("<p class='font-bold'>BODY MASS INDEX (BMI)</p>",
                unsafe_allow_html=True)

with col2:
    st.image("https://storage.googleapis.com/a1aa/image/gmoUsZ8E3Jb1H1tlQrfEzmfMg4mVSVEgc4OFdC8YFUZgtfqnA.jpg",
             caption="Bracket system with a trophy", width=200)
    st.markdown("<p class='font-bold'>BRACKET SYSTEM</p>",
                unsafe_allow_html=True)

# What is BMI
st.markdown("""
    <div class="section">
        <h2>What is BMI?</h2>
        <p>BMI (Body Mass Index) adalah pengukuran sederhana untuk menilai status berat badan seseorang berdasarkan berat badan (kg) dan tinggi badan (m) kuadrat. Indeks ini digunakan untuk mengkategorikan seseorang ke dalam status seperti kurus, normal, atau obesitas.</p>
    </div>
""", unsafe_allow_html=True)

# What is Bracket System
st.markdown("""
    <div class="section">
        <h2>What is Bracket System?</h2>
        <p>Sistem bracket adalah format kompetisi di mana peserta diatur dalam struktur seperti pohon. Pemenang melanjutkan ke babak berikutnya hingga diperoleh pemenang akhir.</p>
    </div>
""", unsafe_allow_html=True)

# Team Section with images
st.markdown("""
    <div class="section">
        <h2>Meet the team</h2>
    </div>
""", unsafe_allow_html=True)

# Using st.columns for team members side by side
col1, col2, col3 = st.columns(3)


with col1:
    st.image("gmbr/vito.jpg", caption="5054241046",
             width=180, clamp=True)
    st.markdown("<p class='font-bold'>Arvito Rajapandya Natlysandro</p>",
                unsafe_allow_html=True)

with col2:

    st.image("gmbr/henry.jpg", caption="5054241024 ",
             width=200, clamp=True)
    st.markdown("<p class='font-bold'>Mochammad Henry Alifian</p>",
                unsafe_allow_html=True)

with col3:
    st.image("gmbr/ajip.jpg", caption='5054241024',
             width=200, clamp=True)
    st.markdown("<p class='font-bold'>Nazhif Berlian Nashrullah</p>",
                unsafe_allow_html=True)
