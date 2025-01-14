import streamlit as st
import random

# Deklarasi data armor list
armor_list = {
    "Baju Pengelana": {
        "Sayap Burung": "x35",
        "Kain": "40 poin",
        "Bahan_per_item": {"Sayap Burung": 35, "Kain": 40},
    },
    "Baju Diomedea": {
        "Kain Lembu": "x25",
        "Batu Ultimea": "x10",
        "Kain": "250 poin",
        "Logam": "50 poin",
        "Bahan_per_item": {"Kain Lembu": 25, "Kain": 250, "Logam": 50},
    },
    "Zirah Pepagan": {
        "Topeng Kuzto Rusak": "x1",
        "Kacang Mistis": "x1",
        "Herbal Berkualitas": "x2",
        "Kayu": "1.850 poin",
        "Bahan_per_item": {
            "Topeng Kuzto Rusak": 1,
            "Kacang Mistis": 1,
            "Herbal Berkualitas": 2,
            "Kayu": 1850,
        },
    },
    "Kostum Pengelabu": {
        "Kulit Naga Penyamar": "x4",
        "Mata Naga Penyamar": "x1",
        "Fauna": "1.250 poin",
        "Kain": "1.200 poin",
        "Bahan_per_item": {
            "Kulit Naga Penyamar": 4,
            "Mata Naga Penyamar": 1,
            "Fauna": 1250,
            "Kain": 1200,
        },
    },
    "Jubah Pendeta Air": {
        "Kitab Silat Prajurit Kodok": "x1",
        "Pecahan Zirah Prajurit Kodok": "x4",
        "Kain": "1.600 poin",
        "Fauna": "1.000 poin",
        "Bahan_per_item": {
            "Kitab Silat Prajurit Kodok": 1,
            "Pecahan Zirah Prajurit Kodok": 4,
            "Kain": 1600,
            "Fauna": 1000,
        },
    },
}


# Fungsi RNG untuk crafting
def custom_random_number():
    random_value = random.random()
    if random_value <= 0.90:
        return 0  # Peluang 90%
    elif random_value <= 0.999:
        return 1  # Peluang 8.99%
    else:
        return 2  # Peluang 0.01%


# Streamlit App
st.set_page_config(page_title="Toram Online Crafting Simulator", layout="wide")

# CSS untuk styling
st.markdown(
    """
    <style>
    body {
        background: linear-gradient(to bottom, #121212, #232323);
        color: white;
    }
    .title {
        text-align: center;
        color: #f9a825;
        font-size: 2.5rem;
        margin-bottom: 20px;
    }
    .box {
        background-color: #2b2b2b;
        border-radius: 15px;
        padding: 20px;
        box-shadow: 0px 4px 15px rgba(0, 0, 0, 0.5);
        margin-bottom: 20px;
    }
    .btn {
        margin-top: 20px;
        background-color: #f9a825;
        color: white;
        font-weight: bold;
        padding: 10px;
        border-radius: 10px;
        box-shadow: 0px 4px 10px rgba(0, 0, 0, 0.2);
        text-align: center;
    }
    .btn:hover {
        background-color: #d4a017;
        color: white;
    }
    .footer {
        display: flex;
        justify-content: space-between;
        align-items: center;
        padding: 20px;
        background-color: #1a1a2e;
        color: #f0f0f0;
        font-size: 1rem;
        box-shadow: 0px -4px 15px rgba(0, 0, 0, 0.5);
        border-top: 3px solid #f9a825;
    }
    .footer .left {
        text-align: left;
        flex: 1;
    }
    .footer .right {
        text-align: right;
        flex: 1;
        display: flex;
        align-items: center;
        justify-content: flex-end;
    }
    .footer .left p {
        margin: 0;
        font-weight: bold;
        font-size: 1.1rem;
    }
    .footer .right p {
        margin-right: 10px;
        font-weight: bold;
    }
    .footer a {
        color: #f9a825;
        text-decoration: none;
        font-size: 1.5rem;
        transition: transform 0.3s ease, color 0.3s ease;
    }
    .footer a:hover {
        color: #d4a017;
        transform: scale(1.2);
    }
    .footer a:active {
        transform: scale(0.9);
    }
    .footer img {
        margin-left: 10px;
        transition: transform 0.3s ease;
    }
    .footer img:hover {
        transform: rotate(360deg);
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# Judul
st.markdown(
    "<div class='title'>✨ Toram Online Crafting Simulator ✨</div>",
    unsafe_allow_html=True,
)

# Pilihan armor
armor_name = st.selectbox("Pilih Armor:", list(armor_list.keys()))
num_crafts = st.number_input(
    "Jumlah item yang ingin dicraft:", min_value=1, max_value=10000, value=1
)

# Dua kolom
col1, col2 = st.columns(2)

# Kolom Kiri: Detail Bahan dan Tombol
with col1:
    st.markdown("<div class='box'>", unsafe_allow_html=True)
    st.markdown("<h3>🛡️ Bahan yang Dibutuhkan</h3>", unsafe_allow_html=True)

    selected_armor = armor_list[armor_name]
    for material, value in selected_armor.items():
        if material != "Bahan_per_item":
            st.write(f"- **{material}**: {value}")

    if st.button("💡 Hitung Bahan", key="hitung_bahan"):
        bahan_per_item = selected_armor["Bahan_per_item"]
        total_bahan = {
            bahan: jumlah_per_item * num_crafts
            for bahan, jumlah_per_item in bahan_per_item.items()
        }
        st.session_state.total_bahan = total_bahan

    if st.button("🎲 Mulai Crafting", key="mulai_crafting"):
        results = {0: 0, 1: 0, 2: 0}
        for _ in range(num_crafts):
            result = custom_random_number()
            results[result] += 1
        st.session_state.crafting_results = results

    st.markdown("</div>", unsafe_allow_html=True)

# Kolom Kanan: Hasil Crafting
with col2:
    st.markdown("<div class='box'>", unsafe_allow_html=True)
    st.markdown("<h3>📊 Hasil Perhitungan dan Crafting</h3>", unsafe_allow_html=True)

    if "total_bahan" in st.session_state:
        st.write("**Total Bahan yang Dibutuhkan:**")
        for bahan, total in st.session_state.total_bahan.items():
            st.write(f"- {bahan}: {total}")
    else:
        st.write("Klik tombol **Hitung Bahan** untuk melihat hasilnya.")

    if "crafting_results" in st.session_state:
        st.write("**Hasil Crafting:**")
        st.write(f"- Slot 0: **{st.session_state.crafting_results[0]} kali**")
        st.write(f"- Slot 1: **{st.session_state.crafting_results[1]} kali**")
        st.write(f"- Slot 2: **{st.session_state.crafting_results[2]} kali**")
    else:
        st.write("Klik tombol **Mulai Crafting** untuk melihat hasilnya.")

    st.markdown("</div>", unsafe_allow_html=True)
