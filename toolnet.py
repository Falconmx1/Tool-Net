#!/usr/bin/env python3
# Tool-Net - Escaneo bizarro con IA

import sys
import os
import platform
from banner import show_banner
from scanner import scan_network, quick_scan
from ia_engine import ia_analyze

def clear_screen():
    os.system('clear' if platform.system() != 'Windows' else 'cls')

def main():
    clear_screen()
    show_banner()
    
    print("\n[1] Escaneo rápido (puertos comunes)")
    print("[2] Escaneo completo (1-1024)")
    print("[3] Escaneo personalizado")
    print("[4] IA: Analizar resultados")
    print("[5] Salir")
    
    opcion = input("\nTool-Net> ").strip()
    
    if opcion == "1":
        target = input("IP o dominio: ")
        results = quick_scan(target)
        ia_analyze(results)
    elif opcion == "2":
        target = input("IP o dominio: ")
        results = scan_network(target, 1, 1024)
        ia_analyze(results)
    elif opcion == "3":
        target = input("IP o dominio: ")
        start = int(input("Puerto inicial: "))
        end = int(input("Puerto final: "))
        results = scan_network(target, start, end)
        ia_analyze(results)
    elif opcion == "4":
        archivo = input("Archivo de resultados (results.txt): ")
        if os.path.exists(archivo):
            with open(archivo, 'r') as f:
                data = f.read()
            ia_analyze(data)
        else:
            print("[!] Archivo no encontrado")
    elif opcion == "5":
        print("[*] Saliendo... que la fuerza te acompañe bizarramente")
        sys.exit(0)
    else:
        print("[!] Opción no válida")

if __name__ == "__main__":
    main()
