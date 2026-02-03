# numeros = [1,2,3,4]
# dobles = [num *2 for num in numeros]

# nombres = ['claudio', 'nestor', 'kevin']
# mayusculas = [nombre.upper() for nombre in nombres]

# palabras = ['sol', 'python', 'gato', 'javascript', 'go']
# largas =[palabra for palabra in palabras if len(palabra)>4]
# print(largas)

# nombres = ['claudio', 'nestor', 'kevin']
# longitud = {nombre:len(nombre) for nombre in nombres}
# print (longitud)

# precios = {'manzana':100, 'pera':80, 'uva':150}
# caras = {fruta:precio for fruta, precio in precios.items() if precio > 100}
# print(caras)

manual =[]
for numb in numeros:
    if num not in manual:
        manual.append(num)