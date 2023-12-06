import pickle
import pandas as pd
import streamlit as st
import numpy as np
import base64
from streamlit_option_menu import option_menu
from PIL import Image
from PIL import Image, ImageDraw


# !! Dataset Rekomendasi Buku !!

book_names = pd.read_pickle("artifacts/book_names.pkl")
model = pd.read_pickle("artifacts/model.pkl")
book_pivot = pd.read_pickle("artifacts/book_pivot.pkl")
final_rating = pd.read_pickle("artifacts/final_rating.pkl")



# ---------- css tampilan ----------
#  
page_bg_img ="""
<style>
    [data-testid="stAppViewContainer"] {
        background-image: url("https://images.unsplash.com/photo-1465146633011-14f8e0781093?w=500&auto=format&fit=crop&q=60&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2h8MTA1fHxiYWNrZ3JvdW5kJTIwYnVrdSUyMGdlbGFwfGVufDB8fDB8fHww");
        background-size :cover;
    }
    [data-testid="stHeader"] {
        background-color: rgba(0,0,0,0);
    }
    [data-testid="stToolbar"] {
        right: 2rem;
    }
    [data-testid="stSidebar"] > div:first-child {
        background-image: url("https://www.istockphoto.com/id/foto/tekstur-kertas-daur-ulang-putih-gm1409340439-459919394");
        background-postion: center;
    }
</style>
"""
st.markdown(page_bg_img, unsafe_allow_html=True)


# ---------- Sidebar ---------- 

with st.sidebar:
    choice = option_menu('Dashboard Ruang Buku', ("Home", "Profile", "Store", "Chatbot"), 
    menu_icon="chat-text-fill",
    default_index=1)
    st.sidebar.image ('Ruang Buku/Ruang Buku.png' ,width=150 )



# ---------- Home ---------- 

if choice == "Home":
    st.title('Welcome to :red[ECOMMERCE RUANG BUKU]')
    col1, col2 = st.columns(2)
    with col1:
        st.write("E-Commerce Ruang Buku tercipta karena melihat dari kehidupan nyata yang dimana buku-buku yang sudah tidak terpakai bingung untuk dikemanakan. Menurut kami rasanya sayang jika buku-buku tersebut tidak dimanfaatkan kembali. Sehingga kami menciptakan E-Commerce Ruang Buku yaitu wadah/platform untuk pemanfaatan buku bekas yang masih layak untuk dipergunakan kembali")
    with col2:
        image = Image.open(r"Ruang Buku/Ruang Buku.png")
        st.image(image,width =200)


# ---------- Profile ---------- 

if choice == "Profile":
    st.title('Punggawa :red[The Cagurs]')
    def main():
        st.title('')
    col1, col2, col3 = st.columns(3)

    with col1:
        image = Image.open(r"Profile Tim/Ilham.jpg")
        st.image(image, width=150)
        st.markdown("<p style='text-align:center; font-size:18px;'>Muhamad Ilham Firmansyah</p>", unsafe_allow_html=True)
        st.write("Data Engineering & Full Stack Developer")

    with col2:
        image = Image.open(r"Profile Tim/Pedro.jpg")
        st.image(image, width=150)
        st.markdown("<p style='text-align:center; font-size:18px;'>Michel Mauliate Pedro Gultom</p>", unsafe_allow_html=True)
        st.write("Machine Learning Engineering & Data Engineering")

    with col3:
        image = Image.open(r"Profile Tim/Wendy.jpg")
        st.image(image, width=150)
        st.markdown("<p style='text-align:center; font-size:18px;'>Wendi Wildiansyah</p>", unsafe_allow_html=True)
        st.write("Ketua Tim,Technical Writer & Voice Actor Videografi")

    col4, col5, col6 = st.columns(3)

    with col4:
        image = Image.open(r"Profile Tim/DeTon.jpg")
        st.image(image, width=150)
        st.markdown("<p style='text-align:center; font-size:18px;'>Dede Toni</p>", unsafe_allow_html=True)
        st.write("Technical Writer & Editor Video ")

    with col5:
        image = Image.open(r"Profile Tim/Futuh.jpg")
        st.image(image, width=150)
        st.markdown("<p style='text-align:center; font-size:18px;'>Futuh Balad</p>", unsafe_allow_html=True)
        st.write("UI/UX Design & Tecnical Writer")

    with col6:
        image = Image.open(r"Profile Tim/Shafa.jpg")
        st.image(image, width=150)
        st.markdown("<p style='text-align:center; font-size:18px;'>Shafa Aulia Rizky Prameswari</p>", unsafe_allow_html=True)
        st.write("Technical Writer & Design Logo Web")

    # CSS profil 
    st.markdown(
        """
        <style>
            img {
                border-radius: 50%;
                overflow: hidden;
            }
        </style>
        """,
        unsafe_allow_html=True
    )


# ---------- Store ---------- 

if choice =="Store":
    st.title('Store :red[Ruang Buku]')
