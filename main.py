import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import altair as alt
import matplotlib.pyplot as plt
import seaborn as sns
import pickle
import os

@st.cache_data
def load_data():
    df = pd.read_csv("hotel_bookings (1).csv")
    return df

# Fungsi untuk menampilkan halaman utama
def show_about():
    st.title("Hotel Booking Demand Dataset")

    st.title("Tujuan Bisnis")
    st.write("""Tujuan bisnis dari analisis data booking hatel ini adalah untuk membantu hotel mengetahui Kumpulan data yang berisi informasi pemesanan untuk hotel kota dan hotel resor,mencakup informasi seperti kapan pemesanan dilakukan, lama menginap, jumlah orang dewasa, anak-anak, dan/atau bayi, dan jumlah tempat parkir yang tersedia, dan lain lain, sehingga dapat meminimalkan risiko yang terjadi. Analisis data juga dapat membantu hotel dalam menentukan area risiko yang lebih besar sehingga mereka dapat membuat strategi pemasaran yang tepat dan memberikan layanan yang lebih baik lagi kepada pelanggan.""")
    st.title("Assess Situation")
    st.write("""Situasi bisnis yang mendasari analisis ini adalah Tren Permintaan merupakan kunci untuk memahami bagaimana permintaan untuk akomodasi berubah seiring waktu. Ini mencakup pemahaman tentang musim tinggi dan musim rendah, tren liburan, tren perjalanan bisnis, dan perubahan dalam preferensi konsumen,Persaingan antar hotel di suatu daerah bisa sangat memengaruhi bisnis. Jika daerah tersebut memiliki banyak hotel dengan fasilitas dan harga yang serupa, hotel mungkin perlu bersaing lebih keras untuk menarik tamu, dan efektivitas pemasaran membantu platform untuk memahami kinerja kampanye iklan online, promosi, dan strategi pemasaran lainnya. Ini termasuk pemantauan konversi, retensi pelanggan, dan nilai seumur hidup pelanggan. """)
    st.title("Tujuan Data Mining")
    st.write("""Tujuan dari data mining data booking hotel adalah untuk mengidentifikasi pola, tren, dan wawasan yang dapat membantu manajemen hotel dalam pengambilan keputusan yang lebih baik. adapun beberapa tujuannya, yaitu segmentasi pelanggan, prediksi permintaan, penyempurnaan penawaran dan promosi, peningkatan pengalaman pelanggan, deteksi penipuan dan keamanan, optimasi operasional, analisis kepuasan pelanggan, dan penyusuaian inventaris dan penyedian. oleh karena itu, hotel memerlukan analisis data yang tepat untuk membantu hotel meningkatkan layanan, efisiensi operasional, dan keuntungan keseluruhan hotel dengan memanfaatkan data dari proses booking. """)
    st.title("Rencana Proyek")
    st.write("""
1. Rencana proyek untuk dataset booking hotel mencakup delapan tahap yang penting:

2. Pengumpulan Data: Identifikasi sumber data relevan, kumpulkan data, dan pastikan kepatuhan terhadap kebijakan privasi dan peraturan data.

3. Pembersihan dan Pengolahan Data: Evaluasi kualitas data, tangani data yang hilang atau tidak lengkap, lakukan normalisasi, dan amankan data sensitif.

4. Eksplorasi Data: Lakukan analisis awal untuk memahami distribusi variabel dan identifikasi faktor yang memengaruhi pemesanan hotel.

5. Pemodelan Prediktif: Tentukan tujuan analisis, pilih model prediktif yang sesuai, dan bagi dataset untuk evaluasi kinerja model.

6. Evaluasi dan Validasi Model: Evaluasi kinerja model menggunakan metrik yang relevan, hindari overfitting, dan perbaiki model berdasarkan hasil evaluasi.

7. Interpretasi Hasil: Interpretasikan temuan dan hasil model untuk mendapatkan wawasan berharga tentang faktor-faktor yang memengaruhi pemesanan hotel.

8. Dokumentasi dan Komunikasi: Dokumentasikan proses analisis data, komunikasikan temuan dan rekomendasi kepada pihak terkait, dan siapkan laporan final proyek.

9. Pemeliharaan dan Pengembangan Lanjutan: Lakukan pemeliharaan rutin pada model dan analisis, dan terus kembangkan dan tingkatkan model atau analisis dengan teknik analisis yang lebih canggih. """)
    st.title("Data Booking Hotel Demand")
    # Path ke file CSV
    file_path = 'Data Cleaned (5).csv'

    # Periksa keberadaan file
    if not os.path.exists(file_path):
        st.error(f"File '{file_path}' tidak ditemukan. Pastikan file berada di lokasi yang benar.")
        st.stop()

    # Muat data CSV
    try:
        df = pd.read_csv(file_path)
        st.write(df)  # Tampilkan data jika berhasil dimuat
    except Exception as e:
        st.error(f"Gagal memuat file CSV: {e}")

