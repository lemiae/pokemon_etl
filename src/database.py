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
                hp INTEGER NOT NULL
            )
        """)
        conn.commit()

def add_pokemon(name: str, type_: str, hp: int):
    """Ajoute un Pokémon dans la base."""
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO pokemon (name, type, hp) VALUES (?, ?, ?)",
            (name, type_, hp)
        )
        conn.commit()

def get_all_pokemons():
    """Récupère tous les Pokémon de la base."""
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT id, name, type, hp FROM pokemon")
        return cursor.fetchall()