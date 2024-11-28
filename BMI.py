import streamlit as st

# Set page configuration
st.set_page_config(page_title="FP MATDIS", layout="wide")

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
st.markdown("""
    <div class="section">
        <h1>About Our Final Project</h1>
        <p>Pada final project matematika diskrit kali ini kami membuat sebuah program untuk menghitung body mass index dan membuat sistem bracket. Hal ini kami lakukan karena kami merasa kedua hal tersebut banyak di temui di kehidupan sehari-hari. Jadi kami sangat berharap final project kali ini dapat dipergunakan dalam dunia nyata dan semoga dengan project ini kami dapat mengembangkan kemampuan kami lebih jauh lagi.</p>
    </div>
    <div class="section">
        <h2>Choose Final Project</h2>
        <div class="project-choice">
            <div>
                <img src="https://storage.googleapis.com/a1aa/image/O5ATwXKjBFbdOtPlS8tO9xeQapVmhPOqnjFHc4y4MKtt2v6JA.jpg" alt="Colorful BMI meter" width="200" height="200">
                <p class="font-bold">BODY MASS INDEX (BMI)</p>
            </div>
            <div>
                <img src="https://storage.googleapis.com/a1aa/image/gmoUsZ8E3Jb1H1tlQrfEzmfMg4mVSVEgc4OFdC8YFUZgtfqnA.jpg" alt="Bracket system with a trophy" width="200" height="200">
                <p class="font-bold">BRACKET SYSTEM</p>
            </div>
        </div>
    </div>
    <div class="section">
        <h2>What is BMI?</h2>
        <p>BMI (Body Mass Index) adalah pengukuran sederhana untuk menilai status berat badan seseorang berdasarkan berat badan (kg) dan tinggi badan (m) kuadrat. Indeks ini digunakan untuk mengkategorikan seseorang ke dalam status seperti kurus, normal, atau obesitas.</p>
    </div>
    <div class="section">
        <h2>What is Bracket System?</h2>
        <p>Sistem bracket adalah format kompetisi di mana peserta diatur dalam struktur seperti pohon. Pemenang melanjutkan ke babak berikutnya hingga diperoleh pemenang akhir.</p>
    </div>
    <div class="section">
        <h2>Meet the team</h2>
        <div class="team">
            <div>
                <img src="MATDIZ_FINALPROJECT/gmbr/vito.jpg" alt="Team member 1 smiling">
                <div>
                    <p class="font-bold">Anggota 1</p>
                    <p>Arvito Rajapandya Natlysandro</p>
                    <p>5054241046</p>
                    <p class="italic">“jangan lupa untuk senyum”</p>
                </div>
            </div>
            <div>
                <img src="https://storage.googleapis.com/a1aa/image/WGVYeTWWgsylQSeqCmwuYHugHbGnP9SBQmXcR9N9U10ctfqnA.jpg" alt="Team member 2 with a scenic background">
                <div>
                    <p class="font-bold">Anggota 2</p>
                    <p>Mochammad Henry Alifian</p>
                    <p>5054241024</p>
                    <p class="italic">“nahhh, imma do my own thing”</p>
                </div>
            </div>
            <div>
                <img src="https://storage.googleapis.com/a1aa/image/MM7sezguqfumd0flweD4i5vfQnXyzM4BRGEgcYYmWaQ9r9reE.jpg" alt="Team member 3 holding a 3D printed object">
                <div>
                    <p class="font-bold">Anggota 3</p>
                    <p>Nazhif Berlian Nashrullah</p>
                    <p>5054241035</p>
                    <p class="italic">“bismillah aja”</p>
                </div>
            </div>
        </div>
    </div>
""", unsafe_allow_html=True)

# Footer
st.markdown("""
    <div class="footer">
        <div class="footer-content">
            <div>
                <p class="font-bold">FINAL PROJECT</p>
                <p>MATEMATIKA DISKRITTTTT</p>
            </div>
            <div>
                <a href="#"><i class="fab fa-facebook"></i></a>
                <a href="#"><i class="fab fa-instagram"></i></a>
                <a href="#"><i class="fab fa-linkedin"></i></a>
                <a href="#"><i class="fab fa-youtube"></i></a>
            </div>
        </div>
        <div class="footer-links">
            <div>
                <p class="font-bold">Topic</p>
                <p>Page</p>
                <p>Page</p>
                <p>Page</p>
            </div>
            <div>
                <p class="font-bold">Topic</p>
                <p>Page</p>
                <p>Page</p>
                <p>Page</p>
            </div>
            <div>
                <p class="font-bold">Topic</p>
                <p>Page</p>
                <p>Page</p>
                <p>Page</p>
            </div>
        </div>
    </div>
""", unsafe_allow_html=True)
