from src.database import db
from flask_login import UserMixin
from flask_bcrypt import Bcrypt
from flask_admin.contrib.sqla import ModelView
from flask_admin.form import Select2Widget
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, validators
from wtforms_sqlalchemy.fields import QuerySelectField


bcrypt = Bcrypt()

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password_hash = db.Column(db.String(128), nullable=False)  # Campo protegido
    favorites = db.relationship('Favorite', back_populates='user', lazy=True)

    def set_password(self, password):
        self.password_hash = bcrypt.generate_password_hash(password).decode('utf-8')

    def check_password(self, password):
        return bcrypt.check_password_hash(self.password_hash, password)
    
    def __repr__(self):
        return f"<User {self.username}>"

# Formulario personalizado para evitar que Flask-Admin intente mostrar password_hash
class UserForm(FlaskForm):
    username = StringField("Username", [validators.DataRequired()])
    password = PasswordField("Password", [validators.DataRequired()])

class UserAdmin(ModelView):
    form = UserForm  # Usar formulario personalizado
    column_exclude_list = ['password_hash']
    form_excluded_columns = ['password_hash']

    def on_model_change(self, form, model, is_created):
        if form.password.data:
            model.set_password(form.password.data)

class PokemonAdmin(ModelView):
    column_list = ['id', 'name', 'poke_type']
    column_labels = {
        'name': 'Nombre',
        'poke_type': 'Tipo'
    }

    form_columns = ['name', 'poke_type']
    form_overrides = {
        'poke_type': QuerySelectField
    }
    form_args = {
        'poke_type': {
            'query_factory': lambda: Type.query.all(),
            'get_label': 'name',
            'allow_blank': False
        }
    }

    def _poke_type_formatter(view, context, model, name):
        return model.poke_type.name

    column_formatters = {
        'poke_type': _poke_type_formatter
    }

class FavoriteAdmin(ModelView):
    column_list = ['id', 'user', 'pokemon']  # mostramos relaciones
    column_labels = {
        'user': 'Usuario',
        'pokemon': 'Pokémon'
    }
    column_display_pk = True

    form_columns = ['user', 'pokemon']
    form_overrides = {
        'user': QuerySelectField,
        'pokemon': QuerySelectField
    }
    form_args = {
        'user': {
            'query_factory': lambda: User.query.all(),
            'allow_blank': False,
            'get_label': 'username'
        },
        'pokemon': {
            'query_factory': lambda: Pokemon.query.all(),
            'allow_blank': False,
            'get_label': 'name'
        }
    }

    def _user_formatter(view, context, model, name):
        return model.user.username if model.user else '—'


    def _pokemon_formatter(view, context, model, name):
        return model.pokemon.name if model.pokemon else '—'


    column_formatters = {
        'user': _user_formatter,
        'pokemon': _pokemon_formatter
    }

class Pokemon(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True, nullable=False)
    type_id = db.Column(db.Integer, db.ForeignKey('type.id'), nullable=False)
    poke_type = db.relationship("Type", back_populates="pokemons")
    
    def __repr__(self):
        return f"<Pokemon {self.name}>"


class Type(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True, nullable=False)
    pokemons = db.relationship("Pokemon", back_populates="poke_type")


class Favorite(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    pokemon_id = db.Column(db.Integer, db.ForeignKey('pokemon.id'), nullable=False)  # Ahora es obligatorio

    user = db.relationship("User", back_populates="favorites")
    pokemon = db.relationship("Pokemon")
