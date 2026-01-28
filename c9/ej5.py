def calcular_total(descuento=0, *productos):

    """

    Calcula el total de una compra con descuento opcional.


    Args:

        descuento: Porcentaje de descuento (default: 0)

        *productos: Precios de los productos


    Returns:

        dict con subtotal, descuento_aplicado y total

    """

    subtotal = sum(productos)

    descuento_aplicado = subtotal * (descuento / 100)

    total = subtotal - descuento_aplicado


    return {

        "subtotal": subtotal,

        "descuento_aplicado": descuento_aplicado,

        "total": total

    }



def generar_ticket(nombre_cliente, *productos, descuento=10):

    """

    Genera un ticket de compra formateado.


    Args:

        nombre_cliente: Nombre del cliente

        *productos: Precios de los productos

        descuento: Porcentaje de descuento (default: 10)


    Returns:

        String con el ticket formateado

    """

    # Calcular usando la otra función

    # Nota: calcular_total espera descuento primero, luego *productos

    resultado = calcular_total(descuento, *productos)


    # Formatear productos para mostrar

    productos_str = ", ".join([f"${p}" for p in productos])


    # Construir ticket

    ticket = f"""

========= TICKET =========

Cliente: {nombre_cliente}

Productos: {productos_str}

Subtotal: ${resultado['subtotal']:.2f}

Descuento ({descuento}%): -${resultado['descuento_aplicado']:.2f}

TOTAL: ${resultado['total']:.2f}

=========================="""


    return ticket



# ===== PRUEBAS =====

print("=== Prueba calcular_total ===")

resultado1 = calcular_total(10, 100, 50, 25)

print(f"Con 10% descuento: {resultado1}")


resultado2 = calcular_total(0, 100, 200)

print(f"Sin descuento: {resultado2}")


print("\n=== Prueba generar_ticket ===")

ticket1 = generar_ticket("María", 100, 50, 75)

print(ticket1)


ticket2 = generar_ticket("Carlos", 200, 150, 50, 25, descuento=15)

print(ticket2)


ticket3 = generar_ticket("Ana", 99.99, descuento=5)

print(ticket3)