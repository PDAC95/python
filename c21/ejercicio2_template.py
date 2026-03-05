# ═══════════════════════════════════════════════════════════════
# Clase 21 - Ejercicio 2: Clase Inventario (TEMPLATE)
# ═══════════════════════════════════════════════════════════════
# Crear una clase Inventario para una tienda con:
#
# Atributos:
#   - nombre (string) - nombre de la tienda
#   - productos (lista) - lista de diccionarios:
#     {'nombre': str, 'cantidad': int, 'precio': float}
#
# Métodos normales:
#   - agregar(nombre, cantidad, precio)
#   - vender(nombre, cantidad)
#
# Métodos dunder:
#   - __str__      → "Inventario 'MiTienda' (5 productos)"
#   - __repr__     → "Inventario('MiTienda')"
#   - __len__      → Número de tipos de productos
#   - __getitem__  → Acceder a producto por índice
#   - __contains__ → Verificar si un producto existe (por nombre)
# ═══════════════════════════════════════════════════════════════


class Inventario:
    def __init__(self, nombre):
        # TODO: guardar nombre e inicializar lista vacía
        pass

    def agregar(self, nombre, cantidad, precio):
        # TODO: Si ya existe (ignorar mayúsculas), sumar cantidad
        # Si no existe, agregar como diccionario nuevo
        pass

    def vender(self, nombre, cantidad):
        # TODO: Si hay stock suficiente, restar cantidad
        # Si no hay stock, mostrar mensaje de error
        # Si no existe, mostrar "no encontrado"
        pass

    def __str__(self):
        # TODO: retornar "Inventario 'nombre' (N productos)"
        pass

    def __repr__(self):
        # TODO: retornar "Inventario('nombre')"
        pass

    def __len__(self):
        # TODO: retornar número de productos diferentes
        pass

    def __getitem__(self, indice):
        # TODO: retornar producto por índice
        pass

    def __contains__(self, nombre):
        # TODO: buscar producto por nombre (ignorar mayúsculas)
        pass


# ═══════════════════════════════════════════════════════════════
# Pruebas - NO MODIFICAR
# ═══════════════════════════════════════════════════════════════

if __name__ == "__main__":
    tienda = Inventario("TechStore")
    tienda.agregar("Laptop", 10, 999.99)
    tienda.agregar("Mouse", 50, 29.99)
    tienda.agregar("Teclado", 30, 79.99)

    # Test __str__
    print(f"\n{tienda}")
    # Esperado: Inventario 'TechStore' (3 productos)

    # Test __len__
    print(f"Total tipos: {len(tienda)}")
    # Esperado: 3

    # Test __getitem__ y for
    print("\nProductos:")
    for producto in tienda:
        print(f"  {producto['nombre']}: {producto['cantidad']} unidades")
    # Esperado: lista de los 3 productos

    # Test __contains__
    print(f"\n¿Hay Laptop? {'laptop' in tienda}")    # Esperado: True
    print(f"¿Hay Monitor? {'monitor' in tienda}")    # Esperado: False

    # Test vender
    print()
    tienda.vender("Laptop", 2)
    # Esperado: Vendido: 2x Laptop = $1999.98

    tienda.vender("Laptop", 20)
    # Esperado: Stock insuficiente de Laptop

    # Test agregar existente
    print()
    tienda.agregar("Laptop", 5, 999.99)
    # Esperado: Actualizado: Laptop (+5)
