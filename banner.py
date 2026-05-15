import random
from colorama import init, Fore, Style

init(autoreset=True)

def show_banner():
    frases_bizarras = [
        "🧠 IA: 'Este puerto huele a vulnerabilidad'",
        "🎭 Escaneando como si fuera 1999... pero con IA rancia",
        "👾 Tool-Net: porque nmap es muy serio",
        "🌀 Modo esquizofrenia digital activado",
        "🔮 Predicción IA: Vas a encontrar algo que no querías ver",
        "💀 Si esto falla, culpa al kernel"
    ]
    
    ascii_banner = f"""
{Fore.MAGENTA}╔══════════════════════════════════════════╗
║  {Fore.CYAN} _____            _   _  __      _   {Fore.MAGENTA}   ║
║  {Fore.CYAN}|_   _|          | \ | | \ \    / |  {Fore.MAGENTA}   ║
║  {Fore.CYAN}  | | ___   ___  |  \| |  \ \  / /   {Fore.MAGENTA}   ║
║  {Fore.CYAN}  | |/ _ \ / _ \ | . ` |   \ \/ /    {Fore.MAGENTA}   ║
║  {Fore.CYAN}  | | (_) | (_) || |\  |    \  /     {Fore.MAGENTA}   ║
║  {Fore.CYAN}  \_/\___/ \___/ \_| \_|     \/      {Fore.MAGENTA}   ║
║                                          ║
║  {Fore.YELLOW}{random.choice(frases_bizarras)}{Fore.MAGENTA}  ║
╚══════════════════════════════════════════╝{Style.RESET_ALL}
"""
    print(ascii_banner)