# Fungsi untuk menampilkan halaman tentang
def show_Distribusi(df):
# Judul dan deskripsi
    st.title("Visualisasi Data Mining menggunakan Streamlit")
    st.title("Distribusi Nilai")
    st.write("Menu ini menampilkan distribusi dari nilai lead time, stays in weekend nights, dan stays in week nights dalam dataset Hotel Booking Demand.")

    st.subheader("Distribusi Tipe Pelanggan")
    plt.figure(figsize=(10, 5))
    fig, ax = plt.subplots()
    sns.countplot(x='reservation_status', hue='is_canceled', data=df, palette=['darkturquoise', 'royalblue'])
    plt.title('Count of Cancellations by Reservation Status')
    plt.xlabel('Reservation Status')
    plt.ylabel('Count')
    plt.legend(title='Is Canceled', labels=['Not Canceled', 'Canceled'])
    plt.title("Distribusi Tipe Pelanggan")
    st.pyplot(fig)
    st.write("""Diagram batang pertama menunjukkan distribusi tipe pelanggan berdasarkan status reservasi. Status reservasi dibagi menjadi tiga kategori: "Check-Out" (Tamu telah check-out), "Canceled" (Reservasi dibatalkan), dan "No-Show" (Tamu tidak datang). Jumlah "Check-Out" jauh lebih tinggi dibandingkan jumlah "Canceled" dan "No-Show".""")
    # Buat plot pie
    fig, ax = plt.subplots()
    s = df['is_canceled'].value_counts()
    s.plot(kind='pie', autopct='%1.1f%%', startangle=360, labels=['Not Canceled', 'Canceled'], ax=ax)
    #ax.set_ylabel('')  Hilangkan label sumbu y
    ax.legend()
    # Tampilkan plot di Streamlit
    st.pyplot(fig)
    st.write("""Diagram lingkaran menunjukkan persentase pembatalan reservasi dibandingkan dengan reservasi yang tidak dibatalkan. Dari data ini, terlihat bahwa sekitar 50.5% reservasi tidak dibatalkan, sedangkan 49.5% reservasi dibatalkan.""")

    # Plot bar chart
    fig, ax = plt.subplots(figsize=(12,6))
    sns.barplot(x='arrival_date_year', y='lead_time',hue='is_canceled', data= df, palette='vlag', ax=ax)
    plt.title('Arriving year, Lead time and Cancelations')
    st.pyplot(fig)
    st.write("""Diagram batang terakhir menunjukkan aktivitas kamar hotel per bulan, dibagi menjadi dua kelompok: reservasi yang dibatalkan dan reservasi yang tidak dibatalkan. Garis rata-rata ditampilkan untuk setiap kelompok. Tampaknya aktivitas kamar cenderung stabil dari bulan ke bulan, meskipun ada sedikit fluktuasi antara reservasi yang dibatalkan dan yang tidak dibatalkan.""")

