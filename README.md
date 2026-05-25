# Sistema de Gestion de Equipo - Participacion 19-05-26

Este es un proyecto de ejemplo que implementa una aplicacion web modular en Flask para la gestion de miembros de un equipo de trabajo y el control de sus tareas asignadas. La aplicacion esta estructurada utilizando el patron de diseño MVC mediante Flask Blueprints, lo que permite separar logicamente las rutas, modelos y plantillas de cada modulo.

## Tecnologias utilizadas

- Python 3
- Flask
- Flask-SQLAlchemy (Base de datos SQLite3)
- Flask-Migrate (Gestion de migraciones con Alembic)
- Bootstrap 5 (Estilizacion responsiva)

## Estructura del proyecto

- blueprintapp: Directorio principal de la aplicacion.
  - core: Modulo del panel de control principal.
  - miembros: Modulo para la administracion de miembros del equipo (CRUD).
  - tareas: Modulo para la asignacion y control de tareas (CRUD).
  - templates: Plantilla base compartida.
- run.py: Archivo de entrada para ejecutar la aplicacion.
- requirements.txt: Lista de dependencias del proyecto.

## Instalacion y ejecucion

### 1. Clonar o acceder al directorio del proyecto
Asegurese de abrir su terminal en el directorio raiz del proyecto.

### 2. Crear y activar el entorno virtual
Ejecute los siguientes comandos en su terminal:

```bash
python3 -m venv venv
source venv/bin/activate (en Linux)
venv\Scripts\activate (en Windows)
```

### 3. Instalar las dependencias
Instale los paquetes requeridos especificados en el archivo de requerimientos:

```bash
pip install -r requirements.txt
```

### 4. Inicializar y configurar la base de datos
Establezca la aplicacion Flask y ejecute los comandos de Flask-Migrate para crear las tablas en la base de datos SQLite:

```bash
export FLASK_APP=run.py
flask db init
flask db migrate -m "Creacion de tablas miembros y tareas"
flask db upgrade
```

La base de datos se creara de forma automatica en la ruta `instance/bd_equipo.db`.

### 5. Iniciar la aplicacion
Para arrancar el servidor de desarrollo, ejecute:

```bash
python run.py
```

Abra su navegador de internet y acceda a `http://127.0.0.1:5000`.

## Funcionalidades completadas

- Panel de inicio interactivo con acceso a los modulos.
- Modulo de Miembros: Operaciones completas de creacion, lectura, actualizacion y eliminacion de registros.
- Modulo de Tareas: Registro de actividades con control de estado completado o pendiente y edicion integral.
- Diseño responsivo moderno y optimizado utilizando estilos de Bootstrap 5.
