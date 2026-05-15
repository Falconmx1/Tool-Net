from ml_engine import NetworkML
import joblib

# Entrenar con más datos
ml = NetworkML()
# ... agregar más datos de entrenamiento ...
joblib.dump(ml.model, "network_model_advanced.pkl")
