# Projet Pokémon - Base de données SQLite

Petit projet en Python pour gérer une base de données de Pokémon avec SQLite.

## Structure du projet
├── data/ # Contient la base SQLite (pokemon.db)
├── notebooks/ # Pour tests et explorations Jupyter (optionnel)
├── src/ # Code source
│ └── database.py # Fonctions pour gérer la base
├── main.py # Point d'entrée du projet
└── README.md # Documentation

## Installation

1. Cloner le projet :
   ```bash
   git clone <url-du-repo>
   cd <nom-du-dossier>
2. Créer un environnement virtuel :
    python -m venv venv
    source venv/bin/activate  # sous Linux/Mac
    venv\Scripts\activate     # sous Windows

## Utilisation

1. Lancer le projet :
     ```bash
     python main.py
2. Exemple d'affichage attendu :
    ```bash
    Pokémons enregistrés :
    (1, 'Pikachu', 'Électrik', 35)

## Prochaines améliorations possible :

- Ajouter plus de champs (attaque, défense, vitesse…)
- Créer une interface utilisateur (console ou web)
- Charger des données depuis un fichier CSV
