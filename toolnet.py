#!/usr/bin/env python3
# Tool-Net 2.0 - Full Nuclear Edition

import sys
import os
import platform
from banner import show_banner
from scanner import scan_with_nmap, quick_nmap_scan, full_nmap_scan
from spiderfoot_engine import run_spiderfoot
from ml_engine import ml_engine
from database import ToolNetDB

def clear_screen():
    os.system('clear' if platform.system() != 'Windows' else 'cls')

def main():
    db = ToolNetDB()
    
    while True:
        clear_screen()
        show_banner()
        
        print("\n" + "═"*50)
        print(" 🛠️  TOOL-NET 2.0 | FULL NUCLEAR EDITION")
        print("═"*50)
        print(" [1] Escaneo Nmap (rápido)")
        print(" [2] Escaneo Nmap (completo - 65535 puertos)")
        print(" [3] Escaneo Nmap (personalizado)")
        print(" [4] SpiderFoot OSINT (reconocimiento)")
        print(" [5] ML-Analyzer (analizar resultados guardados)")
        print(" [6] Historial de escaneos")
        print(" [7] Escaneo completo (Nmap + SpiderFoot + ML)")
        print(" [8] Salir")
        print("═"*50)
        
        opcion = input("\n🎯 Tool-Net> ").strip()
        
        if opcion == "1":
            target = input("🌐 IP o dominio: ")
            results = quick_nmap_scan(target)
            if results:
                risk = ml_engine.predict_risk(results)
                db.save_scan(target, "nmap_rapido", len(results), risk, results)
            input("\n[Enter] para continuar...")
        
        elif opcion == "2":
            target = input("🌐 IP o dominio: ")
            results = full_nmap_scan(target)
            if results:
                risk = ml_engine.predict_risk(results)
                db.save_scan(target, "nmap_completo", len(results), risk, results)
            input("\n[Enter] para continuar...")
        
        elif opcion == "3":
            target = input("🌐 IP o dominio: ")
            ports = input("🔌 Puertos (ej: 22,80,443 o 1-1000): ")
            args = input("⚙️ Argumentos Nmap (ej: -sV -O): ") or "-sV"
            results = scan_with_nmap(target, ports, args)
            if results:
                risk = ml_engine.predict_risk(results)
                db.save_scan(target, "nmap_personalizado", len(results), risk, results)
            input("\n[Enter] para continuar...")
        
        elif opcion == "4":
            target = input("🌐 Dominio (ej: google.com): ")
            run_spiderfoot(target)
            input("\n[Enter] para continuar...")
        
        elif opcion == "5":
            archivo = input("📁 Archivo de resultados (nmap_results.txt): ")
            try:
                with open(archivo, 'r') as f:
                    data = f.read()
                ml_engine.predict_risk(data)
            except:
                print("[!] Archivo no encontrado")
            input("\n[Enter] para continuar...")
        
        elif opcion == "6":
            history = db.get_history()
            print("\n📜 HISTORIAL DE ESCANEOS:")
            print("═"*60)
            for h in history:
                print(f"ID:{h[0]} | {h[1]} | {h[2][:19]} | {h[3]} | {h[4]} puertos | {h[5]}")
            input("\n[Enter] para continuar...")
        
        elif opcion == "7":
            target = input("🌐 IP o dominio: ")
            print("\n🔥 LANZANDO ESCANEO COMPLETO...\n")
            
            # Paso 1: Nmap
            print("[1/3] Nmap scan")
            nmap_results = full_nmap_scan(target)
            
            # Paso 2: SpiderFoot
            print("\n[2/3] SpiderFoot OSINT")
            sf_results = run_spiderfoot(target)
            
            # Paso 3: ML Analysis
            print("\n[3/3] Machine Learning Analysis")
            if nmap_results:
                risk = ml_engine.predict_risk(nmap_results)
                db.save_scan(target, "completo", len(nmap_results), risk, nmap_results + str(sf_results))
            
            print("\n✅ Escaneo completo finalizado")
            input("\n[Enter] para continuar...")
        
        elif opcion == "8":
            print("\n👋 Saliendo... ¡Que la fuerza del escaneo te acompañe!")
            db.close()
            sys.exit(0)
        
        else:
            print("[!] Opción no válida")
            input("\n[Enter] para continuar...")

if __name__ == "__main__":
    main()
