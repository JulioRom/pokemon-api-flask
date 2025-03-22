from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_cors import CORS
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView
from flask_wtf.csrf import CSRFProtect
import os

from src.config import Config  # Importar desde el módulo correcto
from src.database import db  # Asegurar que se importa correctamente

# Inicializar la aplicación Flask
app = Flask(__name__)
app.config.from_object(Config)

# Habilitar protección CSRF
csrf = CSRFProtect(app)

# Inicialización de extensiones
CORS(app)
db.init_app(app)
migrate = Migrate(app, db)
admin = Admin(app, name='Pokemon API', template_mode='bootstrap3')

# Importar modelos
from src.models import User, Pokemon, Type, Favorite, UserAdmin, PokemonAdmin, FavoriteAdmin

class ReadOnlyModelView(ModelView):
    can_create = False
    can_edit = False
    can_delete = False

# Agregar modelos a Flask-Admin
admin.add_view(UserAdmin(User, db.session))
admin.add_view(PokemonAdmin(Pokemon, db.session))
admin.add_view(ReadOnlyModelView(Type, db.session))  # Tipos ahora son solo visuales
admin.add_view(FavoriteAdmin(Favorite, db.session))

# Importar rutas después de inicializar la app y la base de datos
from src.routes import *

if __name__ == '__main__':
    app.run(debug=True, port=3000)
