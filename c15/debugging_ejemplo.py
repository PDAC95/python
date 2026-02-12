# ============================================
# Ejemplo: Tecnicas de debugging
# ============================================

# --- PRINT DEBUGGING ---
def buscar_palabra_debug(texto, palabra):
    """Version con prints de debug."""
    palabras = texto.split()
    print(f"DEBUG: palabras = {palabras}")
    print(f"DEBUG: buscando = '{palabra}'")

    for i in range(len(palabras)):
        print(f"DEBUG: [{i}] comparando '{palabras[i]}' con '{palabra}'")
        if palabras[i] == palabra:
            return i
    return -1


# --- ASSERT ---
def calcular_promedio_con_assert(notas):
    """Version con validaciones assert."""
    assert len(notas) > 0, "La lista de notas no puede estar vacia"
    assert all(isinstance(n, (int, float)) for n in notas), "Todas las notas deben ser numeros"
    assert all(0 <= n <= 100 for n in notas), "Las notas deben estar entre 0 y 100"

    return sum(notas) / len(notas)


# PRUEBAS
if __name__ == "__main__":
    print("=== PRINT DEBUGGING ===")
    resultado = buscar_palabra_debug("Hola mundo Python", "Python")
    print(f"Resultado: {resultado}\n")

    print("=== ASSERT ===")
    print(f"Promedio: {calcular_promedio_con_assert([90, 85, 88]):.2f}")

    # Descomentar para ver los assert fallar:
    # print(calcular_promedio_con_assert([]))  # AssertionError
    # print(calcular_promedio_con_assert([90, 150]))  # AssertionError
