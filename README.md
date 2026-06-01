# MLOps No Show

Proyecto de aprendizaje desarrollado para introducir conceptos fundamentales de MLOps utilizando Python, Scikit-Learn, Flask, Git y GitHub.

El objetivo de este proyecto fue construir un flujo básico de Machine Learning que permitiera:

* Entrenar un modelo de clasificación.
* Guardar el modelo entrenado.
* Exponer el modelo mediante una API REST con Flask.
* Gestionar versiones del código mediante Git.
* Publicar y mantener el proyecto en GitHub.

Los datos utilizados en este proyecto fueron generados manualmente con fines educativos y no corresponden a información real de pacientes. La finalidad principal fue comprender el flujo de trabajo de un proyecto de Machine Learning orientado a producción antes de avanzar hacia herramientas más avanzadas de MLOps como MLflow, Docker, CI/CD y despliegue en la nube.

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

## Próximos pasos

* Incorporar MLflow para el seguimiento de experimentos.
* Dockerizar la aplicación.
* Implementar pruebas automatizadas.
* Construir un pipeline de CI/CD con GitHub Actions.
* Desplegar la aplicación en un servicio cloud.

## Autor

Diego Gebauer
