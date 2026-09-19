from pathlib import Path

class Player:
    def __init__(self, name, characterType):
        self.name = name
        self.characterType = characterType
        self.inventory = []

    def move(self, direction):
        print(f"{self.name} moves {direction}.")


class Knight(Player):
    def __init__(self, name):
        super().__init__(name, "knight")
        self.inventory = ["sword", "shield"]
        
    def attack(self):
        print(f"{self.name} attacks with their {self.inventory[0]}!")

    def defend(self):
        print(f"{self.name} defends with their {self.inventory[1]}!")


class Wizard(Player):
    def __init__(self, name):
        super().__init__(name, "wizard")
        self.inventory = ["staff", "spellbook"]
        
    def castSpell(self):
        print(f"{self.name} casts a spell with their {self.inventory[0]}!")
        

    def readSpellbook(self):
        print(f"{self.name} reads their {self.inventory[1]} and learns a new spell!")
        

CHARACTERS_FILE = Path(__file__).parent / "characters.txt"

def savePlayer(player):
    with CHARACTERS_FILE.open("a", encoding="utf-8") as file:
        file.write(
            f"Character Name: {player.name}, "
            f"Character Type: {player.characterType}, "
            f"Inventory: {player.inventory}\n"
        )

def getChoice(prompt, validChoices):
    validChoices = tuple(choice.lower() for choice in validChoices)

    while True:
        choice = input(prompt).lower().strip()

        if choice in validChoices:
            return choice

        print(f"Invalid choice. Choose one of: {', '.join(validChoices)}")

def start():
    print("Welcome to the Choose Your Own Adventure game!")
    
    name = input("Enter your character's name: ")   
    while True:
        characterType = input(
            "Choose your character type (knight/wizard): "
        ).lower().strip()

        if characterType == "knight":
            player = Knight(name)
            break
        elif characterType == "wizard":
            player = Wizard(name)
            break
        else:
            print("Invalid character type. Please choose knight or wizard.")
    return player

def gameOver(message, player):
    print(message)
    savePlayer(player)  # Save the character's state at the end of the game
    print("Game Over.")
  
def knightPath(player):
    print("You are a brave knight!")
    print("Your inventory:", player.inventory)

    # narrative 1 for the knight character
    print("You find yourself in a dark forest. Up ahead you see a fork in the path.")
    # decision point 1 for the knight character
    print("Do you want to go left or right?")
    direction = getChoice("Enter 'left' or 'right': ", ["left", "right"])
    player.move(direction)

    # narrative 2 for the knight character
    if direction == "left":
        print("You hear a rustling in the bushes. Do you want to investigate " \
                "or keep moving?")
        # decision point 2 for the knight character
        choice = getChoice("Enter 'investigate' or 'leave': ", ["investigate", "leave"])
        if choice == "investigate":
            # narrative 3 for the knight character
                print ("A wild goblin jumps out and attacks you!")
                player.defend()
                player.attack()
                print("You fight bravely and defeat it.")
                print("You find a treasure chest with gold and jewels!")
                player.inventory.append("gold and jewels")
                print("You continue down the path and find your way out of the " \
                "forest.")
                gameOver("You win!, You made it out of the forest with treasure "
                            "in hand!", player)
        elif choice == "leave":
                # narrative 4 for the knight character
                print("You continue down the path and find a peaceful clearing.")
                print("You rest and regain your strength.")
                print("After resting, you continue down the path and encounter a " \
                        "ferocious dragon!")
                print("Do you want to fight the dragon or run away?")
                # decision point 3 for the knight character
                choice = getChoice("Enter 'fight' or 'run': ", ["fight", "run"])
                if choice == "fight":
                    print("You bravely fight the dragon and defeat it!")
                    player.attack()
                    print("You find a treasure chest with gold and jewels!")
                    player.inventory.append("gold and jewels")
                    print("You continue down the path and find your way out of the " \
                    "forest.")
                    gameOver("You win!, You made it out of the forest with treasure "
                                "in hand!", player)
                elif choice == "run":
                    print("You run away from the dragon, but it catches up to you and " \
                            "defeats you.")
                    gameOver("You lose!, You were defeated by the dragon.", player)

    elif direction == "right":
        # narrative 5 for the knight character
        print("You see a river blocking your path and the exit of the forest is on " \
        "the other side.")
        print("Do you want to swim across the river or look for a bridge?")
        # decision point 4 for the knight character
        choice = getChoice("Enter 'swim' or 'bridge': ", ["swim", "bridge"])
        if choice == "swim":
                print("You swim across the river, but the current is too strong and " \
                "you drown.")
                gameOver("You lose!, You drowned in the river.", player)
        elif choice == "bridge":
                print("You look for a bridge and find one to cross the river.")
                print("You continue down the path towards the exit.")
                print("You see a giant blocking your path.")
                # decision point 5 for the knight character
                print("Do you want to fight the giant or try to sneak past it?")
                choice = getChoice("Enter 'fight' or 'sneak': ", ["fight", "sneak"])
                if choice == "fight":
                        print("You bravely fight the giant and defeat it!")
                        player.attack()
                        print("You find a treasure chest with gold and jewels!")
                        player.inventory.append("gold and jewels")
                        print("You continue down the path and find your way out of " \
                        "the forest.")
                        gameOver("You win!, You made it out of the forest with " \
                                    "treasure in hand!", player)
                elif choice == "sneak":
                        print("You try to sneak past the giant, but it spots you and " \
                        "defeats you.")
                        gameOver("You lose!, You were defeated by the giant.", player)
    
