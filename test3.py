import streamlit as st
import pandas as pd

# Menampilkan slide untuk pendahuluan
st.markdown(
    """
    <div style='background-color: #f0f0f0; padding: 20px; border-radius: 10px;'>
        <h2 style='color: #333333; text-align:center;'>Selamat Datang di Aplikasi Kalkulator Kalori Buah</h2>
        <p style='color: #333333; text-align:justify;'>Aplikasi ini dirancang untuk membantu Anda menghitung jumlah kalori dalam berbagai jenis buah. 
        Pilih buah favorit Anda, masukkan beratnya, dan aplikasi kami akan memberikan informasi tentang jumlah kalori serta kandungan nutrisinya. 
        Selain itu, Anda juga dapat menemukan rekomendasi buah berdasarkan jumlah kalori yang Anda inginkan.</p>
    </div>
    """,
    unsafe_allow_html=True
)


kalori_buah = {
    'apel': {
        'kalori': 52,
        'gambar': 'c:\\Users\\Bagas AL-Fikri\\Downloads\\apel.png',
        'vitamin': {'Vitamin A': '3%', 'Vitamin C': '14%'},
        'serat': '2.4g',
        'protein': '0.3g',
        'lemak': '0.2g'
    },
    'pisang': {
        'kalori': 89,
        'gambar': 'c:\\Users\\Bagas AL-Fikri\\Downloads\\pisang.png',
        'vitamin': {'Vitamin B6': '20%', 'Vitamin C': '14%'},
        'serat': '2.6g',
        'protein': '1.1g',
        'lemak': '0.3g'
    },
    'jeruk': {
        'kalori': 43,
        'gambar': 'c:\\Users\\Bagas AL-Fikri\\Downloads\\gambar jeruk.webp',
        'vitamin': {'Vitamin C': '90%'},
        'serat': '2.4g',
        'protein': '0.9g',
        'lemak': '0.2g'
    },
    'pir': {
        'kalori': 57,
        'gambar': 'c:\\Users\\Bagas AL-Fikri\\Downloads\\pir.png',
        'vitamin': {'Vitamin C': '7%'},
        'serat': '2.4g',
        'protein': '0.4g',
        'lemak': '0.2g'
    },
    'strawberry': {
        'kalori': 32,
        'gambar': 'c:\\Users\\Bagas AL-Fikri\\Downloads\\gambar strawberry.png',
        'vitamin': {'Vitamin C': '98%'},
        'serat': '2g',
        'protein': '0.7g',
        'lemak': '0.3g'
    },
    'semangka': {
        'kalori': 30,
        'gambar': 'c:\\Users\\Bagas AL-Fikri\\Downloads\\semangka.png',
        'vitamin': {'Vitamin A': '11%', 'Vitamin C': '13%'},
        'serat': '0.4g',
        'protein': '0.6g',
        'lemak': '0.2g'
    },
    'mangga': {
        'kalori': 60,
        'gambar': 'c:\\Users\\Bagas AL-Fikri\\Downloads\\gambar mangga.jpg',
        'vitamin': {'Vitamin A': '25%', 'Vitamin C': '76%'},
        'serat': '1.6g',
        'protein': '0.8g',
        'lemak': '0.4g'
    },
    'alpukat': {
        'kalori': 160,
        'gambar': 'c:\\Users\\Bagas AL-Fikri\\Downloads\\alpukat.png',
        'vitamin': {'Vitamin K': '26%', 'Vitamin E': '14%'},
        'serat': '6.7g',
        'protein': '2g',
        'lemak': '14.7g'
    },
    'kurma': {
        'kalori': 282,
        'gambar': 'c:\\Users\\Bagas AL-Fikri\\Downloads\\gambar kurma.png',
        'vitamin': {'Vitamin B6': '10%', 'Vitamin C': '3%'},
        'serat': '8g',
        'protein': '2.2g',
        'lemak': '0.2g'
    },
    'anggur': {
        'kalori': 67,
        'gambar': 'c:\\Users\\Bagas AL-Fikri\\Downloads\\gambar anggur.jpg',
        'vitamin': {'Vitamin C': '5%', 'Vitamin K': '18%'},
        'serat': '0.9g',
        'protein': '0.6g',
        'lemak': '0.2g'
    },
    'nanas': {
        'kalori': 50,
        'gambar': 'c:\\Users\\Bagas AL-Fikri\\Downloads\\nanas.jpeg',
        'vitamin': {'Vitamin C': '79%'},
        'serat': '1.4g',
        'protein': '0.5g',
        'lemak': '0.1g'
    },
    'kiwi': {
        'kalori': 61,
        'gambar': 'c:\\Users\\Bagas AL-Fikri\\Downloads\\gambar kiwii.png',
        'vitamin': {'Vitamin C': '112%', 'Vitamin K': '38%'},
        'serat': '2.1g',
        'protein': '1.1g',
        'lemak': '0.5g'
    },
    'rambutan': {
        'kalori': 68,
        'gambar': 'c:\\Users\\Bagas AL-Fikri\\Downloads\\gambar rambutann.png',
        'vitamin': {'Vitamin C': '44%'},
        'serat': '0.9g',
        'protein': '0.9g',
        'lemak': '0.2g'
    },
    'pepaya': {
        'kalori': 43,
        'gambar': 'c:\\Users\\Bagas AL-Fikri\\Downloads\\pepaya-removebg-preview.png',
        'vitamin': {'Vitamin C': '148%', 'Vitamin A': '31%'},
        'serat': '1.7g',
        'protein': '0.5g',
        'lemak': '0.3g'
    },
    'lemon': {
        'kalori': 29,
        'gambar': 'c:\\Users\\Bagas AL-Fikri\\Downloads\\lemon-removebg-preview.png',
        'vitamin': {'Vitamin C': '64%'},
        'serat': '2.8g',
        'protein': '1.1g',
        'lemak': '0.3g'
    },
    'markisa': {
        'kalori': 97,
        'gambar': 'c:\\Users\\Bagas AL-Fikri\\Downloads\\markisa-removebg-preview.png',
        'vitamin': {'Vitamin C': '20%'},
        'serat': '2.4g',
        'protein': '2.2g',
        'lemak': '0.7g'
    },
    'kelapa': {
        'kalori': 354,
        'gambar': 'c:\\Users\\Bagas AL-Fikri\\Downloads\\gambar_kelapa.png',
        'vitamin': {'Vitamin C': '3%', 'Vitamin B6': '5%'},
        'serat': '9g',
        'protein': '3.3g',
        'lemak': '33.5g'
    },
    'durian': {
        'kalori': 150,
        'gambar': 'c:\\Users\\Bagas AL-Fikri\\Downloads\\durian.png',
        'vitamin': {'Vitamin C': '47%', 'Vitamin B6': '10%'},
        'serat': '3.8g',
        'protein': '1.5g',
        'lemak': '5.3g'
    },
    'salak': {
        'kalori': 82,
        'gambar': 'c:\\Users\\Bagas AL-Fikri\\Downloads\\salak.png',
        'vitamin': {'Vitamin C': '8%'},
        'serat': '2.6g',
        'protein': '0.6g',
        'lemak': '0.7g'
    },
}




