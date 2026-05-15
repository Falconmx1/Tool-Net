import nmap
import subprocess
import sys

def scan_with_nmap(target, ports="1-1000", arguments="-sV -sC -O"):
    """
    Escaneo con Nmap real
    -sV: Versiones de servicios
    -sC: Scripts por defecto
    -O: Detección de OS
    """
    print(f"\n[🔍] Lanzando Nmap real contra {target}")
    print(f"[⚙️] Argumentos: {arguments}")
    print(f"[🎯] Puertos: {ports}\n")
    
    try:
        nm = nmap.PortScanner()
        scan_result = nm.scan(target, ports, arguments)
        
        results = []
        
        for host in nm.all_hosts():
            print(f"\n📡 Host: {host} ({nm[host].hostname()})")
            print(f"🖥️ Estado: {nm[host].state()}")
            
            if 'osmatch' in nm[host]:
                for os in nm[host]['osmatch']:
                    print(f"💿 OS: {os['name']} (accuracy: {os['accuracy']}%)")
            
            print("\n🔌 Puertos abiertos:")
            for proto in nm[host].all_protocols():
                ports_list = nm[host][proto].keys()
                for port in ports_list:
                    service = nm[host][proto][port]
                    info = f"  {port}/{proto} - {service['name']} - {service.get('product', '')} {service.get('version', '')}"
                    print(info)
                    results.append(info)
        
        # Guardar resultados
        with open("nmap_results.txt", "w") as f:
            f.write(str(nm))
        
        print(f"\n[+] Escaneo Nmap completado. {len(results)} servicios encontrados.")
        return results
        
    except nmap.PortScannerError as e:
        print(f"[!] Error Nmap: {e}")
        print("[*] ¿Tienes Nmap instalado? (sudo apt install nmap / pkg install nmap)")
        return []
    except Exception as e:
        print(f"[!] Error inesperado: {e}")
        return []

def quick_nmap_scan(target):
    """Escaneo rápido con Nmap (top 100 puertos)"""
    return scan_with_nmap(target, ports="1-100", arguments="-F -sV")

def full_nmap_scan(target):
    """Escaneo completo con Nmap"""
    return scan_with_nmap(target, ports="1-65535", arguments="-sV -O -sC")
