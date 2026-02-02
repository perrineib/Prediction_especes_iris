import streamlit as st
import requests
import os
import pandas as pd

# URL adaptée selon l'environnement
API_URL = os.getenv("API_URL", "http://localhost:8000")

# Configuration de la page
st.set_page_config(
    page_title="Prédiction de l'espèce",
    page_icon="🌸",
    layout="centered"
)

# CSS personnalisé 
st.markdown("""
    <style>
    .main {
        background: linear-gradient(135deg, #ffeef8 0%, #e8f5e9 100%);
    }

    h1 {
        color: #2c3e50;
        text-align: center;
        font-size: 2.5em;
        margin-bottom: 40px;
    }

    .stButton > button {
        background: linear-gradient(135deg, #ff4081, #f50057);
        color: white;
        font-size: 1.2em;
        font-weight: bold;
        border: none;
        border-radius: 50px;
        padding: 15px 40px;
        box-shadow: 0 4px 15px rgba(255, 64, 129, 0.4);
        transition: all 0.3s ease;
        width: 100%;
    }

    .stButton > button:hover {
        transform: scale(1.05);
        box-shadow: 0 6px 20px rgba(255, 64, 129, 0.6);
    }

    .slider-label {
        color: #000000;
        font-size: 1.1em;
        font-weight: 500;
        margin-bottom: 10px;
    }
    </style>
""", unsafe_allow_html=True)

# Sidebar
st.sidebar.title("🌸 Navigation")
page = st.sidebar.radio("", ["🌺 Prédiction", "🌺 Modèle & Data"])

