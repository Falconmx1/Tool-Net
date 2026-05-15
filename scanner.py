import socket
import sys
import threading
from datetime import datetime

def scan_port(target, port, results, index):
    """Escanea un puerto individual"""
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(0.5)
        result = sock.connect_ex((target, port))
        if result == 0:
            try:
                service = socket.getservbyport(port)
            except:
                service = "desconocido"
            results[index] = f"Puerto {port} ABIERTO - {service}"
        sock.close()
    except:
        pass

def scan_network(target, start_port, end_port):
    """Escaneo multithreading bizarro"""
    print(f"\n[+] Escaneando {target} desde puerto {start_port} hasta {end_port}")
    print("[IA] Modo: Paciencia nivel dios\n")
    
    results = [None] * (end_port - start_port + 1)
    threads = []
    
    for port in range(start_port, end_port + 1):
        index = port - start_port
        t = threading.Thread(target=scan_port, args=(target, port, results, index))
        t.start()
        threads.append(t)
    
    for t in threads:
        t.join()
    
    open_ports = [r for r in results if r is not None]
    
    # Guardar resultados
    with open("results.txt", "w") as f:
        for res in open_ports:
            print(res)
            f.write(res + "\n")
    
    print(f"\n[+] Escaneo completado. {len(open_ports)} puertos abiertos encontrados.")
    print("[*] Resultados guardados en results.txt")
    return open_ports

def quick_scan(target):
    """Escaneo rápido: puertos comunes"""
    common_ports = [21, 22, 23, 25, 53, 80, 110, 135, 139, 143, 443, 445, 
                    993, 995, 1723, 3306, 3389, 5432, 5900, 8080, 8443]
    
    print(f"\n[+] Escaneo rápido a {target} (solo puertos comunes)")
    results = []
    
    for port in common_ports:
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(0.3)
            result = sock.connect_ex((target, port))
            if result == 0:
                try:
                    service = socket.getservbyport(port)
                except:
                    service = "desconocido"
                msg = f"Puerto {port} ABIERTO - {service}"
                print(msg)
                results.append(msg)
            sock.close()
        except:
            pass
    
    with open("results.txt", "w") as f:
        for res in results:
            f.write(res + "\n")
    
    print(f"\n[+] Escaneo rápido completado. {len(results)} puertos abiertos.")
    return results
