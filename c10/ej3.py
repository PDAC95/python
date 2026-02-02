# productos = ["Laptop", "Mouse", "Teclado", "Monitor"]

precios = [15000, 500, 1200, 8000]


# print("Precios originales:", precios)

# # 20% descuento = pagar el 80%

# # Por eso multiplicamos por 0.80

# con_descuento = list(map(lambda precio: precio * 0.80, precios))


# print("Con descuento (20%):", con_descuento)

# # 16% IVA = multiplicar por 1.16

# precios_finales = list(map(lambda precio: precio * 1.16, con_descuento))


# print("Precios finales (con IVA):", precios_finales)

# # Usar map() con múltiples listas para mostrar todo junto

# resultados = list(map(

#     lambda prod, original, final: f"{prod}: ${original} → ${final:.2f}",

#     productos,

#     precios,

#     precios_finales

# ))


# print("\n=== RESULTADOS ===")

# for resultado in resultados:

#     print(resultado)

precios_finales = list(map(lambda p: p * 0.80 * 1.16,precios))
print ('version corta', precios_finales)