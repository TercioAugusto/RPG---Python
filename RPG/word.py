class Player:
    def __init__(self, name, classe, health, attack, defense, mana):
        self.name = name
        self.classe = classe
        self.health = health
        self.attack = attack
        self.defense = defense
        self.mana = mana
        self.inventory = []

    def __str__(self):
        return (f"Nome: {self.name}\n"
                f"Classe: {self.classe}\n"
                f"Vida: {self.health}\n"
                f"Ataque: {self.attack}\n"
                f"Defesa: {self.defense}\n"
                f"Mana: {self.mana}\n"
                f"Inventário: {', '.join(self.inventory)}")

class Warrior:
    def __init__(self):
        self.classe = "Guerreiro"
        self.health = 120
        self.attack = 15
        self.defense = 10
        self.mana = 5
        self.inventory = ["Espada", "Escudo"]

class Mage:
    def __init__(self):
        self.classe = "Mago"
        self.health = 80
        self.attack = 10
        self.defense = 5
        self.mana = 20
        self.inventory = ["Varinha", "Poção de Mana"]

class Archer:
    def __init__(self):
        self.classe = "Arqueiro"
        self.health = 100
        self.attack = 12
        self.defense = 8
        self.mana = 10
        self.inventory = ["Arco", "Flechas"]

class Game:
    def __init__(self):
        self.player = None

    def start(self):
        print("Bem-vindo ao RPG!")
        player_name = input("Digite o nome do seu personagem: ")
        
        classe_name = int(input("Digite 1 para Guerreiro, 2 para Mago e 3 para Arqueiro: "))
        
        if classe_name == 1:
            player_class = Warrior()
        elif classe_name == 2:
            player_class = Mage()
        elif classe_name == 3:
            player_class = Archer()
        else:
            print("O número digitado está incorreto, tente novamente")
            return
        
        self.player = Player(player_name, player_class.classe, player_class.health, player_class.attack, player_class.defense, player_class.mana)
        print(self.player)

game = Game()
game.start()