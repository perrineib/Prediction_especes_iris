from fastapi import FastAPI
from pydantic import BaseModel
import joblib #on appelle joblib pour trouver le package
import numpy as np

app = FastAPI()

# Charger le modèle et les métriques au démarrage
model_data = joblib.load('model.pkl')
model = model_data['model']
model_accuracy = model_data['accuracy']
confusion_matrix = model_data.get('confusion_matrix', None)
classification_report = model_data.get('classification_report', None)

class IrisFeatures(BaseModel):
    features: list[float]

@app.get("/")
def read_root():
    return {
        "message": "API de prédiction Iris",
        "model_accuracy": round(model_accuracy * 100, 2),
        "confusion_matrix": confusion_matrix,
        "classification_report": classification_report
    }

@app.post("/")
def predict(data: IrisFeatures):
    # Convertir les features en array numpy
    features_array = np.array(data.features).reshape(1, -1)

    # Faire la prédiction
    prediction = model.predict(features_array)

    # Obtenir les probabilités pour chaque classe
    probabilities = model.predict_proba(features_array)

    # Probabilité de la classe prédite
    confidence = float(probabilities[0][prediction[0]]) * 100

    return {
        "prediction": int(prediction[0]),
        "confidence": round(confidence, 2),
        "probabilities": {
            "Setosa": round(float(probabilities[0][0]) * 100, 2),
            "Versicolor": round(float(probabilities[0][1]) * 100, 2),
            "Virginica": round(float(probabilities[0][2]) * 100, 2)
        },
        "model_accuracy": round(model_accuracy * 100, 2)
    }
