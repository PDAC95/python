productos = [

    {"nombre": "laptop", "precio": 800},

    {"nombre": "mouse", "precio": 25},

    {"nombre": "teclado", "precio": 50},

    {"nombre": "monitor", "precio": 300}

]

nombres = [producto["nombre"] for producto in productos]

print("Nombres:", nombres)

precios_dict = {producto["nombre"]: producto["precio"] for producto in productos}

print("Precios:", precios_dict)

precios_aumentados = [producto["precio"] * 1.15 for producto in productos]

print("Precios aumentados:", precios_aumentados)

caros = {producto["nombre"]: producto["precio"] for producto in productos if producto["precio"] > 100}

print("Productos caros:", caros)

