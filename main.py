from src.database import init_db, add_pokemon, get_all_pokemons

def main():
    # Initialisation de la base (création si elle n’existe pas déjà)
    init_db()

    # Exemple : ajout d’un Pokémon
    add_pokemon("Pikachu", "Électrik", 35)

    # Récupération et affichage
    pokemons = get_all_pokemons()
    print("Pokémons enregistrés :")
    for p in pokemons:
        print(p)

if __name__ == "__main__":
    main()