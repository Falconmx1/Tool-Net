import random
from colorama import Fore, Style

def show_banner():
    frases = [
        "Escaneando tu wifi como si fuera 1999",
        "IA: 'Esto parece inseguro... o no?'",
        "Bienvenido a Tool-Net, deja tu cordura en la puerta",
        "[*] Si ves muchos puertos abiertos, reza un padre nuestro"
    ]
    print(Fore.MAGENTA + """
  _____            _   _  __      _   
 |_   _|          | \ | | \ \    / |  
   | | ___   ___  |  \| |  \ \  / /  
   | |/ _ \ / _ \ | . ` |   \ \/ /   
   | | (_) | (_) || |\  |    \  /    
   \_/\___/ \___/ \_| \_|     \/     
    """ + Style.RESET_ALL)
    print(Fore.CYAN + random.choice(frases) + Style.RESET_ALL)