def show_hubungan(df):
    st.title("Visualisasi Data Mining menggunakan Streamlit")
    st.title("Hubungan Nilai")
    st.write("Menu ini menampilkan hubungan antara nilai math, reading, dan writing dalam dataset Hotel Bookings.")
    plot_option = st.selectbox("Pilih Plot:", ["Lead Time vs Stays in Weekend Nights", "Lead Time vs Stays in Week Nights", "Stays in Weekend Nights vs Stays in Week Nights"])

    if plot_option == "Lead Time vs Stays in Weekend Nights":
        st.subheader("Scatter Plot: Lead Time vs Stays in Weekend Nights")
        fig, ax = plt.subplots()
        sns.scatterplot(x='lead_time', y='stays_in_weekend_nights', data=df)
        ax.set_xlabel("Lead Time")
        ax.set_ylabel("Stays in Weekend Nights")
        st.pyplot(fig)

    elif plot_option == "Lead Time vs Stays in Week Nights":
        st.subheader("Scatter Plot: Lead Time vs Stays in Week Nights")
        fig, ax = plt.subplots()
        sns.scatterplot(x='lead_time', y='stays_in_week_nights', data=df)
        ax.set_xlabel("Lead Time")
        ax.set_ylabel("Stays in Week Nights")
        st.pyplot(fig)

    elif plot_option == "Stays in Weekend Nights vs Stays in Week Nights":
        st.subheader("Scatter Plot: Stays in Weekend Nights vs Stays in Week Nights")
        fig, ax = plt.subplots()
        sns.scatterplot(x='stays_in_weekend_nights', y='stays_in_week_nights', data=df)
        ax.set_xlabel("Stays in Weekend Nights")
        ax.set_ylabel("Stays in Week Nights")
        st.pyplot(fig)

    st.title("Korelasi")
    df_file_corr = df.corr(numeric_only=True)

    # Ambil hanya 10 kolom dan baris pertama
    # df_file_corr_subset = df_file_corr.iloc[:10, :10]

    # Buat heatmap menggunakan seaborn
    fig, ax = plt.subplots(figsize=(30, 30))
    sns.heatmap(df_file_corr, annot=True, cmap='vlag', ax=ax)
    plt.title('Nilai Korelasi')
    plt.show()

    # Tampilkan heatmap menggunakan Streamlit
    st.pyplot(fig)

    # Tambahkan teks penjelasan
    text = 'Tabel korelasi diatas menunjukkan bahwa terdapat hubungan yang signifikan antara beberapa variabel. Hotel dapat menggunakan informasi ini untuk membuat keputusan yang lebih baik tentang layanan hotel, strategi marketing, dan program loyalitas pelanggan.'
    st.markdown(text)
    

# Memuat data
df = load_data()

# Menampilkan hubungan
# show_relationship(df)


