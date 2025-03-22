from src.app import app, db
from src.models import Type

# Lista fija de tipos Pokémon
TYPES = [
    "Normal", "Fuego", "Agua", "Planta", "Eléctrico", "Hielo", "Lucha",
    "Veneno", "Tierra", "Volador", "Psíquico", "Bicho", "Roca", "Fantasma",
    "Dragón", "Siniestro", "Acero", "Hada"
]

# Ejecutar en contexto de aplicación
with app.app_context():
    for name in TYPES:
        # Verificamos si ya existe
        if not Type.query.filter_by(name=name).first():
            db.session.add(Type(name=name))
            print(f"✅ Insertado: {name}")
        else:
            print(f"⏩ Ya existe: {name}")
    db.session.commit()
    print("🎉 Seed completado correctamente.")
