materias = ("Matematicas", "Fisica", "Quimica")
estudiantes = []

estudiantes.append("Ana")
estudiantes.append("Luis")

for est in estudiantes:
    print(f"{est} cursa:")
    for mat in materias:
        print(f"  - {mat}")