def wizardPath(player):
    print("You are a wise wizard!")
    print("Your inventory:", player.inventory)
    # narrative 1 for the wizard character
    print("You find yourself in an enormous castle. Up ahead you see a fork in the path.")
    # decision point 1 for the wizard character
    print("Do you want to go left or right?")
    direction = getChoice("Enter 'left' or 'right': ", ["left", "right"])
    player.move(direction)

    # narrative 2 for the wizard character
    if direction == "left":
        print("You hear a strange noise coming from a room. Do you want to "
                "investigate?")
        # decision point 2 for the wizard character
        choice = getChoice("Enter 'yes' or 'no': ", ["yes", "no"])
        if choice == "yes":
            print("You investigate the room and find a hidden passage.")
            print("You continue down the hidden passage and find a treasure chest!")
            player.inventory.append("treasure chest")
            print("You continue down the path and find your way out of the castle.")
            gameOver("You win!, You found the treasure and escaped the castle!", player)
        elif choice == "no":
            print("You decide not to investigate and continue on your way.")
            # narrative 3 for the wizard character
            print("Off in the distance, you see a group of guards approaching.  " 
                    "Do you want to hide or confront them?")
            # decision point 3 for the wizard character
            choice = getChoice("Enter 'hide' or 'confront': ", ["hide", "confront"])
            if choice == "hide":
                print("You hide and the guards pass by without noticing you.")
                print("You continue down the path and find your way out of the " \
                "castle.")
                gameOver("You win!, You made it out of the castle safely!", player)
            elif choice == "confront":
                print("You confront the guards and engage in a battle.")
                player.readSpellbook()
                player.castSpell()
                print("You are quickly defeated by the guards.")
                gameOver("You lose!, You were defeated by the guards.  You spend" \
                " the rest of your days in the castle's dungeon.", player)
       
    # narrative 4 for the wizard character
    elif direction == "right":
        print("You end up in a large courtyard and hear a loud roar.")
        print("Do you want to investigate the roar or keep moving?")
        # decision point 4 for the wizard character
        choice = getChoice("Enter 'investigate' or 'leave': ", ["investigate", "leave"])
        if choice == "investigate":
                print("You investigate the roar and find a dragon.")
                # decision point 5 for the wizard character
                print("Do you want to fight the dragon or try to sneak past it?")
                choice = getChoice("Enter 'fight' or 'sneak': ", ["fight", "sneak"])
                if choice == "fight":
                        print("You bravely fight the dragon and defeat it!")
                        player.readSpellbook()
                        player.castSpell()
                        print("You find a treasure chest with gold and jewels!")
                        player.inventory.append("gold and jewels")
                        print("You continue down the path and find your way out of " \
                        "the castle.")
                        gameOver("You win!, You made it out of the castle with " \
                        "treasure in hand!", player)         
                elif choice == "sneak":
                        print("You try to sneak past the dragon, but it spots you "
                        "and defeats you.")
                        gameOver("You lose!, You were defeated by the dragon.", player)
        elif choice == "leave":
                print("You decide to leave the courtyard and continue on your way.")
                print("You find a peaceful garden and rest for a while.")
                print("After resting, you continue down the path and find your way " \
                "out of the castle.")
                gameOver("You win!, You made it out of the castle safely!", player)
            
while True:
    player = start()

    if player.characterType == "knight":
        knightPath(player)
    elif player.characterType == "wizard":
        wizardPath(player)

    playAgain = getChoice("Do you want to play again? (yes/no): ", ["yes", "no"])
    if playAgain != "yes":
        print("Thanks for playing!")
        break