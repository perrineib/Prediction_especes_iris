#  🌺 Application de Prédiction Iris 🌺

Cette application basée sur le machine learning sert à prédire les espèces d'iris, elle est développée avec FastAPI et Streamlit, déployée avec Docker.

##  Description

Cette application permet de prédire l'espèce d'une fleur d'iris (Setosa, Versicolor ou Virginica) à partir des mesures de ses pétales et sépales. Elle utilise un modèle Random Forest entraîné sur le dataset Iris.

### Fonctionnalités

- **Prédiction interactive** : Interface utilisateur pour prédire l'espèce d'iris en fonction des paramètres sépales et pétales
- **Visualisation des résultats** : Affichage des probabilités et du niveau de confiance
- **Informations contextuelles** : Résumés des espèces photos et liens Wikipedia
- **Métriques du modèle** : Accuracy, matrice de confusion, métriques par espèce (précision, rappel, F1-score)

##  Architecture

Le projet est composé de deux services Docker :

- **Backend (FastAPI)** : API REST pour les prédictions
- **Frontend (Streamlit)** : Interface utilisateur web

```
Prediction_especes_iris/
├── server/              # Backend FastAPI
│   ├── app.py          # API REST
│   ├── train.py        # Entraînement du modèle
│   ├── model.pkl       # Modèle entraîné
│   ├── requirements.txt
│   └── Dockerfile
├── client/             # Frontend Streamlit
│   ├── app.py         # Interface utilisateur
│   ├── requirements.txt
│   ├── Dockerfile
│   └── .streamlit/
│       └── config.toml
└── docker-compose.yml
```

##  Installation et lancement de l'application

### Prérequis

- Docker Desktop

### Démarrage

1. Cloner le repository
```bash
git clone https://github.com/perrineib/Prediction_especes_iris.git
cd Prediction_especes_iris
```

2. Lancer l'application avec Docker compose
```bash
docker-compose up --build
```

3. Accéder à l'application
- **Interface utilisateur** : http://localhost:8501
- **API Backend** : http://localhost:8000

### Arrêt

```bash
docker-compose down
```

##  Le Modèle

### Dataset
- **Source** : Dataset Iris (scikit-learn)
- **Échantillons** : 150 (50 par espèce)
- **Features** : 4 caractéristiques
  - Longueur du sépale (cm)
  - Largeur du sépale (cm)
  - Longueur du pétale (cm)
  - Largeur du pétale (cm)
- **Classes** : 3 espèces (Setosa, Versicolor, Virginica)

### Modèle
- **Algorithme** : Random Forest
- **Nombre d'arbres** : 100
- **Split** : 80% entraînement / 20% test
- **Performance** : ~100% accuracy


##  Technologies Utilisées

- **Backend** : FastAPI, scikit-learn, joblib
- **Frontend** : Streamlit
- **DevOps** : Docker, Docker Compose

##  Interface Utilisateur

L'interface propose deux pages accessibles via une barre latérale :

- **Prédiction** : Interface interactive pour prédire l'espèce d'iris
- **Modèle & Data** : Métriques de performance et informations sur le dataset

##  Notes de Développement

### Modifier le nombre d'arbres

Pour ajuster la complexité du modèle, éditer `server/train.py` :

```python
model = RandomForestClassifier(n_estimators=100, random_state=42)
```

Puis reconstruire les containers :

```bash
docker-compose down
docker-compose up --build
```

### Personnalisation du thème

Le thème de l'interface peut être modifié dans `client/.streamlit/config.toml`.

##  Licence

Projet universitaire - MASTER SISE

##  Auteur

PERRINE IBOUROI