# Sekarang lanjutkan dengan kode aplikasi Streamlit Anda seperti biasa



st.title('Kalkulator Kalori Buah')
st.write("Selamat datang di aplikasi kalkulator kalori buah. Pilih buah favorit Anda dan berapa beratnya, lalu kami akan memberi tahu Anda jumlah kalori yang terkandung.")
buah = st.selectbox('Pilih Buah', list(kalori_buah.keys()), format_func=lambda x: x.capitalize())

berat = st.slider('Berat (gram)', min_value=1, max_value=1000, value=100)



if st.button('Hitung Kalori'):
    kalori_total = (kalori_buah[buah]['kalori'] / 100) * berat
    st.write(f"Jumlah kalori dalam {berat} gram {buah} adalah: {kalori_total} kalori")
    st.write("Informasi Nutrisi:")
    st.write(f"- Serat: {kalori_buah[buah]['serat']}")
    st.write(f"- Protein: {kalori_buah[buah]['protein']}")
    st.write(f"- Lemak: {kalori_buah[buah]['lemak']}")
    st.write("Kandungan Vitamin:")
    for vitamin, nilai in kalori_buah[buah]['vitamin'].items():
        st.write(f"- {vitamin}: {nilai}")
    st.image(kalori_buah[buah]['gambar'], caption='Gambar ' + buah.capitalize())

# Tambahkan rekomendasi buah berdasarkan jumlah kalori yang dipilih
st.sidebar.title('Rekomendasi Buah Berdasarkan Kalori')
kalori_target = st.sidebar.slider('Pilih Jumlah Kalori', min_value=10, max_value=1000, value=100)
st.sidebar.write('Buah-buahan dengan kalori serupa:')
for buah, info in kalori_buah.items():
    if abs((info['kalori'] / 100) * berat - kalori_target) < 20:
        st.sidebar.write(f"- {buah.capitalize()}")



