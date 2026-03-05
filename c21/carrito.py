class CarritoCompras:
    def __init__(self):
        self.productos = []

    def agregar(self, producto):
        self.productos.append(producto)
        print(f"Agregado: {producto}")

    def __len__(self):
        return len(self.productos)
    
    def __str__(self):
        return f"Carrito con {len(self)} productos"
    
carrito = CarritoCompras()
print(len(carrito))  # Salida: 0
    
carrito.agregar("Manzanas")
carrito.agregar("Pan")
carrito.agregar("Leche")

print(len(carrito))  # Salida: 3
print(carrito)