# ============================================
# PAGE PRÉDICTION
# ============================================
if page == "🌺 Prédiction":
    # Titre 
    st.markdown("<h1>🌸 Prédiction d'espèces d'Iris🌸</h1>", unsafe_allow_html=True)

    # Récupérer et afficher l'accuracy du modèle
    #try:
    #    info_response = requests.get(API_URL)
    #    if info_response.status_code == 200:
    #        info = info_response.json()
    #        model_accuracy = info.get("model_accuracy")
    #        if model_accuracy:
    #            st.markdown(f'<div style="text-align: center; color: #34495e; font-size: 0.95em; margin-bottom: 20px;">Précision du modèle : <strong>{model_accuracy}%</strong></div>', unsafe_allow_html=True)
    #except:
    #    pass

    # Encart de présentation de l'application
    st.markdown("""
        <div style="
            background: linear-gradient(135deg, #fff3e0 0%, #e8f5e9 100%);
            border-left: 4px solid #ff4081;
            padding: 15px;
            margin: 15px 0 25px 0;
            border-radius: 8px;
            box-shadow: 0 2px 8px rgba(0,0,0,0.1);
        ">
            <p style="margin: 0; color: #2c3e50; font-size: 0.95em; line-height: 1.6; text-align: justify;">
                Cette application utilise un modèle de Machine Learning pour prédire l'espèce d'iris à partir de
                mesures de ses pétales et sépales. Ajustez les curseurs ci-dessous pour entrer les dimensions de
                votre fleur et obtenez une prédiction instantanée avec le niveau de confiance associé.
            </p>
        </div>
    """, unsafe_allow_html=True)

    # Conteneur principal
    with st.container():
        # Sliders avec labels personnalisés et infobulles
        st.markdown('<p class="slider-label">Longueur du <span style="cursor: help; color: #000000; text-decoration: underline dotted;" title="Le sépale est la partie externe de la fleur qui protège le bouton floral avant son ouverture">sépale</span> (cm)</p>', unsafe_allow_html=True)
        sepal_length = st.slider(
            "sepal_length_label",
            min_value=4.0,
            max_value=8.0,
            value=5.8,
            step=0.01,
            label_visibility="collapsed"
        )

        st.markdown('<p class="slider-label">Largeur du <span style="cursor: help; color: #000000; text-decoration: underline dotted;" title="Le sépale est la partie externe de la fleur qui protège le bouton floral avant son ouverture">sépale</span> (cm)</p>', unsafe_allow_html=True)
        sepal_width = st.slider(
            "sepal_width_label",
            min_value=2.0,
            max_value=4.5,
            value=3.0,
            step=0.01,
            label_visibility="collapsed"
        )

        st.markdown('<p class="slider-label">Longueur du <span style="cursor: help; color: #000000; text-decoration: underline dotted;" title="Le pétale est la partie colorée et décorative de la fleur, située à l\'intérieur des sépales">pétale</span> (cm)</p>', unsafe_allow_html=True)
        petal_length = st.slider(
            "petal_length_label",
            min_value=1.0,
            max_value=7.0,
            value=3.8,
            step=0.01,
            label_visibility="collapsed"
        )

        st.markdown('<p class="slider-label">Largeur du <span style="cursor: help; color: #000000; text-decoration: underline dotted;" title="Le pétale est la partie colorée et décorative de la fleur, située à l\'intérieur des sépales">pétale</span> (cm)</p>', unsafe_allow_html=True)
        petal_width = st.slider(
            "petal_width_label",
            min_value=0.1,
            max_value=2.5,
            value=1.3,
            step=0.01,
            label_visibility="collapsed"
        )

    # Bouton de prédiction 
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        if st.button("🌺 Prédire l'espèce 🌺"):
            # Préparer les données à envoyer
            data = {
                "features": [sepal_length, sepal_width, petal_length, petal_width]
            }

            try:
                # Faire la requête à l'API
                response = requests.post(API_URL, json=data)

                if response.status_code == 200:
                    result = response.json()
                    prediction = result.get("prediction")
                    confidence = result.get("confidence")
                    probabilities = result.get("probabilities", {})

                    # Mapper les prédictions aux noms d'espèces avec liens Wikipedia et résumés
                    species_info = {
                        0: {
                            "name": "Setosa",
                            "wiki": "https://en.wikipedia.org/wiki/Iris_setosa",
                            "summary": "L'Iris setosa est une espèce d'iris originaire des régions arctiques et subarctiques. Cette plante vivace se distingue par ses fleurs violettes à bleues et ses feuilles en forme d'épée. Elle pousse naturellement dans les zones humides et les prairies.",
                            "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/5/56/Kosaciec_szczecinkowaty_Iris_setosa.jpg/440px-Kosaciec_szczecinkowaty_Iris_setosa.jpg"
                        },
                        1: {
                            "name": "Versicolor",
                            "wiki": "https://fr.wikipedia.org/wiki/Iris_versicolor",
                            "summary": "L'Iris versicolor, aussi appelé iris versicolore, est une espèce originaire d'Amérique du Nord. Ses fleurs présentent des teintes variées allant du violet au bleu avec des veines plus foncées. Cette plante pousse dans les milieux humides et marécageux.",
                            "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/4/41/Iris_versicolor_3.jpg/440px-Iris_versicolor_3.jpg"
                        },
                        2: {
                            "name": "Virginica",
                            "wiki": "https://en.wikipedia.org/wiki/Iris_virginica",
                            "summary": "L'Iris virginica est une espèce native de l'est des États-Unis. Elle se caractérise par ses grandes fleurs violettes à bleues avec des pétales tombants marqués de jaune. Cette plante affectionne les zones humides et les bords de cours d'eau.",
                            "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/9/9f/Iris_virginica.jpg/440px-Iris_virginica.jpg"
                        }
                    }

                    info = species_info.get(prediction)
                    species = info["name"] if info else "Inconnu"
                    wiki_link = info["wiki"] if info else ""
                    summary = info["summary"] if info else ""
                    image_url = info["image"] if info else ""

                    # Afficher le résultat avec style
                    st.markdown("<br>", unsafe_allow_html=True)
                    st.success(f"🌸 Espèce prédite : **{species}** 🌸")

                    # Afficher le résumé de l'espèce
                    if summary:
                        st.markdown(f"""
                            <div style="
                                background: linear-gradient(135deg, #fff3e0 0%, #e8f5e9 100%);
                                border-left: 4px solid #ff4081;
                                padding: 15px;
                                margin: 15px 0;
                                border-radius: 8px;
                                box-shadow: 0 2px 8px rgba(0,0,0,0.1);
                            ">
                                <p style="margin: 0 0 10px 0; color: #2c3e50; font-size: 0.95em; line-height: 1.6; text-align: justify;">
                                    {summary}
                                </p>
                                <p style="margin: 10px 0 0 0; text-align: center;">
                                    <a href="{wiki_link}" target="_blank" style="color: #ff4081; font-size: 0.95em; text-decoration: none; font-weight: 500;">
                                        📖 En savoir plus sur Wikipedia
                                    </a>
                                </p>
                            </div>
                        """, unsafe_allow_html=True)

                        # Afficher l'image 
                        if image_url:
                            st.markdown(f"""
                                <div style="text-align: center; margin: 15px 0;">
                                    <img src="{image_url}" alt="{species}" style="max-width: 100%; height: auto; border-radius: 8px; box-shadow: 0 2px 8px rgba(0,0,0,0.2);">
                                </div>
                            """, unsafe_allow_html=True)

                    # Afficher la confiance
                    st.markdown(f'<div style="text-align: center; color: #2c3e50; font-size: 1.2em; margin-top: 10px;">Confiance : <strong>{confidence}%</strong></div>', unsafe_allow_html=True)

                    # Afficher toutes les probabilités
                    st.markdown("<br>", unsafe_allow_html=True)
                    st.markdown('<p style="text-align: center; color: #34495e; font-size: 1.1em; margin-bottom: 10px;">Probabilités pour chaque espèce :</p>', unsafe_allow_html=True)

                    # Afficher les probabilités avec des colonnes Streamlit
                    col1, col2, col3 = st.columns(3)

                    with col1:
                        st.markdown(f'<p style="text-align: center; margin: 0; color: #34495e; font-size: 0.9em;">Setosa</p>', unsafe_allow_html=True)
                        st.markdown(f'<p style="text-align: center; margin: 5px 0 0 0; color: #2c3e50; font-size: 1.3em; font-weight: bold;">{probabilities["Setosa"]}%</p>', unsafe_allow_html=True)

                    with col2:
                        st.markdown(f'<p style="text-align: center; margin: 0; color: #34495e; font-size: 0.9em;">Versicolor</p>', unsafe_allow_html=True)
                        st.markdown(f'<p style="text-align: center; margin: 5px 0 0 0; color: #2c3e50; font-size: 1.3em; font-weight: bold;">{probabilities["Versicolor"]}%</p>', unsafe_allow_html=True)

                    with col3:
                        st.markdown(f'<p style="text-align: center; margin: 0; color: #34495e; font-size: 0.9em;">Virginica</p>', unsafe_allow_html=True)
                        st.markdown(f'<p style="text-align: center; margin: 5px 0 0 0; color: #2c3e50; font-size: 1.3em; font-weight: bold;">{probabilities["Virginica"]}%</p>', unsafe_allow_html=True)

                else:
                    st.error(f" Erreur de l'API : {response.status_code}")

            except requests.exceptions.ConnectionError:
                st.error(" Impossible de se connecter à l'API. Vérifiez que le serveur FastAPI est lancé.")
            except Exception as e:
                st.error(f" Erreur : {str(e)}")

