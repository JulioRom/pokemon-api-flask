# config.py - Configuración de la aplicación
import os

class Config:
    BASE_DIR = os.path.abspath(os.path.dirname(__file__))  # Directorio base del proyecto
    INSTANCE_DIR = os.path.join(os.path.dirname(BASE_DIR), "instance")  # Mover a instance/

    if not os.path.exists(INSTANCE_DIR):
        os.makedirs(INSTANCE_DIR)  # Crear la carpeta instance si no existe

    SQLALCHEMY_DATABASE_URI = f"sqlite:///{os.path.join(INSTANCE_DIR, 'pokemon.db')}"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    
    # Agregar clave secreta para CSRF en Flask-WTF
    SECRET_KEY = os.environ.get("SECRET_KEY") or "supersecretkey"
    WTF_CSRF_ENABLED = True  # Habilitar protección CSRF en los formularios
