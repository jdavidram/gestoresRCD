# ============================
# Entrenamiento de modelos RCD
# ============================

# importar librerías necesarias
import pandas as pd
import joblib
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, confusion_matrix

# ============================
# 1. Cargar los datos
# ============================
data = pd.read_csv("data/datos_modelo_random_forest.csv")

# Variables predictoras (comunes a todos los modelos)
X = data[["Municipio", "Latitud_Y", "Longitud_X"]]

# Diccionario para almacenar modelos
modelos = {}

# ============================
# 2. Definir los modelos
# ============================

# --- Modelo Pavimento ---
y = data["areaPavimento"]
Xtr, Xte, ytr, yte = train_test_split(X, y, test_size=0.3, random_state=42, stratify=y)

modelo_pavimento = RandomForestClassifier(
    criterion='entropy',
    max_depth=None,
    max_features='sqrt',
    min_samples_leaf=1,
    min_samples_split=2,
    n_estimators=100,
    random_state=42
)
modelo_pavimento.fit(Xtr, ytr)
print("\n== Pavimento ==")
print(confusion_matrix(yte, modelo_pavimento.predict(Xte)))
print(classification_report(yte, modelo_pavimento.predict(Xte)))
modelos["pavimento"] = modelo_pavimento

# --- Modelo Concreto ---
y = data["areaConcreto"]
Xtr, Xte, ytr, yte = train_test_split(X, y, test_size=0.3, random_state=42, stratify=y)

modelo_concreto = RandomForestClassifier(
    criterion='gini',
    max_depth=10,
    max_features='sqrt',
    min_samples_leaf=1,
    min_samples_split=2,
    n_estimators=100,
    random_state=42
)
modelo_concreto.fit(Xtr, ytr)
print("\n== Concreto ==")
print(confusion_matrix(yte, modelo_concreto.predict(Xte)))
print(classification_report(yte, modelo_concreto.predict(Xte)))
modelos["concreto"] = modelo_concreto

# --- Modelo Roca ---
y = data["areaRoca"]
Xtr, Xte, ytr, yte = train_test_split(X, y, test_size=0.3, random_state=42, stratify=y)

modelo_roca = RandomForestClassifier(
    criterion='gini',
    max_depth=None,
    max_features='sqrt',
    min_samples_leaf=1,
    min_samples_split=2,
    n_estimators=100,
    random_state=42
)
modelo_roca.fit(Xtr, ytr)
print("\n== Roca ==")
print(confusion_matrix(yte, modelo_roca.predict(Xte)))
print(classification_report(yte, modelo_roca.predict(Xte)))
modelos["roca"] = modelo_roca

# --- Modelo Tierras ---
y = data["areaTierras"]
Xtr, Xte, ytr, yte = train_test_split(X, y, test_size=0.3, random_state=42, stratify=y)

modelo_tierras = RandomForestClassifier(
    criterion='entropy',
    max_depth=10,
    max_features='sqrt',
    min_samples_leaf=1,
    min_samples_split=2,
    n_estimators=200,
    random_state=42
)
modelo_tierras.fit(Xtr, ytr)
print("\n== Tierras ==")
print(confusion_matrix(yte, modelo_tierras.predict(Xte)))
print(classification_report(yte, modelo_tierras.predict(Xte)))
modelos["tierras"] = modelo_tierras

# ============================
# 3. Guardar modelos entrenados
# ============================
for nombre, modelo in modelos.items():
    filename = f"predictiveModels/modelo_{nombre}.pkl"
    joblib.dump(modelo, filename)
    print(f"✅ Modelo {nombre} guardado como {filename}")