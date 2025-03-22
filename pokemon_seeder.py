# pokemon_seeder.py
from src.app import app, db
from src.models import Type, Pokemon

# Lista de Pokémon con su tipo correspondiente
POKEMON_DATA = [
    ("Pikachu", "Eléctrico"),
    ("Charmander", "Fuego"),
    ("Squirtle", "Agua"),
    ("Bulbasaur", "Planta"),
    ("Jigglypuff", "Hada"),
    ("Geodude", "Roca"),
    ("Machop", "Lucha"),
    ("Gastly", "Fantasma"),
    ("Abra", "Psíquico"),
    ("Sandshrew", "Tierra")
]

with app.app_context():
    for name, type_name in POKEMON_DATA:
        type_obj = Type.query.filter_by(name=type_name).first()
        if not type_obj:
            print(f"❌ Tipo '{type_name}' no encontrado. Skipping {name}")
            continue

        exists = Pokemon.query.filter_by(name=name).first()
        if exists:
            print(f"⏩ Ya existe: {name}")
            continue

        new_pokemon = Pokemon(name=name, type_id=type_obj.id)
        db.session.add(new_pokemon)
        print(f"✅ Insertado: {name} ({type_name})")

    db.session.commit()
    print("🎉 Pokémon insertados correctamente.")
