# Las 4 estructuras juntas:
categorias = ("Electronica", "Ropa")  # Tupla
productos = []                         # Lista
inventario = {}                        # Dict
marcas = set()                         # Set

def agregar(nombre, precio, marca):
    productos.append(nombre)
    inventario[nombre] = {"precio": precio}
    marcas.add(marca)

agregar("Laptop", 999, "Dell")
agregar("Mouse", 29, "Dell")
print(f"Marcas: {marcas}")  # {"Dell"}