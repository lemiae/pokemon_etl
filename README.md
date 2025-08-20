# Projet Pokémon ETL

## Objectif
Récupérer des données Pokémon depuis l'API PokéAPI, les transformer en DataFrame et les stocker dans une base SQLite.  
Ce projet sert d'exemple d'ETL simple en Python.

## Structure du projet
pokemon_etl/
├─ data/ # Base SQLite et éventuels CSV
├─ src/ # Scripts Python
├─ notebooks/ # Notebooks pour exploration
├─ README.md

## Installation

1. Cloner le projet :
   ```bash
   git clone <url-du-repo>
   cd <nom-du-dossier>
2. Créer un environnement virtuel :
    python -m venv venv312
    source venv312/bin/activate  # sous Linux/Mac
    venv312\Scripts\activate     # sous Windows

## Utilisation

1. Lancer le projet :
     ```bash
     python main.py
2. Exemple d'affichage attendu :
    ```bash
    Pokémons enregistrés :
    (1, 'Pikachu', 'Électrik', 35)
3. Installation dépendances :
    ```bash
    pip install pandas requests
4. Lancement :
    ```bash
    python src/fetch_pokemon.py

## Le script :
- Récupère les 5 premiers Pokémon depuis l'API
- Transforme les données en DataFrame
- Sauvegarde les données dans data/pokemon.db

## Résultat :
- DataFrame affiché dans la console
- Base SQLite pokemon.db avec table pokemon

## Option :
Exporter les données en CSV:
    ```bash
    df.to_csv('data/pokemon.csv', index=False)
