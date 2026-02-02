# imperativa

# numeros = [1,2,3,4,5]
# duplicados = []

# for numero in numeros:
#     duplicados.append(numero*2)

#     print('imperativo', duplicados)

numeros = [1,2,3,4,5]
duplicados = list(map(lambda x: x*2, numeros))

print("funcional:", duplicados)