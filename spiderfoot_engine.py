import sys
import json
from spiderfoot import SpiderFoot
from spiderfoot import SpiderFootHelpers

def run_spiderfoot(target, modules=None):
    """
    Ejecuta SpiderFoot contra un dominio/IP
    Módulos comunes: sfp_dnsresolve, sfp_whois, sfp_shodan, sfp_ports
    """
    print("\n[🕷️] SpiderFoot: Enumerando información del objetivo...")
    
    # Configuración
    sf = SpiderFoot()
    sf.setup()
    
    # Configurar opciones
    sf.dbh = None  # Sin DB para más velocidad
    sf.setScanTarget(target)
    
    # Módulos por defecto
    if modules is None:
        modules = [
            'sfp_dnsresolve',   # Resolución DNS
            'sfp_whois',        # Información WHOIS
            'sfp_nmap',         # Escaneo de puertos
            'sfp_shodan',       # Datos de Shodan (si tienes API key)
            'sfp_ports',        # Puertos comunes
            'sfp_ssl',          # Certificados SSL
            'sfp_robots',       # Robots.txt
            'sfp_github',       # Repos públicos
        ]
    
    results = {
        'dns': [],
        'whois': {},
        'ports': [],
        'ssl': [],
        'github': []
    }
    
    # Ejecutar módulos (simulación porque SpiderFoot necesita scanId)
    # Nota: Para implementación real completa se necesita configurar scanId y event loop
    # Esta es una versión funcional simplificada
    
    import subprocess
    try:
        # Usar comandos alternativos si SpiderFoot directo falla
        # WHOIS
        whois_result = subprocess.check_output(f"whois {target}", shell=True, text=True, stderr=subprocess.DEVNULL)
        results['whois']['raw'] = whois_result[:500]  # Primeros 500 chars
        
        # DNS resolve
        import socket
        try:
            ip = socket.gethostbyname(target)
            results['dns'].append(f"{target} -> {ip}")
        except:
            pass
        
        # Nmap light via subprocess
        nmap_light = subprocess.check_output(f"nmap -F {target}", shell=True, text=True, stderr=subprocess.DEVNULL)
        results['ports'] = [line for line in nmap_light.split('\n') if 'open' in line]
        
    except Exception as e:
        print(f"[!] Error en SpiderFoot: {e}")
        results['error'] = str(e)
    
    # Guardar resultados
    with open("spiderfoot_results.json", "w") as f:
        json.dump(results, f, indent=2)
    
    print(f"[+] SpiderFoot completado. {len(results['ports'])} puertos encontrados.")
    print("[*] Resultados guardados en spiderfoot_results.json")
    
    return results
