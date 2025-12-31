import streamlit as st
import pandas as pd

# TITLE
st.title("Aplikasi Streamlit Sederhana")

# HEADER
st.header("Contoh Komponen Streamlit")

# SUBHEADER
st.subheader("Penjelasan")

# TEXT / PARAGRAPH
st.write(
    "Ini adalah contoh web page yang dibuat menggunakan Streamlit. "
    "Aplikasi ini menampilkan teks, kode, tabel data, dan grafik."
)

# CAPTION
st.caption("Dibuat menggunakan Streamlit")

# CODE
st.code(
    """import streamlit as st
st.title("Hello Streamlit")""",
    language="python"
)

# DATA
data = pd.DataFrame({
    "Nama": ["Andi", "Budi", "Citra", "Dewi"],
    "Nilai": [80, 90, 75, 85]
})

# DATAFRAME
st.subheader("Tabel Data")
st.dataframe(data)

# CHART
st.subheader("Grafik Nilai")
st.bar_chart(data.set_index("Nama"))

git init
git remote add origin git init
git remote add origin https://github.com/hisyamabdulah/hisyamnewstreamlit
git branch -M main
git push -u origin main
git branch -M main
git push -u origin main
