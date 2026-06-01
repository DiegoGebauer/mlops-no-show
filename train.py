import pandas as pd
import joblib

from sklearn.ensemble import RandomForestClassifier
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder
from sklearn.pipeline import Pipeline


data = pd.DataFrame({
    "edad": [25, 40, 62, 35, 50, 29, 70, 45, 33, 58],
    "dias_anticipacion": [2, 10, 30, 1, 15, 3, 40, 7, 5, 20],
    "hora_cita": [9, 11, 16, 8, 14, 10, 17, 12, 15, 13],
    "dia_semana": [1, 2, 4, 1, 3, 5, 4, 2, 3, 5],
    "especialidad": [
        "imagenologia", "medicina_general", "imagenologia",
        "traumatologia", "cardiologia", "medicina_general",
        "imagenologia", "traumatologia", "cardiologia", "imagenologia"
    ],
    "tipo_paciente": [
        "fonasa", "isapre", "fonasa", "particular", "isapre",
        "fonasa", "fonasa", "particular", "isapre", "fonasa"
    ],
    "no_show": [0, 0, 1, 0, 0, 0, 1, 0, 1, 1]
})

X = data.drop(columns="no_show")
y = data["no_show"]

categorical_features = ["especialidad", "tipo_paciente"]
numeric_features = ["edad", "dias_anticipacion", "hora_cita", "dia_semana"]

preprocessor = ColumnTransformer([
    ("categoricas", OneHotEncoder(handle_unknown="ignore"), categorical_features),
    ("numericas", "passthrough", numeric_features)
])

model = Pipeline([
    ("preprocessor", preprocessor),
    ("classifier", RandomForestClassifier(random_state=42))
])

model.fit(X, y)

joblib.dump(model, "model.pkl")

print("Modelo entrenado y guardado como model.pkl")