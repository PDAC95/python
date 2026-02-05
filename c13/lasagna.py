# ============================================================
# TAREA 1: Definir tiempo de horneado esperado como constante
# ============================================================
"""
prueba
"""
# TODO: Define la constante EXPECTED_BAKE_TIME que representa
# cuántos minutos debe hornear la lasagna en el horno.
# Según tu libro de cocina, la lasagna debe estar 40 minutos en el horno.
#
# Recuerda: Las constantes se escriben en MAYÚSCULAS (SCREAMING_SNAKE_CASE)
# Ejemplo: MI_CONSTANTE = 100

EXPECTED_BAKE_TIME = 40

# ============================================================
# TAREA 2: Calcular tiempo de horneado restante en minutos
# ============================================================

# TODO: Define la función bake_time_remaining() que:
# - Recibe un parámetro: elapsed_bake_time (minutos que ya lleva en el horno)
# - Retorna cuántos minutos le faltan a la lasagna basándose en EXPECTED_BAKE_TIME
#
# Ejemplo de uso:
# >>> bake_time_remaining(30)
# 10
#
# Pista: resta elapsed_bake_time de EXPECTED_BAKE_TIME

def bake_time_remaining(elapsed_bake_time):
    """
    calcula cuantos minutos le faltan a la lasagna 
    :param elapsed_bake_time: int - minutos que ya ha estado en el horno
    :return: int - cuantos minutos faltan
    """
    tiempo_restante = EXPECTED_BAKE_TIME - elapsed_bake_time
    return tiempo_restante
    pass


# ============================================================
# TAREA 3: Calcular tiempo de preparación en minutos
# ============================================================

# TODO: Define la función preparation_time_in_minutes() que:
# - Recibe un parámetro: number_of_layers (número de capas que quieres agregar)
# - Retorna cuántos minutos tardarías en hacerlas
# - Asume que cada capa toma 2 minutos en prepararse
#
# Ejemplo de uso:
# >>> preparation_time_in_minutes(2)
# 4
#
# Pista: multiplica number_of_layers por 2
def preparation_time_in_minutes(number_of_layers):
    """
    Docstring for preparation_time_in_minutes
    
    :param number_of_layers: Description
    """
    MINUTOS_POR_CAPA = 2
    tiempo_preparacion = number_of_layers * MINUTOS_POR_CAPA
    return tiempo_preparacion


# ============================================================
# TAREA 4: Calcular tiempo total transcurrido (preparación + horneado)
# ============================================================

# TODO: Define la función elapsed_time_in_minutes() que:
# - Recibe dos parámetros:
#   * number_of_layers (número de capas agregadas a la lasagna)
#   * elapsed_bake_time (minutos que la lasagna ha estado en el horno)
# - Retorna el total de minutos que has estado en la cocina cocinando
#   (tiempo de preparación + tiempo de horneado)
#
# Ejemplo de uso:
# >>> elapsed_time_in_minutes(3, 20)
# 26
#
# Pista: suma el tiempo de preparación (usa la función anterior)
#        con el tiempo de horneado transcurrido

def elapsed_time_in_minutes(number_of_layers, elapsed_bake_time):
    """
    Docstring for elapsed_time_in_minutes
    
    :param number_of_layers: Description
    :param elapsed_bake_time: Description
    """
    tiempo_preparacion = preparation_time_in_minutes(number_of_layers)

    tiempo_total = tiempo_preparacion + elapsed_bake_time

    return tiempo_total


# ============================================================
# TAREA 5: Actualizar la receta con notas
# ============================================================

# TODO: Regresa a través de la receta y agrega "notas" en forma de docstrings
# a TODAS las funciones que creaste.
#
# Formato del docstring:
# """
# Descripción breve de la función.
#
# :param nombre_parametro: tipo - descripción del parámetro
# :return: tipo - descripción de lo que retorna
#
# Explicación más detallada de lo que hace la función.
# """
#
# Ejemplo:
# def mi_funcion(numero):
#     """
#     Duplica un número.
#
#     :param numero: int - el número a duplicar
#     :return: int - el número duplicado
#
#     Esta función toma un número entero y lo multiplica por 2.
#     """
#     return numero * 2


# ============================================================
# PRUEBAS (No modificar - solo ejecutar)
# ============================================================

if __name__ == "__main__":
    print("=" * 60)
    print("PRUEBAS DEL EJERCICIO LASAGNA")
    print("=" * 60)
    print()
    
    # Prueba 1
    print("PRUEBA 1: Constante EXPECTED_BAKE_TIME")
    print(f"Tiempo esperado de horneado: {EXPECTED_BAKE_TIME} minutos")
    assert EXPECTED_BAKE_TIME == 40, "EXPECTED_BAKE_TIME debe ser 40"
    print("✓ Correcto")
    print()
    
    # Prueba 2
    print("PRUEBA 2: bake_time_remaining()")
    result = bake_time_remaining(30)
    print(f"Tiempo restante (30 min transcurridos): {result} minutos")
    assert result == 10, "Con 30 minutos transcurridos, deben faltar 10"
    print("✓ Correcto")
    print()
    
    # Prueba 3
    print("PRUEBA 3: preparation_time_in_minutes()")
    result = preparation_time_in_minutes(2)
    print(f"Tiempo de preparación (2 capas): {result} minutos")
    assert result == 4, "2 capas deben tomar 4 minutos"
    print("✓ Correcto")
    print()
    
    # Prueba 4
    print("PRUEBA 4: elapsed_time_in_minutes()")
    result = elapsed_time_in_minutes(3, 20)
    print(f"Tiempo total (3 capas, 20 min horneado): {result} minutos")
    assert result == 26, "3 capas (6 min) + 20 min horneado = 26 min"
    print("✓ Correcto")
    print()
    
    # Prueba 5
    print("PRUEBA 5: Docstrings")
    functions = [
        bake_time_remaining,
        preparation_time_in_minutes,
        elapsed_time_in_minutes
    ]
    for func in functions:
        assert func.__doc__ is not None, f"{func.__name__} necesita docstring"
        print(f"✓ {func.__name__} tiene docstring")
    print()
    
    print("=" * 60)
    print("✓ TODAS LAS PRUEBAS PASARON")
    print("=" * 60)