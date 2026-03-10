# PRE-CLASE 23: Instalacion de DB Browser for SQLite

## Que vamos a instalar?

**DB Browser for SQLite** es un programa visual para trabajar con bases de datos.

Piensen en el como el "VS Code de las bases de datos":
- Pueden ver las tablas
- Escribir comandos SQL
- Ver los resultados al instante

Es **gratis** y lo usaremos en las proximas clases.

---

## Tiempo estimado: 5-10 minutos

---

## PASO 1: Descargar el instalador

1. Abran su navegador y vayan a:

   **https://sqlitebrowser.org/dl/**

2. En la seccion **Windows**, hagan clic en:

   **DB Browser for SQLite - Standard installer for 64-bit Windows**

   (Es el primer enlace de la seccion Windows)

3. Se descargara un archivo llamado algo como:

   `DB.Browser.for.SQLite-3.12.2-win64.msi`

---

## PASO 2: Instalar el programa

1. **Busquen el archivo descargado** en la carpeta Descargas

2. **Doble clic en el archivo** para ejecutarlo

3. Si Windows pregunta "Desea permitir que esta aplicacion haga cambios?":
   - Clic en **Si**

4. **Sigan el asistente:**

   | Pantalla | Que hacer |
   |----------|-----------|
   | Welcome | Clic en **Next** |
   | License Agreement | Marcar "I accept..." y **Next** |
   | Choose Install Location | Dejar por defecto, **Next** |
   | Choose Components | Dejar todo marcado, **Next** |
   | Choose Start Menu Folder | **Next** |
   | Ready to Install | **Install** |
   | Completing | **Finish** |

---

## PASO 3: Verificar que funciona

1. Presionen la tecla **Windows** (la tecla con el logo)
2. Escriban: `DB Browser`
3. Clic en **DB Browser for SQLite**
4. Deben ver una ventana con menu y pestanas

Si ven la ventana, todo esta bien!

---

## PASO 4: Prueba rapida (opcional)

1. Clic en **New Database**
2. Nombre: `prueba.db`, guardar en Escritorio
3. Si aparece "Edit table definition", clic en **Cancel**
4. Ir a pestana **Execute SQL**
5. Escribir: `SELECT 'Hola, estoy listo!' AS mensaje;`
6. Clic en el boton Play (o F5)
7. Debe aparecer "Hola, estoy listo!" abajo

Listo! Pueden borrar prueba.db

---

## Problemas comunes

**"No puedo descargar"**
- Intenten otro navegador

**"Windows no me deja instalar"**
- Clic en "Si" cuando pregunte permisos

**"No encuentro el programa"**
- Buscar "DB Browser" en menu inicio

---

## Checklist antes de clase

- [ ] Descargue el instalador
- [ ] Instale el programa
- [ ] Puedo abrir DB Browser for SQLite
- [ ] (Opcional) Hice la prueba rapida

**Problemas?** Contacten al instructor antes de la clase.

**Nos vemos en la Clase 23!**
