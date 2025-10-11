import streamlit as st
import pandas as pd
from datetime import datetime, timedelta

# ------------------------------
# CONFIG
# ------------------------------
st.set_page_config(page_title="Coach Trail - Test", page_icon="🏃‍♂️")
st.title("🏔️ Ton Coach Trail (version test)")

# ------------------------------
# FORMULAIRE UTILISATEUR
# ------------------------------
st.header("📝 Paramètres de ta course")

with st.form("course_form"):
    distance = st.number_input("Distance du trail (km)", min_value=5, max_value=200, value=30)
    denivele = st.number_input("Dénivelé positif (m)", min_value=0, max_value=10000, value=1000)
    date_trail = st.date_input("Date de ton trail", min_value=datetime.today())
    jours_dispo = st.multiselect(
        "Jours disponibles pour t'entraîner",
        ["Lundi","Mardi","Mercredi","Jeudi","Vendredi","Samedi","Dimanche"],
        default=["Mardi","Jeudi","Samedi"]
    )
    contraintes = st.text_area("Autres contraintes ou préférences (facultatif)", placeholder="Ex : pas d'entraînement le lundi soir")
    submitted = st.form_submit_button("Créer mon planning")

# ------------------------------
# SIMULATION DU PLANNING
# ------------------------------
if submitted:
    st.info("Ton coach réfléchit... ⏳")

    # On crée un planning fictif
    dates = [datetime.today() + timedelta(days=i) for i in range(7)]
    types_seance = ["Footing", "Fractionné", "Sortie longue", "Récup", "Footing", "Fractionné", "Récup"]
    durees = [30, 45, 90, 20, 35, 50, 25]

    df = pd.DataFrame({
        "Date": [d.strftime("%d/%m/%Y") for d in dates],
        "Type": types_seance,
        "Durée (min)": durees
    })

    # Code couleur pour le type de séance
    colors = {
        "Footing": "#a8dadc",
        "Fractionné": "#f4a261",
        "Sortie longue": "#2a9d8f",
        "Récup": "#e9c46a"
    }

    def color_row(row):
        return [f'background-color: {colors.get(row["Type"], "#ffffff")}' for _ in row]

    st.header("📅 Ton planning personnalisé (simulation)")
    st.dataframe(df.style.apply(color_row, axis=1))
