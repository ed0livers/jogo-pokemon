import random
from classPokemon import Pokemon
from pokedex import pokedex
import copy

def verMeusPokemons(listaPokemons):
    for pokemon in listaPokemons:
        pokemon.verPokemon()

def verBancoPokemon(bancoPokemon):
    if not bancoPokemon:
        print("O banco de Pokémon está vazio.")
    else:
        print("POKÉMON NO BANCO:")
        for pokemon in bancoPokemon:
            pokemon.verPokemon()

def capturarPokemon(meusPokemons, bancoPokemon):
    pokemonSelvagem = random.choice(pokedex)
    print(f"Um {pokemonSelvagem.nome} selvagem apareceu!")
    
    pokemonSelvagemCopia = copy.deepcopy(pokemonSelvagem)
    meuPokemon = copy.deepcopy(meusPokemons[0])
    
    meuPokemon.batalhar(pokemonSelvagemCopia)
    
    if pokemonSelvagemCopia.hp == 0:
        print(f"Você capturou o {pokemonSelvagem.nome}!")
        pokemonSelvagemCopia.hp = pokemonSelvagem.hp  
        
        if len(meusPokemons) < 6:
            meusPokemons.append(pokemonSelvagemCopia)
        else:
            bancoPokemon.append(pokemonSelvagemCopia)
    else:
        print(f"Você perdeu a batalha e o {pokemonSelvagem.nome} fugiu!")

bancoPokemon = []

def menu():
    meusPokemons = [
        Pokemon("Mew", 100, 100, 100),
        Pokemon("Mewtwo", 110, 130, 106)
    ]

    while True:
        print("\nMENU:")
        print("1. Ver meus Pokémons")
        print("2. Ver Pokémon no Banco")
        print("3. Capturar Pokémon")
        print("4. Sair")

        escolha = input("Escolha uma opção: ")

        if escolha == "1":
            verMeusPokemons(meusPokemons)
        elif escolha == "2":
            verBancoPokemon(bancoPokemon)
        elif escolha == "3":
            capturarPokemon(meusPokemons, bancoPokemon)
        elif escolha == "4":
            print("Saindo do jogo...")
            break
        else:
            print("Opção inválida! Tente novamente.")

if __name__ == "__main__":
    menu()
