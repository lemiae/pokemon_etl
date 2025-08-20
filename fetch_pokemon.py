import requests
import pandas as pd
import sqlite3
from pathlib import Path
import logging

# --- Configuration du logging ---
logging.basicConfig(level=logging.INFO, format='%(levelname)s:%(message)s')

# --- Fonction pour récupérer un Pokémon depuis l'API ---
def fetch_pokemon(pokemon_id):
    url = f"https://pokeapi.co/api/v2/pokemon/{pokemon_id}"
    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        pokemon_dict = {
            'name': data['name'],
            'height': data['height'],
            'weight': data['weight'],
            'base_experience': data['base_experience'],
            'types': ', '.join([t['type']['name'] for t in data['types']])
        }
        logging.info(f"Pokémon {data['name']} récupéré avec succès")
        return pokemon_dict
    except requests.exceptions.RequestException as e:
        logging.error(f"Erreur pour Pokémon ID {pokemon_id} : {e}")
        return None

# --- Fonction pour créer un DataFrame depuis une liste de Pokémon ---
def create_dataframe(pokemon_list):
    df = pd.DataFrame(pokemon_list)
    return df

# --- Fonction pour sauvegarder un DataFrame dans SQLite ---
def save_to_sqlite(df, db_path='data/pokemon.db', table_name='pokemon'):
    conn = sqlite3.connect(db_path)
    df.to_sql(table_name, conn, if_exists='replace', index=False)
    logging.info(f"Données sauvegardées dans {db_path} table {table_name}")
    conn.close()

# --- Fonction principale ---
def main():
    pokemon_list = []
    for i in range(1, 6):  # récupérer les 5 premiers Pokémon
        pokemon = fetch_pokemon(i)
        if pokemon:
            pokemon_list.append(pokemon)

    df = create_dataframe(pokemon_list)
    print(df)
    save_to_sqlite(df)

if __name__ == "__main__":
    main()
