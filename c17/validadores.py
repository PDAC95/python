"""
Funciones de validación - Para practicar testing
"""


def es_par(n):
    """Retorna True si n es par."""
    return n % 2 == 0


def es_positivo(n):
    """Retorna True si n es mayor que cero."""
    return n > 0


def es_adulto(edad):
    """Retorna True si la edad es 18 o mayor."""
    return edad >= 18


def es_email_valido(email):
    """
    Validación básica de email.
    Debe contener @ y al menos un punto después del @.
    """
    if "@" not in email:
        return False
    partes = email.split("@")
    if len(partes) != 2:
        return False
    return "." in partes[1]
