import joblib
import pandas as pd
import numpy as np

def cargar_modelo(nombre_modelo):
    return joblib.load(f"predictiveModels/modelo_{nombre_modelo}.pkl")

def predecir(nombre_modelo, datos_nuevos):
    modelo = cargar_modelo(nombre_modelo)
    X_nuevo = pd.DataFrame([datos_nuevos], columns=["Municipio", "Latitud_Y", "Longitud_X"])
    return modelo.predict(X_nuevo)[0]

def gestor_mas_cercano(df, lat, lon):
    if df.empty:
        return None
    df = df.copy()
    df["distancia"] = np.sqrt((df["Y"] - lat)**2 + (df["X"] - lon)**2)
    return df.loc[df["distancia"].idxmin()]