if "produk_buku" not in st.session_state:
    st.session_state.produk_buku = [
        {"judul": "A Fine Balance", "harga": 35000, "stok": 10},
        {"judul": "A Time to Kill", "harga": 57500, "stok": 5},
        {"judul": "Big Cherry Holler: A Big Stone Gap Novel", "harga": 25000, "stok": 8},
        {"judul": "Pulau Misteri : Petualangan di Nusantara", "harga": 45000, "stok": 15}
    ]

if "keranjang" not in st.session_state:
    st.session_state.keranjang = []

def tampilkan_toko():
    for buku in st.session_state.produk_buku:
        st.write(f"### {buku['judul']}")
        st.write(f"Harga: Rp {format_harga(buku['harga'])} | Stok: {buku['stok']}")
        if st.button(f"Beli {buku['judul']}"):
            tambahkan_ke_keranjang(buku)
            st.success(f"{buku['judul']} ditambahkan ke keranjang!")

def tampilkan_jual_buku():
    st.title("Jual Buku")

    # Formulir untuk menjual buku
    st.write("### Jual Buku Anda")
    nama_buku = st.text_input("Nama Buku")
    
    harga_buku = st.number_input("Harga Buku", min_value=0, value=0)
    stok_buku = st.number_input("Stok Buku", min_value=0, value=0)
    
    if st.button("Jual Buku"):
        if not nama_buku or harga_buku <= 0 or stok_buku <= 0:
            st.warning("Mohon lengkapi semua informasi untuk menjual buku.")
        else:
            buku_baru = {"judul": nama_buku, "harga": harga_buku, "stok": stok_buku}
            st.session_state.produk_buku.append(buku_baru)
            st.success(f"Buku '{nama_buku}' berhasil dijual!")

def tampilkan_checkout():
    st.title("Checkout")

    if not st.session_state.keranjang:
        st.warning("Keranjang belanja Anda kosong. Silakan beli beberapa buku terlebih dahulu.")
        return

    for buku in st.session_state.keranjang:
        st.write(f"### {buku['judul']}")
        st.write(f"Harga: Rp {format_harga(buku['harga'])}")

        # Kurangi stok buku
        buku_index = next((index for index, item in enumerate(st.session_state.produk_buku) if item["judul"] == buku["judul"]), None)
        if buku_index is not None:
            st.session_state.produk_buku[buku_index]["stok"] -= 1

    total_harga = sum(buku["harga"] for buku in st.session_state.keranjang)
    st.write(f"**Total Harga:** Rp {format_harga(total_harga)}")

    # Form Checkout
    st.write("### Informasi Pembayaran dan Pengiriman")
    nama_pengiriman = st.text_input("Nama Penerima")
    alamat_pengiriman = st.text_area("Alamat Pengiriman")
    metode_pembayaran = st.selectbox("Metode Pembayaran", ["Kartu Kredit", "Transfer Bank"])

    if st.button("Bayar"):
        st.success(f"Pembayaran berhasil! Terima kasih atas pembelian Anda, {nama_pengiriman}!")

def tambahkan_ke_keranjang(buku):
    st.session_state.keranjang.append(buku)

def format_harga(harga):
    return f"{harga:,.0f}"

# Main App
mode = st.selectbox("Pilih Halaman", ["Toko", "Jual Buku", "Checkout"])

if mode == "Toko":
    tampilkan_toko()
elif mode == "Jual Buku":
    tampilkan_jual_buku()
elif mode == "Checkout":
    tampilkan_checkout()


# ---------- Chatbot ------------

if choice =="Chatbot":
    st.title('Chatbot :red[Ruang Buku]')

def fecth_poster(suggestion):
    book_names = []
    ids_index = []
    poster_url = []

    for book_id in suggestion:
        book_names.append(book_pivot.index[book_id])

    for name in book_names[0]:
        ids = np.where(final_rating['title'] == name)[0][0]
        ids_index.append(ids)

    for idx in ids_index:
        url = final_rating.iloc[idx]['img_url']
        poster_url.append(url)

    return poster_url


def recommend_books(book_names):
    book_list = []
    book_id = np.where(book_pivot.index == book_names)[0][0]
    distance, suggestion = model.kneighbors(
        book_pivot.iloc[book_id, :].values.reshape(1, -1), n_neighbors=6)

    poster_url = fecth_poster(suggestion)

    for i in range(len(suggestion)):
        books = book_pivot.index[suggestion[i]]
        for j in books:
            book_list.append(j)

    return book_list, poster_url


selected_books = st.selectbox(
    "Masukkan Judul Buku Yang Ingin Dibeli, Kami RUBUK Akan Merekomendasikannya :)",
    book_names
)


if st.button('Tampilkan Rekomendasi'):
    recommendation_books, poster_url = recommend_books(selected_books)
    col1, col2, col3, col4, col5 = st.columns(5)

    with col1:
        st.text(recommendation_books[1])
        st.image(poster_url[1], width=65)

    with col2:
        st.text(recommendation_books[2])
        st.image(poster_url[2], width=65)

    with col3:
        st.text(recommendation_books[3])
        st.image(poster_url[3], width=65)

    with col4:
        st.text(recommendation_books[4])
        st.image(poster_url[4], width=65)

    with col5:
        st.text(recommendation_books[5])
        st.image(poster_url[5], width=70)

response = " Terima Kasih Telah Menggunakan Teman RUBUK :)"

