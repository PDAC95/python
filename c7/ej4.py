# Solucion:
persona = {
    "nombre": "Carlos",
    "edad": 28,
    "ciudad": "Lima"
}
persona["profesion"] = "Disenador"
persona["edad"] = 29

for k, v in persona.items():
    print(f"{k}: {v}")