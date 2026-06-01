# MLOps No Show

Proyecto de Machine Learning para la predicción de inasistencia (No-Show) a citas médicas.

## Tecnologías utilizadas

* Python
* Scikit-Learn
* Flask
* Git
* GitHub

## Estructura del proyecto

```text
no-show-mlops/
│
├── app.py
├── train.py
├── model.pkl
├── requirements.txt
└── README.md
```

## Entrenar el modelo

```bash
python train.py
```

## Ejecutar la API

```bash
python app.py
```

La API estará disponible en:

```text
http://127.0.0.1:5000
```

## Endpoint de prueba

```text
GET /
```

Respuesta:

```json
{
  "message": "API No-Show funcionando"
}
```

## Autor

Diego Gebauer
