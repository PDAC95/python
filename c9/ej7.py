def funcion_completa(a, b, *args, x=10, y=20, **kwargs):

    print(f"a = {a}")

    print(f"b = {b}")

    print(f"*args = {args}")

    print(f"x = {x}")

    print(f"y = {y}")

    print(f"**kwargs = {kwargs}")

    print("-" * 30)


# Prueba 1: Solo obligatorios

funcion_completa(1, 2)


# Prueba 2: Con *args

funcion_completa(1, 2, 3, 4, 5)


# Prueba 3: Con defaults

funcion_completa(1, 2, x=100)


# Prueba 4: Con **kwargs

funcion_completa(1, 2, extra="dato", otro=True)


# Prueba 5: COMPLETA

funcion_completa(1, 2, 3, 4, 5, x=100, y=200, extra="hola", debug=True)