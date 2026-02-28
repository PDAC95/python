# Crear una clase Producto para una tienda

class Producto:
    """Representa un producto en una tienda."""

    # El constructor (__init__) se ejecuta al crear un objeto
    # 'self' es la referencia al objeto que se está creando
    def __init__(self, nombre: str, precio: float, stock: int):
        self.nombre = nombre    # Atributo de instancia: nombre del producto
        self.precio = precio    # Atributo de instancia: precio unitario
        self.stock = stock      # Atributo de instancia: cantidad disponible

    # Método que reduce el stock al vender unidades
    def vender(self, cantidad: int):
        # BONUS: Verificar que hay stock suficiente antes de vender
        if cantidad > self.stock:
            print(f"No hay suficiente stock. Stock disponible: {self.stock}")
            return  # Salimos del método sin hacer nada más

        self.stock -= cantidad  # Reducimos el stock

    # Método que aumenta el stock al recibir mercancía
    def reabastecer(self, cantidad: int):
        self.stock += cantidad  # Aumentamos el stock

    # Método que calcula el valor total del inventario
    def calcular_valor_total(self) -> float:
        return self.precio * self.stock  # precio unitario * unidades disponibles


# --- Ejemplo de uso esperado ---
laptop = Producto("Laptop", 999.99, 10)

laptop.vender(3)                    # Vendemos 3 → stock: 7
print(f"Stock después de vender: {laptop.stock}")

print(f"Valor total: {laptop.calcular_valor_total()}")  # → 6999.93

# Probando el BONUS: intentar vender más de lo disponible
laptop.vender(100)                  # → "No hay suficiente stock..."

# Probando reabastecer
laptop.reabastecer(5)               # stock: 7 + 5 = 12
print(f"Stock después de reabastecer: {laptop.stock}")