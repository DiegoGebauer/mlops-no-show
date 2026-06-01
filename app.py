from flask import Flask, request, jsonify
import pandas as pd
import joblib

app = Flask(__name__)

model = joblib.load("model.pkl")


@app.route("/")
def home():
    return {"message": "API No-Show funcionando"}


@app.route("/predict", methods=["POST"])
def predict():
    data = request.json

    input_data = pd.DataFrame([{
        "edad": data["edad"],
        "dias_anticipacion": data["dias_anticipacion"],
        "hora_cita": data["hora_cita"],
        "dia_semana": data["dia_semana"],
        "especialidad": data["especialidad"],
        "tipo_paciente": data["tipo_paciente"]
    }])

    prediction = model.predict(input_data)[0]
    probability = model.predict_proba(input_data)[0][1]

    return jsonify({
        "no_show_predicho": int(prediction),
        "probabilidad_no_show": round(float(probability), 3)
    })


if __name__ == "__main__":
    app.run(debug=True)