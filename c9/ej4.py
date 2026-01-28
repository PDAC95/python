def calcular(operacion, *valores):

    """Combina parámetro normal con *args"""

    print(f"Operación: {operacion}")

    print(f"Valores: {valores}")


    if operacion == "suma":

        return sum(valores)

    elif operacion == "promedio":

        return sum(valores) / len(valores) if valores else 0

    elif operacion == "maximo":

        return max(valores) if valores else None

    elif operacion == "minimo":

        return min(valores) if valores else None

    else:

        return None


print(calcular("suma", 1, 2, 3, 4, 5))      # 15

print(calcular("promedio", 10, 20, 30))     # 20.0

print(calcular("maximo", 5, 2, 8, 1, 9))    # 9