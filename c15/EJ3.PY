def buscar_palabra(texto, palabra):

    palabras = texto.split()

    print(f"DEBUG: palabras = {palabras}")

    print(f"DEBUG: buscando = '{palabra}'")


    for i in range(len(palabras)):

        print(f"DEBUG: [{i}] comparando '{palabras[i]}' con '{palabra}'")

        if palabras[i] == palabra:

            return i

    return -1