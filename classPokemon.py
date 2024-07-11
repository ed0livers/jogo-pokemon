import random

class Pokemon:
  def __init__(self, nome, poder, velocidade, hp):
    self.nome = nome
    self.poder = poder
    self.velocidade = velocidade
    self.hp = hp

  def verPokemon(self):
    print(f'''
NOME: {self.nome}
PODER: {self.poder}
VELOCIDADE: {self.velocidade}
VIDA: {self.hp} 

''')

  def perderVida(self, dano):
    self.hp = max(self.hp - dano, 0)
    print (f"{self.nome} sofreu {dano} de dano, sua nova vida é: {self.hp}")
    return self.hp

  def atacar(self, defensor):
    print(f"{self.nome} atacou {defensor.nome} e causou {self.poder} de dano")
    defensor.perderVida(self.poder)

  def batalhar(self, pokemonInimigo):
    print(f"Batalha entre {self.nome} e {pokemonInimigo.nome} iniciada!")
    round = 1
    if (self.velocidade > pokemonInimigo.velocidade):
      while (self.hp > 0 and pokemonInimigo.hp > 0):
        print(F"{round}° ROUND")
        round += 1
        self.atacar(pokemonInimigo)
        if pokemonInimigo.hp > 0:
          pokemonInimigo.atacar(self)
        else:
          print(f"A vida do {pokemonInimigo.nome} é 0, o vencedor é o {self.nome}")
          break
        if self.hp <= 0:
            print(f"A vida do {self.nome} é 0, o vencedor é o {pokemonInimigo.nome}")
            break
        else:
          pass

    elif (pokemonInimigo.velocidade > self.velocidade):
      while (self.hp > 0 and pokemonInimigo.hp > 0):
        print(F"{round}° ROUND")
        round += 1
        pokemonInimigo.atacar(self)
        if self.hp > 0:
          self.atacar(pokemonInimigo)
        else:
          print(f"A vida do {self.nome} é 0, o vencedor é {pokemonInimigo.nome}")
          break
        if pokemonInimigo.hp <= 0:
          print(f"A vida do {pokemonInimigo.nome} é 0, o vencedor é {self.nome}")
          break

    elif (pokemonInimigo.velocidade == self.velocidade):
      primeiro = random.choice([self, pokemonInimigo])
      segundo = pokemonInimigo if primeiro == self else self
      while (self.hp > 0 and pokemonInimigo.hp > 0):
        print(F"{round}° ROUND")
        round += 1
        primeiro.atacar(segundo)
        if (segundo.hp > 0):
          segundo.atacar(primeiro)
        else:
          print(f"A vida do {segundo.nome} é 0, o vencedor é {primeiro.nome}!")
        if (primeiro.hp <= 0):
          print(f"A vida do {primeiro.nome} é 0, o vencedor é {segundo.nome}!")
          
def verMeusPokemons(listaPokemons):
  for pokemon in listaPokemons:
    pokemon.verPokemon()


