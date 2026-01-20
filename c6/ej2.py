# break y continue

numero = 0
while numero <20:
    numero +=1 

    # Primero verificar break
    if numero == 15:
        print("Llegue a 15, detengo")
        break
    
    # Luego verificar continue
    if numero % 3 == 0:
        continue  # Salta multiplos de 3
    
    print(numero)
