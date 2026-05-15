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

🛠️ Instalación completa (Ubuntu/Termux)
# Instalar dependencias del sistema
sudo apt update
sudo apt install nmap whois python3-pip -y

# En Termux
pkg install nmap whois python

# Crear entorno virtual
python3 -m venv venv
source venv/bin/activate

# Instalar librerías Python
pip install --upgrade pip
pip install python-nmap colorama scikit-learn pandas numpy requests shodan whois

# SpiderFoot tiene dependencias extras
pip install spiderfoot

# Ejecutar
python toolnet.py

⚠️ Para Windows
# Instalar Nmap desde https://nmap.org/download.html
# Agregar Nmap al PATH

pip install python-nmap colorama scikit-learn pandas numpy requests shodan whois spiderfoot
python toolnet.py
