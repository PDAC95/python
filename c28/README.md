# Dashboard E-commerce

Proyecto del curso de Python - Bloque Django (Clases 28-34)

## Setup

1. Crear entorno virtual:
```
python -m venv venv
```

2. Activar entorno:
```
venv\Scripts\activate
```

3. Instalar dependencias:
```
pip install -r requirements.txt
```

4. Aplicar migraciones:
```
cd dashboard
python manage.py migrate
```

5. Crear superusuario:
```
python manage.py createsuperuser
```

6. Correr servidor:
```
python manage.py runserver
```

7. Visitar: http://127.0.0.1:8000

## Estructura

- `dashboard/` - Configuracion del proyecto
- `core/` - App principal (landing page)

## URLs

- `/` - Pagina principal
- `/about/` - Sobre nosotros
- `/contact/` - Contacto
- `/admin/` - Panel de administracion
