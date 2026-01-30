# datos_prueba.py
# Datos de ejemplo para testing del sistema de tareas

# "Lista de tareas de ejemplo"
# "Usamos esto para no tener que crear tareas manualmente cada vez"
tareas_ejemplo = [
    {
        "id": 1,
        "titulo": "Completar informe mensual",
        "descripcion": "Reporte de ventas y métricas del equipo",
        "prioridad": "alta",
        "categoria": "trabajo",
        "completada": False,
        "fecha_creacion": "2025-01-28"
    },
    {
        "id": 2,
        "titulo": "Comprar despensa",
        "descripcion": "Leche, pan, huevos, frutas",
        "prioridad": "media",
        "categoria": "hogar",
        "completada": False,
        "fecha_creacion": "2025-01-29"
    },
    {
        "id": 3,
        "titulo": "Estudiar para examen Python",
        "descripcion": "Repasar funciones, clases y módulos",
        "prioridad": "alta",
        "categoria": "estudio",
        "completada": True,
        "fecha_creacion": "2025-01-25"
    },
    {
        "id": 4,
        "titulo": "Hacer ejercicio",
        "descripcion": "Gimnasio o correr 30 minutos",
        "prioridad": "media",
        "categoria": "personal",
        "completada": False,
        "fecha_creacion": "2025-01-30"
    },
    {
        "id": 5,
        "titulo": "Llamar al cliente",
        "descripcion": "Seguimiento del proyecto",
        "prioridad": "alta",
        "categoria": "trabajo",
        "completada": False,
        "fecha_creacion": "2025-01-30"
    },
    {
        "id": 6,
        "titulo": "Lavar el coche",
        "descripcion": "",
        "prioridad": "baja",
        "categoria": "hogar",
        "completada": True,
        "fecha_creacion": "2025-01-27"
    },
    {
        "id": 7,
        "titulo": "Preparar presentación",
        "descripcion": "Slides para reunión del viernes",
        "prioridad": "media",
        "categoria": "trabajo",
        "completada": False,
        "fecha_creacion": "2025-01-29"
    }
]

# "Tenemos 7 tareas de ejemplo con variedad:"
# "- Diferentes prioridades (alta, media, baja)"
# "- Diferentes categorías (trabajo, hogar, estudio, personal)"
# "- Algunas completadas, otras pendientes"
# "- Con y sin descripción"