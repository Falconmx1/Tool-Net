# 🌐 Tool-Net

**Tool-Net** es una herramienta de escaneo de red con un toque de IA (básica pero efectiva) y un banner **bizarro/simple** que te recibirá en cada ejecución. Ideal para pentesters, curiosos o gente que quiere sentir que hackea la Matrix desde Ubuntu, Termux o Windows.

## 🧠 ¿Qué hace?
- Escaneo de puertos (como nmap pero más feo).
- Enumeración de dominios (inspirado en SpiderFoot).
- Clasificación con IA tonta: te dice si el host "huele mal" o "parece seguro" según los puertos abiertos.
- Banner personalizable (puedes poner frases raras o ASCII art turbio).

## 🛠️ Instalación
```bash
git clone https://github.com/Falconmx1/Tool-Net
cd Tool-Net
python -m venv venv
source venv/bin/activate  # En Windows: venv\Scripts\activate
pip install -r requirements.txt
python toolnet.py

🎭 Banner de ejemplo
  _____            _   _  __      _   
 |_   _|          | \ | | \ \    / |  
   | | ___   ___  |  \| |  \ \  / /  
   | |/ _ \ / _ \ | . ` |   \ \/ /   
   | | (_) | (_) || |\  |    \  /    
   \_/\___/ \___/ \_| \_/     \/     
                                     
[+] Tool-Net ready for weird scanning...
[IA] Modo: paranoico nivel 3

🚀 Paso final: Instalar y ejecutar
python3 -m venv venv
source venv/bin/activate  # En Windows: venv\Scripts\activate
pip install -r requirements.txt
python3 toolnet.py

🎯 Para Termux (extra)
pkg install python
pip install colorama
python toolnet.py

🪟 Para Windows

    Instalar Python desde python.org

    Ejecutar como admin si quieres escanear localhost

    Desactivar firewall para pruebas
