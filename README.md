# 🧬 Pokémon API - Flask + Flask-Admin

Este proyecto es una API REST y panel de administración para gestionar usuarios, pokémon, tipos y favoritos. Construida con **Flask**, utiliza **Flask-Admin** para una interfaz web de administración, **SQLAlchemy** para el ORM y **WTForms** para formularios.

---

## 🧾 Descripción General

- Administra usuarios con autenticación (hash de contraseña).
- Administra pokémon, asociados a un tipo (por ejemplo: Fuego, Agua...).
- Consulta y gestión de tipos de pokémon.
- Asociación de usuarios con múltiples pokémon favoritos.
- CRUD completo por endpoints REST y panel Flask-Admin.

---

## 🗃️ Estructura de Carpetas

```
pokemon-api-flask/
│
├── src/
│   ├── app.py              # Punto de entrada principal de la app Flask
│   ├── config.py           # Configuraciones generales (base de datos, claves)
│   ├── database.py         # Inicialización de la base de datos con SQLAlchemy
│   ├── models.py           # Definición de modelos y clases de Flask-Admin
│   ├── routes.py           # Endpoints REST
│   ├── seeder.py           # Carga inicial de datos (admin y tipos)
│   └── pokemon_seeder.py   # Inserta Pokémon por defecto
├── Pipfile                 # Declaración de dependencias
├── Pipfile.lock
├── reset-env.bat          # Script para eliminar entorno virtual y reinstalar
├── README.md              # Este archivo 📘
```

---

## ⚙️ Dependencias Principales

- **Flask**: Framework web principal.
- **Flask-Admin**: Interfaz web de administración.
- **Flask-SQLAlchemy**: ORM para la base de datos.
- **Flask-Migrate**: Manejo de migraciones con Alembic.
- **Flask-Bcrypt**: Hash seguro para contraseñas.
- **Flask-WTF / WTForms**: Validación de formularios.
- **Flask-CORS**: Soporte para CORS.
- **python-dotenv**: Carga de variables desde `.env`.

> 📌 Se fijó la versión de `wtforms` a `3.1.2` debido a incompatibilidades con `flask-admin`.

---

## 📜 Scripts especiales (definidos en `Pipfile`)

```toml
[scripts]
seed = "python src/seeder.py"
seed-pokemon = "python src/pokemon_seeder.py"
reset-env = "reset-env.bat"
```

### 🧪 Ejecutarlos con:

```bash
pipenv run seed         # Inserta admin + tipos base
pipenv run seed-pokemon # Inserta pokémon de prueba
pipenv run reset-env    # Elimina entorno actual y crea uno nuevo
```

---

## 🔁 Script especial: `reset-env.bat`

Este archivo automatiza el proceso de reinicio completo del entorno virtual:

```bat
@echo off
echo 🧹 Eliminando entorno virtual actual...
pipenv --rm

echo 📦 Instalando dependencias desde Pipfile...
pipenv install

echo ✅ Entorno limpio y listo!
```

---

## 🧪 Seeder principal: `src/seeder.py`

Este script:

- Crea un usuario admin con contraseña (`admin:admin123`).
- Inserta los **18 tipos** de Pokémon oficiales:
  - Agua, Fuego, Planta, Veneno, Fantasma, etc.

---

## 🧪 Seeder Pokémon: `src/pokemon_seeder.py`

Inserta un conjunto de pokémon ficticios relacionados a tipos predefinidos. Útil para pruebas iniciales.

---

## 📮 Endpoints REST

| Método | Ruta                            | Descripción                      |
|--------|----------------------------------|----------------------------------|
| GET    | `/users`                        | Lista todos los usuarios         |
| POST   | `/users`                        | Crea un nuevo usuario            |
| DELETE | `/users/<id>`                  | Elimina un usuario               |
| GET    | `/pokemons`                     | Lista todos los pokémon          |
| POST   | `/pokemons`                     | Crea un nuevo pokémon            |
| DELETE | `/pokemons/<id>`               | Elimina un pokémon               |
| GET    | `/types`                        | Lista tipos disponibles          |
| GET    | `/users/<id>/favorites`        | Lista favoritos de un usuario    |
| POST   | `/users/<id>/favorites`        | Agrega un pokémon a favoritos    |
| DELETE | `/users/<id>/favorites/<fid>`  | Elimina un favorito              |

---

## 🧑‍💻 Panel Flask-Admin

Disponible en: [http://localhost:3000/admin](http://localhost:3000/admin)

- `User`: Administra usuarios (crear, editar, eliminar).
- `Pokemon`: Crear pokémon y asignarles tipo desde un combo box.
- `Type`: Solo lectura. Tipos cargados desde el seeder.
- `Favorite`: Asociación entre usuario y pokémon.

---

## 🧪 Cómo correr el proyecto desde cero

```bash
git clone <repo>
cd pokemon-api-flask

# Opcional: limpiar entorno si ya existía
pipenv run reset-env

# Activar entorno y cargar dependencias
pipenv shell
pipenv install

# Migrar DB y cargar datos
flask db upgrade
pipenv run seed
pipenv run seed-pokemon

# Ejecutar app
pipenv run start
```

---

## 👨‍💻 **Autor**

- **Desarrollado por JulioRom**
- 📧 **Correo:** [julioandrescampos@gmail.com](mailto:julioandrescampos@gmail.com)
- 🔗 **GitHub:** [https://github.com/JulioRom](https://github.com/JulioRom)