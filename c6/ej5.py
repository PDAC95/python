# tabla_multiplicar.py
numero = int(input("Numero: "))

print(f"Tabla del {numero}:")
for i in range(1, 11):  # 1 a 10
    resultado = numero * i
    print(f"{numero} x {i} = {resultado}")
