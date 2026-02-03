# lista = [x*2 for x in range (5)]
# print ("lista:", lista)
# print ('tipo:', type(lista))

generador = (x*2 for x in range (5))
for valor in generador:
    print(valor)
print ("generador:", generador)
print ('Tipo:', type(generador))

