# === CONFIGURACIÓN INICIAL ===
secreto = 27       # El número que hay que adivinar
max_int = 7        # Máximo de intentos permitidos
usados = 0         # Contador: empieza en 0

# Mensaje de bienvenida
print("Adivina el numero (1-50). Tienes 7 intentos")

# === LOOP PRINCIPAL ===
while usados < max_int:  # Mientras no llegue a 7 intentos
    
    entrada = input("Tu numero: ")  # Pide un número al usuario
    
    # VALIDACIÓN: ¿Es un número?
    if not entrada.isdigit():       # Si NO es número...
        print("Solo numeros!")      # Avisa el error
        continue                    # Salta (no cuenta este intento)
    
    # PROCESAR INTENTO VÁLIDO
    num = int(entrada)  # Convierte texto a número
    usados += 1         # Suma 1 al contador de intentos
    
    # COMPARAR CON EL SECRETO
    if num == secreto:  # ¿Adivinó?
        print(f"Ganaste en {usados} intentos!")
        break           # Termina el juego (ganó)
    
    elif num < secreto:  # ¿Muy bajo?
        print(f"Muy bajo! Quedan {max_int - usados}")
    
    else:  # ¿Muy alto?
        print(f"Muy alto! Quedan {max_int - usados}")

# === SI NUNCA HUBO BREAK ===
else:
    print(f"Perdiste! Era {secreto}")  # Usó los 7 intentos sin adivinar