# Fungsi untuk menampilkan halaman perbandingan
def show_Perbandingan(df):
    st.title("Visualisasi Data Mining menggunakan Streamlit")
    st.title("Perbandingan")
        # Membuat subplots
    fig, axes = plt.subplots(2, 2, figsize=(15, 12))

    # Plot pertama: market_segment
    sns.countplot(x='market_segment', data=df, palette='rocket', ax=axes[0, 0])
    axes[0, 0].set_title('Types of market segment', fontweight="bold", size=10)

    # Plot kedua: distribution_channel
    sns.countplot(data=df, x='distribution_channel', palette='Set1_r', ax=axes[0, 1])
    axes[0, 1].set_title('Types of distribution channels', fontweight="bold", size=20)

    # Plot ketiga: is_repeated_guest
    sns.countplot(data=df, x='is_repeated_guest', ax=axes[1, 0]).set_title('Graph showing whether guest is repeated guest', fontsize=20)

    # Plot keempat: customer_type
    sns.countplot(x='customer_type', data=df, ax=axes[1, 1]).set_title('customer_type')

    # Menampilkan plot di Streamlit
    st.pyplot(fig)
    st.write("""1. Types of Market Segment (Jenis Segmen Pasar):

Diagram batang menampilkan jumlah reservasi hotel berdasarkan jenis segmen pasar. Segmen pasar terbagi menjadi "Direct", "Corporate", "Online TA", "Offline TA/TO", dan "Complementary Groups". Jumlah reservasi tertinggi terjadi pada segmen pasar "Online TA" dan "Offline TA/TO", diikuti oleh segmen "Corporate".

2. Types of Distribution Channels (Jenis Saluran Distribusi):
Diagram batang menunjukkan jumlah reservasi hotel berdasarkan jenis saluran distribusi. Saluran distribusi terbagi menjadi "Direct", "Corporate", "TA/TO", dan "Undefined". Jumlah reservasi tertinggi terjadi melalui saluran distribusi "TA/TO" (Travel Agent/Tour Operator).

3. Graph showing whether guest is repeated guest (Grafik yang menunjukkan apakah tamu adalah tamu berulang):
Diagram batang menunjukkan jumlah reservasi hotel berdasarkan apakah tamu adalah tamu berulang atau tidak. Terlihat bahwa jumlah tamu yang tidak berulang (0) jauh lebih tinggi daripada jumlah tamu yang berulang (1).

4. Customer Type (Jenis Pelanggan):
Diagram batang menampilkan jumlah reservasi hotel berdasarkan jenis pelanggan. Jenis pelanggan terbagi menjadi "Transient", "Contract", "Transient-Party", "Group", dan "Ta". Mayoritas reservasi berasal dari jenis pelanggan "Transient".""")
# Fungsi untuk menampilkan halaman komposisi
def show_Komposisi(df):
    st.title("Composition")

    # Buat pie chart
    fig, ax = plt.subplots(figsize=(8, 8))
    ax.pie(df.groupby(by=["arrival_date_month"]).size(), labels=df["arrival_date_month"].unique(), autopct="%0.2f")
    ax.set_title('Arrivals per month')
    st.pyplot(fig)
    st.write("""Terdapat pola kedatangan tamu yang bervariasi per bulan. Bulan-bulan musim panas, seperti Juli dan Agustus, memiliki persentase kedatangan yang lebih tinggi, sementara bulan-bulan musim dingin, seperti Januari dan Februari, memiliki persentase kedatangan yang lebih rendah. Hal ini mungkin menggambarkan adanya musim liburan atau faktor-faktor lain yang memengaruhi arus kedatangan tamu ke hotel selama berbagai bulan dalam setahun.""")

def predict_cancellation(df):
    st.title("Visualisasi Data Mining menggunakan Streamlit")
    st.title("Hotel Booking Cancellation Prediction")

    # Select features
    feature_columns = [
        'hotel','lead_time', 'arrival_date_year', 'arrival_date_week_number', 
        'arrival_date_day_of_month', 'stays_in_weekend_nights', 'stays_in_week_nights', 
        'adults', 'children', 'babies', 'is_repeated_guest', 'previous_cancellations', 
        'previous_bookings_not_canceled', 'booking_changes', 'deposit_type', 'agent', 
        'days_in_waiting_list', 'adr', 'required_car_parking_spaces', 'total_of_special_requests'
    ]

    selected_features = {}
    for feature in feature_columns:
        selected_features[feature] = st.selectbox(f"{feature.replace('_', ' ').title()}", sorted(df[feature].unique()))

    data = pd.DataFrame(selected_features, index=[0])

    # One-hot encode categorical features
    data = pd.get_dummies(data, columns=['hotel','deposit_type'])

    # Ensure all columns in data are numeric
    data = data.astype(float)

    # Button for prediction
    button = st.button('Predict')
    if button:
        with open('model.pkl', 'rb') as file:
            loaded_model = pickle.load(file)

        # Predict using model
        predicted = loaded_model.predict(data)

        # Display prediction
        print(predicted)
        if predicted[0] == 0:
            st.write('Not Canceled')
        else:
            st.write('Canceled')

# Assuming df is your DataFrame
# df = pd.read_csv('hotel_data.csv')  # Load your data here
# predict_cancellation(df)

# Memuat data
df = load_data()

# Mengatur sidebar
df2 = pd.read_csv('Data Cleaned (5).csv')
nav_options = {
    "About": show_about,
    "Distribution": lambda: show_Distribusi(df),
    "Relations": lambda: show_hubungan(df),
    "Comparison": lambda: show_Perbandingan(df),
    "Composition": lambda: show_Komposisi(df),
    "Predict": lambda: predict_cancellation(df2)
}

# Menampilkan sidebar
st.sidebar.title("Hotel Demand")
selected_page = st.sidebar.radio("Menu", list(nav_options.keys()))

# Menampilkan halaman yang dipilih
nav_options[selected_page]()