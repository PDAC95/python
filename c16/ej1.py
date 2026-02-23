from datetime import datetime, timedelta    

# ahora = datetime.now()
# manana = ahora + timedelta(days=1)
# en_una_semana = ahora + timedelta(days=7)
# ayer = ahora - timedelta(days=1)
# print("Ahora:", ahora)
# print("Mañana:", manana)
# print("En una semana:", en_una_semana)  
# print("Ayer:", ayer)


hoy = datetime.now()
fin_de_ano = datetime(hoy.year, 12, 31)
dias_restantes = (fin_de_ano - hoy).days
print("Días restantes para fin de año:", dias_restantes)
