# Proyecto de Predicción y Reentrenamiento de Modelo

Este proyecto proporciona una API para leer datos de una base de datos, realizar predicciones y reentrenar el modelo cuando sea necesario.

## Estructura del Proyecto

```
├── data/                   # Carpeta para datos (si aplica)
├── api_model_2.py          # Código principal de la API
├── docker-compose.yml      # Configuración de Docker Compose
├── Dockerfile              # Dockerfile para contenerizar la aplicación
├── model.pkl               # Archivo del modelo entrenado
├── README.md               # Documentación del proyecto
├── requirements.txt        # Dependencias del proyecto
├── test_api.py             # Script para probar la API
```

## Instalación

### Requisitos
- Python 3.11
- Docker y Docker Compose (opcional si se usa contenedorización)

### Instalación Manual

1. Clonar el repositorio:
   ```bash
   git clone <repositorio>
   cd <repositorio>
   ```
2. Crear un entorno virtual y activar:
   ```bash
   python -m venv venv
   source venv/bin/activate  # En Windows usar: venv\Scripts\activate
   ```
3. Instalar las dependencias:
   ```bash
   pip install -r requirements.txt
   ```

### Uso con Docker

1. Construir la imagen:
   ```bash
   docker build -t api_model .
   ```
2. Ejecutar el contenedor:
   ```bash
   docker run -p 8000:8000 api_model
   ```

## Endpoints de la API

### `POST /predict`
Realiza una predicción con los datos ingresados en el cuerpo de la solicitud.

**Ejemplo de uso:**
```bash
curl -X POST "http://localhost:8000/predict" -H "Content-Type: application/json" -d '{"TV": valor, "radio": valor, "newpaper": valor}'
```

### `POST /ingest`
Ingresa nuevos datos a la base de datos.

**Ejemplo de uso:**
```bash
curl -X POST "http://localhost:8000/ingest" -H "Content-Type: application/json" -d '{"data": [<datos>]}'
```

### `POST /retrain`
Reentrena el modelo con nuevos datos.

**Ejemplo de uso:**
```bash
curl -X POST "http://localhost:8000/retrain"
```

## Pruebas
Para probar la API, ejecuta:
```bash
python test_api.py
```

