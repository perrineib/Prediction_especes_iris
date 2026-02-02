from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix

import joblib #pour créer le pickl
import json

#chargement des données

iris = load_iris()
X = iris.data #data et target: convention sklearn pour ses datasets
y = iris.target


#diviser en train/test:
X_train, X_test, y_train, y_test = train_test_split(X,y,test_size=0.2,random_state=42)

#Créer et entraîner le modèle 
model = RandomForestClassifier(n_estimators=100,random_state=42)
model.fit(X_train,y_train)

#Evaluer le modèle
y_pred = model.predict(X_test)
accuracy = accuracy_score(y_test,y_pred)

print(f"Accuracy du modèle : {accuracy * 100:.2f}%")

# Calculer la matrice de confusion
conf_matrix = confusion_matrix(y_test, y_pred)

# Calculer le classification report
class_report = classification_report(y_test, y_pred, target_names=iris.target_names, output_dict=True)

# Afficher les métriques
print("\nMatrice de confusion:")
print(conf_matrix)
print("\nClassification Report:")
print(classification_report(y_test, y_pred, target_names=iris.target_names))

#Sauvegarder l'accuracy avec le modèle et les métriques
model_data = {
    'model': model,
    'accuracy': accuracy,
    'confusion_matrix': conf_matrix.tolist(),
    'classification_report': class_report
}

#Transformation en pickl
joblib.dump(model_data,'model.pkl')