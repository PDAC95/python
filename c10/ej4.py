from functools import reduce

numeros = [1, 2, 3, 4, 5]

producto = reduce(lambda acc, x: acc * x, numeros)

print("\nProducto:", producto)  # 120