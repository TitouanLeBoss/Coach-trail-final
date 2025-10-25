import streamlit as st
import pandas as pd
from datetime import datetime
from supabase import create_client, Client
import os

# ------------------------------
# 1️⃣ CONFIGURATION STREAMLIT
# ------------------------------
st.set_page_config(page_title="Coach Trail", page_icon="🏃‍♂️", layout="wide")
st.title("🏔️ Mon Coach Trail")

# ------------------------------
# 2️⃣ CONNEXION À SUPABASE
# ------------------------------
# ⚠️ Ces infos NE DOIVENT PAS être écrites en clair ici.
# Tu les stockeras plus tard dans Streamlit Cloud > Settings > Secrets.
# Exemple de ce que tu mettras là-bas :
# SUPABASE_URL="https://xxxxx.supabase.co"
# SUPABASE_KEY="eyJhbGciOiJIUzI1NiIsInR5cCI..."

url = os.getenv("SUPABASE_URL")
key = os.getenv("SUPABASE_KEY")

if url and key:
    supabase: Client = create_client(url, key)
else:
    st.warning("🔐 Supabase non connecté — ajoute tes clés dans les secrets Streamlit.")

# ------------------------------
# 3️⃣ PAGE DE PROFIL
# ------------------------------
st.sidebar.header("Navigation")
page = st.sidebar.radio("Aller à :", ["Profil", "Calendrier"])

if page == "Profil":
    st.header("👤 Mon Profil")

    name = st.text_input("Nom")
    workload = st.slider("Charge de travail actuelle (1 = faible / 10 = très élevée)", 1, 10, 5)
    next_goal = st.text_input("Prochain objectif de l’année (ex: Trail des Alpes 25km)")

    if st.button("💾 Enregistrer mes infos"):
        if url and key:
            data = {"name": name, "workload": workload, "next_goal": next_goal}
            supabase.table("users").insert(data).execute()
            st.success("✅ Profil enregistré dans Supabase !")
        else:
            st.info("Simulation : Données enregistrées localement.")
            st.write({"name": name, "workload": workload, "next_goal": next_goal})

# ------------------------------
# 4️⃣ PAGE CALENDRIER
# ------------------------------
elif page == "Calendrier":
    st.header("📅 Mon Calendrier d'entraînement")

    # (Version simple : calendrier simulé)
    date = st.date_input("Date de la séance")
    title = st.text_input("Nom de la séance (ex: Sortie longue)")
    duration = st.number_input("Durée (minutes)", min_value=10, max_value=300, value=60)
    color = st.color_picker("Couleur de la séance", "#00b4d8")

    if st.button("Ajouter cette séance"):
        st.success(f"✅ Séance ajoutée : {title} ({duration} min le {date})")

    # Affichage d’exemple d’un mini tableau (plus tard → calendrier interactif)
    sample = pd.DataFrame({
        "Date": [datetime.today().date()],
        "Séance": ["Footing"],
        "Durée (min)": [45],
        "Couleur": ["#00b4d8"]
    })
    st.dataframe(sample)
