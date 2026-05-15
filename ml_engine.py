import numpy as np
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import StandardScaler
import joblib
import os
import socket

class NetworkML:
    def __init__(self):
        self.model = None
        self.scaler = StandardScaler()
        self.model_file = "network_model.pkl"
        
        # Entrenar o cargar modelo
        if os.path.exists(self.model_file):
            self.model = joblib.load(self.model_file)
            print("[ML] Modelo cargado desde disco")
        else:
            self.train_model()
    
    def train_model(self):
        """Entrena un modelo de Random Forest con datos sintéticos realistas"""
        print("[ML] Entrenando modelo de IA con datos de red...")
        
        # Datos sintéticos de entrenamiento
        # Características: [puertos_abiertos, servicios_web, servicios_db, servicios_ftp, servicios_ssh, vulnerabilidad_conocida]
        X_train = np.array([
            [1, 0, 0, 0, 1, 0],   # Solo SSH (seguro)
            [2, 1, 0, 0, 1, 0],   # SSH + HTTP
            [5, 2, 1, 0, 1, 1],   # Múltiples servicios, MySQL
            [10, 3, 2, 1, 1, 1],  # Muchos puertos, vulnerable
            [0, 0, 0, 0, 0, 0],   # Sin puertos
            [3, 1, 0, 1, 0, 1],   # FTP abierto
            [4, 2, 1, 0, 1, 0],   # Web + DB
            [20, 5, 3, 2, 1, 1],  # Muy expuesto
            [2, 0, 0, 0, 0, 0],   # Solo puertos no comunes
            [7, 3, 1, 1, 1, 1],   # Alto riesgo
        ])
        
        # Etiquetas: 0 = seguro, 1 = riesgo medio, 2 = peligro
        y_train = np.array([0, 1, 2, 2, 0, 2, 1, 2, 0, 2])
        
        # Escalar
        X_scaled = self.scaler.fit_transform(X_train)
        
        # Entrenar Random Forest
        self.model = RandomForestClassifier(n_estimators=100, random_state=42)
        self.model.fit(X_scaled, y_train)
        
        # Guardar modelo
        joblib.dump(self.model, self.model_file)
        print("[ML] Modelo entrenado y guardado")
    
    def extract_features(self, scan_results):
        """Extrae características numéricas de los resultados del escaneo"""
        if isinstance(scan_results, list):
            scan_text = " ".join(scan_results)
        else:
            scan_text = str(scan_results)
        
        # Contar puertos abiertos
        puertos_abiertos = scan_text.lower().count("abierto") + scan_text.lower().count("open")
        
        # Detectar servicios específicos
        servicios_web = scan_text.lower().count("80") + scan_text.lower().count("443") + scan_text.lower().count("8080")
        servicios_db = scan_text.lower().count("3306") + scan_text.lower().count("5432") + scan_text.lower().count("27017")
        servicios_ftp = scan_text.lower().count("21") + scan_text.lower().count("20")
        servicios_ssh = scan_text.lower().count("22")
        
        # Palabras clave de vulnerabilidad
        vulnerabilidad = 1 if ("anonymous" in scan_text.lower() or "default" in scan_text.lower() or "weak" in scan_text.lower()) else 0
        
        features = [puertos_abiertos, servicios_web, servicios_db, servicios_ftp, servicios_ssh, vulnerabilidad]
        return np.array(features).reshape(1, -1)
    
    def predict_risk(self, scan_results):
        """Predice nivel de riesgo usando ML"""
        if self.model is None:
            return "⚠️ Modelo no disponible"
        
        features = self.extract_features(scan_results)
        features_scaled = self.scaler.transform(features)
        prediction = self.model.predict(features_scaled)[0]
        probabilities = self.model.predict_proba(features_scaled)[0]
        
        riesgo_map = {0: "🟢 SEGURO", 1: "🟡 RIESGO MEDIO", 2: "🔴 PELIGRO"}
        colores = {0: "\033[92m", 1: "\033[93m", 2: "\033[91m"}
        
        print("\n" + "="*50)
        print(f"[🤖 ML - Random Forest]")
        print(f"📊 Clasificación: {colores[prediction]}{riesgo_map[prediction]}\033[0m")
        print(f"📈 Confianza: {max(probabilities)*100:.1f}%")
        print(f"🎲 Probabilidades -> Seguro: {probabilities[0]:.2f} | Medio: {probabilities[1]:.2f} | Peligro: {probabilities[2]:.2f}")
        
        # Recomendaciones específicas
        if prediction == 2:
            print("\n🔥 RECOMENDACIÓN: Cierra puertos innecesarios, actualiza servicios y revisa logs")
        elif prediction == 1:
            print("\n⚡ RECOMENDACIÓN: Revisa configuraciones y aplica parches de seguridad")
        else:
            print("\n✅ RECOMENDACIÓN: Sigue así, pero mantén monitoreo activo")
        
        return riesgo_map[prediction]

# Instancia global
ml_engine = NetworkML()
