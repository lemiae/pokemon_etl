import sqlite3
from pathlib import Path

# Chemin vers la base de données (dans le dossier data)
DB_PATH = Path("data/pokemon.db")

def get_connection():
    """Retourne une connexion SQLite."""
    return sqlite3.connect(DB_PATH)

def init_db():
    """Crée la table Pokémon si elle n’existe pas."""
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS pokemon (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                type TEXT NOT NULL,
                hp INTEGER NOT NULL,
                attaque INTEGER,
                defense INTEGER,
                vitesse INTEGER
            )
        """)
        conn.commit()

def add_pokemon(name: str, type_: str, hp: int, attaque: int = None, defense: int = None, vitesse: int = None):
    """Ajoute un Pokémon dans la base."""
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO pokemon (name, type, hp, attaque, defense, vitesse) VALUES (?, ?, ?, ?, ?, ?)",
            (name, type_, hp, attaque, defense, vitesse)
        )
        conn.commit()

def get_all_pokemons():
    """Récupère tous les Pokémon de la base."""
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT id, name, type, hp, attaque, defense, vitesse FROM pokemon")
        return cursor.fetchall()

def delete_pokemon(pokemon_id):
    """Supprime un Pokémon de la base."""
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute("DELETE FROM pokemon WHERE id = ?", (pokemon_id,))
        conn.commit()