# ============================================
# PAGE MODÈLE & DATA
# ============================================
elif page == "🌺 Modèle & Data":
    st.markdown("<h1>🌺 Modèle & Données</h1>", unsafe_allow_html=True)

    # Informations sur le dataset
    st.markdown("## À propos du dataset Iris")
    st.markdown("""
        <div style="
            background: linear-gradient(135deg, #fff3e0 0%, #e8f5e9 100%);
            border-left: 4px solid #ff4081;
            padding: 15px;
            margin: 15px 0;
            border-radius: 8px;
            box-shadow: 0 2px 8px rgba(0,0,0,0.1);
        ">
            <p style="margin: 0 0 10px 0; color: #2c3e50; font-size: 0.95em; line-height: 1.6;">
                <strong>Dataset Iris</strong><br>
                • 150 échantillons (50 par espèce)<br>
                • 4 caractéristiques (longueur/largeur sépales et pétales)<br>
                • 3 classes (Setosa, Versicolor, Virginica)<br>
                • Split : 80% entraînement / 20% test<br>
                • Modèle : Random Forest (100 arbres)
            </p>
        </div>
    """, unsafe_allow_html=True)

    st.markdown("---")

    try:
        info_response = requests.get(API_URL)
        if info_response.status_code == 200:
            metrics = info_response.json()
            model_accuracy = metrics.get("model_accuracy")
            conf_matrix = metrics.get("confusion_matrix")
            class_report = metrics.get("classification_report")

            # Section accuracy
            st.markdown("## Performance globale")

            # Encadré explicatif pour l'accuracy élevée
            
            st.markdown(f"""
                <div style="
                    background: linear-gradient(135deg, #fff3e0 0%, #e8f5e9 100%);
                    border-left: 4px solid #ff4081;
                    padding: 20px;
                    margin: 15px 0;
                    border-radius: 8px;
                    box-shadow: 0 2px 8px rgba(0,0,0,0.1);
                    text-align: center;
                ">
                    <p style="margin: 0; color: #2c3e50; font-size: 1.1em;">
                        <strong>Accuracy du modèle</strong>
                    </p>
                    <p style="margin: 10px 0 0 0; color: #ff4081; font-size: 2.5em; font-weight: bold;">
                        {model_accuracy}%
                    </p>
                </div>
            """, unsafe_allow_html=True)
            if model_accuracy and model_accuracy >= 99:
                st.markdown("""
                    <div style="
                        background: linear-gradient(135deg, #fff3e0 0%, #e8f5e9 100%);
                        border-left: 4px solid #6a1b9a;
                        padding: 15px;
                        margin: 15px 0;
                        border-radius: 8px;
                        box-shadow: 0 2px 8px rgba(0,0,0,0.1);
                    ">
                        <p style="margin: 0; color: #2c3e50; font-size: 0.9em; line-height: 1.6; text-align: justify;">
                            Les trois espèces d'iris présentent des caractéristiques morphologiques distinctes qui permettent une classification quasi-parfaite d'où l'accuracy de <strong>100%</strong>.
                        </p>
                    </div>
                """, unsafe_allow_html=True)

            st.markdown("---")

            # Matrice de confusion
            if conf_matrix and class_report:
                st.markdown("## Matrice de confusion")

                species_names = ["Setosa", "Versicolor", "Virginica"]
                df_conf = pd.DataFrame(conf_matrix, index=species_names, columns=species_names)
                st.dataframe(df_conf, use_container_width=True)

                st.markdown("---")

                # Métriques par espèce
                st.markdown("## Métriques par espèce")

                report_data = []
                for species in species_names:
                    if species.lower() in class_report:
                        data = class_report[species.lower()]
                        report_data.append({
                            "Espèce": species,
                            "Précision": f"{data['precision']*100:.1f}%",
                            "Rappel": f"{data['recall']*100:.1f}%",
                            "F1-Score": f"{data['f1-score']*100:.1f}%",
                            "Support": int(data['support'])
                        })

                if report_data:
                    df_report = pd.DataFrame(report_data)
                    st.dataframe(df_report, use_container_width=True, hide_index=True)

    except Exception as e:
        st.error(f"Impossible de charger les métriques : {e}")
