from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import sqlite3
from sklearn.linear_model import LinearRegression
import pandas as pd
import numpy as np
import pickle

app = FastAPI()
class Data(BaseModel):
    TV: float
    radio: float
    newpaper: float

class Data_all(BaseModel):
    TV: float
    radio: float
    newpaper: float
    sales: float

conn = sqlite3.connect('./data/adv.db')
cursor = conn.cursor()

# 1. Endpoint de predicción

@app.post('/predict')
async def get_prediction(data: Data):
    print('Hola')  # Para depuración

    # Extraer valores del body
    values_to_predict = [[data.TV, data.radio, data.newpaper]]  # Convertir en lista de listas

    # Obtener datos de entrenamiento desde la base de datos
    cursor.execute('SELECT TV, radio, newpaper FROM adv')
    X = np.array(cursor.fetchall())  # Convertir a array de NumPy

    cursor.execute('SELECT sales FROM adv')
    y = np.array(cursor.fetchall()).ravel()  # Convertir a array y a una dimensión

    #Cargo el modelo
    with open('./model.pkl', "rb") as file:
        lin_reg = pickle.load(file)

    # Realizar la predicción
    prediction = lin_reg.predict(values_to_predict)

    # Devolver la predicción en formato JSON
    return {"prediction": float(prediction[0])}


# 2. Endpoint de ingesta de datos

@app.post('/ingest')
async def get_prediction(data: Data_all):
    print('Hola')  # Para depuración

    # Obtener datos de entrenamiento desde la base de datos
    cursor.execute('SELECT * FROM adv')
    all_data = cursor.fetchall()

    all_data.append(data)

    return 'datos introducidos correctamente'


# 3. Endpoint de reentramiento del modelo

@app.get('/retrain')
async def get_prediction():

    # Obtener datos de entrenamiento desde la base de datos
    cursor.execute('SELECT TV, radio, newpaper FROM adv')
    X = np.array(cursor.fetchall())  # Convertir a array de NumPy

    cursor.execute('SELECT sales FROM adv')
    y = np.array(cursor.fetchall()).ravel()  # Convertir a array y a una dimensión
   
    #Cargo el modelo
    with open('./model.pkl', "rb") as file:
        lin_reg = pickle.load(file)

    #Reentreno el modelo
    lin_reg.fit(X, y)

    #Lo vuelvo a guardar
    with open('./model.pkl', 'wb') as archivo_salida:
        pickle.dump(lin_reg, archivo_salida)

    # Devolver la predicción en formato JSON
    return 'Modelo reentrenado'