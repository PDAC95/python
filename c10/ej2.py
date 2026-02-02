mayor = lambda a, b: a if a > b else b
print(mayor(10,5))

es_adulto = lambda edad: "adulto" if edad >= 18 else 'menor'
print (es_adulto(18))

def impuestos (precio):
    iva = precio *.16
    total = precio + iva
    return total 