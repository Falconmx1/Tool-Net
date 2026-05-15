import random
from colorama import Fore, Style

def ia_analyze(data):
    """Análisis bizarro con IA trucha"""
    print("\n" + Fore.CYAN + "="*50)
    print("[🧠 IA BIZARRA ANALIZANDO...]")
    print("="*50 + Style.RESET_ALL)
    
    if isinstance(data, list):
        text = " ".join(data)
    else:
        text = str(data)
    
    # Reglas de la "IA"
    riesgos = 0
    recomendaciones = []
    
    if "22" in text and "abierto" in text.lower():
        riesgos += 2
        recomendaciones.append("⚠️ SSH abierto -> Cambia la contraseña de root")
    
    if "80" in text and "abierto" in text.lower():
        riesgos += 1
        recomendaciones.append("🌐 HTTP expuesto -> ¿Tienes WordPress sin actualizar?")
    
    if "443" in text and "abierto" in text.lower():
        riesgos -= 1
        recomendaciones.append("🔒 HTTPS presente -> Algo de seguridad tienes")
    
    if "3306" in text and "abierto" in text.lower():
        riesgos += 3
        recomendaciones.append("💀 MySQL expuesto -> Te van a robar la base de datos")
    
    if "3389" in text and "abierto" in text.lower():
        riesgos += 3
        recomendaciones.append("🪟 RDP abierto -> Objetivo favorito de ransomware")
    
    if "21" in text and "abierto" in text.lower():
        riesgos += 2
        recomendaciones.append("📁 FTP anónimo? Probablemente")
    
    # Puertos abiertos totales
    puertos_abiertos = text.count("ABIERTO")
    if puertos_abiertos > 10:
        riesgos += 5
        recomendaciones.append("🔥 DEMASIADOS puertos abiertos -> Esto es un colador")
    elif puertos_abiertos == 0:
        riesgos = -2
        recomendaciones.append("✅ No hay puertos abiertos -> O estás protegido o el firewall bloquea todo")
    
    # Veredicto final
    print(f"\n📊 Puertos analizados: {puertos_abiertos}")
    print(f"🎲 Nivel de riesgo: {riesgos}/10")
    
    if riesgos <= 0:
        print(Fore.GREEN + "🟢 VEREDICTO IA: Bastante seguro. Buen trabajo (por ahora)" + Style.RESET_ALL)
    elif riesgos <= 4:
        print(Fore.YELLOW + "🟡 VEREDICTO IA: Cuidado. Algo huele mal aquí" + Style.RESET_ALL)
    else:
        print(Fore.RED + "🔴 VEREDICTO IA: PELIGRO. Esto está regalado" + Style.RESET_ALL)
    
    if recomendaciones:
        print("\n📝 Recomendaciones de la IA:")
        for rec in recomendaciones:
            print(f"  {rec}")
    
    # Frase random bizarra
    frases_finales = [
        "🧙 La IA ha hablado. No me hagas caso, solo soy un script",
        "🎭 Recuerda: escanear sin permiso es como espiar a tu ex",
        "💀 Si encontraste algo malo... pues ya sabes, parchea o reza",
        "🌀 Tool-Net no se hace responsable de tus malas decisiones"
    ]
    print(f"\n{Fore.MAGENTA}{random.choice(frases_finales)}{Style.RESET_ALL}")
