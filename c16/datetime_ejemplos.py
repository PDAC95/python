# ============================================
# Ejemplos de datetime
# ============================================

from datetime import datetime, date, timedelta

# Fecha y hora actual
ahora = datetime.now()
print(f"Ahora: {ahora}")
print(f"Solo fecha: {date.today()}")

# Formatear
print(f"\nFormatos:")
print(f"  Latinoamericano: {ahora.strftime('%d/%m/%Y')}")
print(f"  ISO: {ahora.strftime('%Y-%m-%d')}")
print(f"  Completo: {ahora.strftime('%A, %d de %B de %Y')}")
print(f"  Hora: {ahora.strftime('%H:%M:%S')}")

# Parsear texto a fecha
texto = "25/12/2025"
navidad = datetime.strptime(texto, "%d/%m/%Y")
print(f"\nNavidad: {navidad}")

# Cálculos
dias_para_navidad = (navidad - ahora).days
print(f"Faltan {dias_para_navidad} días para Navidad")

# Sumar días
en_una_semana = ahora + timedelta(weeks=1)
print(f"En una semana: {en_una_semana.strftime('%d/%m/%Y')}")
