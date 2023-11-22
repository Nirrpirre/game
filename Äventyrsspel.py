import random as rand

class Player:
    def __init__(self):
        self.name = ""
        self.hp = 100
        self.strength = 10
        self.level = 1
        self.xp = 0


class Monster:
    def __init__(self, player1):
        self.monster_strength = rand.randint(1, 1) + player1.level
        self.monster_health = rand.randint(1, 100) + player1.level
        self.monster = rand.choice(["goblin", "zombie", "orc", "pig"])


class Trap:
    def __init__(self, player1):
        self.trap_name = rand.choice(["bear", "spike"])
        self.trap_damage = rand.randint(player1.hp // 4, player1.hp // 2)

    def trigger(self, player1):
        print(f"You triggered a {self.trap_name} trap!")
        player1.hp -= self.trap_damage
        print(f"You lost {self.trap_damage} hp")
        print(f"Your hp is now {int(player1.hp)}")


def display_stats(player1):
    print(f"Health: {int(player1.hp)}")
    print(f"Strength: {int(player1.strength)}")
    print(f"Level: {player1.level}")
    print(f"Xp: {player1.xp}")

class Items:
    def __init__(self):
        self.name = rand.choice(["longbow", "iron sword", "iron armor", "iron shield"])
        if self.name == "longbow" or self.name == "iron sword":
            self.strength_bonus = rand.uniform(0.1, 0.2)
        else:
            self.hp_bonus = rand.uniform(0.1, 0.2)

def intro(player1):
    print("What is your name, adventurer?: ")
    player1.name = str(input(""))

    print("Enter 1 to begin the adventure or any other key to exit: ")
    if int(input()) == 1:
        print("""
            In the forsaken realm of Eldrath, 
            a once-prosperous kingdom now teeters on the edge of darkness. 
            A sinister portal has unleashed a horde of nightmarish monsters, 
            terrorizing the land and plunging it into chaos. 
            As the last descendant of an ancient monster-slaying lineage, 
            you emerge as the kingdom's reluctant savior.
 
            The once-idyllic landscapes now echo with the growls of grotesque creatures that lurk in every shadow.
            From haunted forests to desolate dungeons, 
            you must navigate treacherous terrains to confront the source of the malevolence.

            As you traverse the kingdom, you encounter fellow survivors, 
            each harboring their own tales of loss and desperation. Together, 
            you form an unlikely fellowship, 
            pooling your skills and resources to face increasingly formidable monsters. 
            Unearth the secrets of Eldrath's downfall, 
            unlocking ancient powers that enhance your combat abilities and reveal the monsters' vulnerabilities.

            The stakes escalate as you delve into the heart of darkness, 
            facing colossal bosses and deciphering cryptic clues, 
            that unveil the true nature of the otherworldly invasion. 
            Your choices impact the kingdom's fate, 
            determining whether Eldrath succumbs to eternal night or emerges victorious against the monstrous tide.

            Will you rise as the hero Eldrath needs, 
            purging the land of its monstrous scourge, 
            or succumb to the relentless darkness that threatens to consume all? 
            The battle against the monsters has begun, 
            and only YOU can decide the kingdom's ultimate destiny.
          
            We believe in you, our hero!
\n""")
    else:
        print(f"I understand {player1.name}, maybe another time")

            

def backpack(pack):
    if not pack:
        return "Your backpack is empty"
    else:
        return pack

def level(player1):
    if player1.xp < 5:
        player1.level = 1
    elif 5 <= player1.xp < 10:
        player1.level = 2
    elif 10 <= player1.xp < 15:
        player1.level = 3
    elif 15 <= player1.xp < 20:
        player1.level = 4
    elif 20 <= player1.xp < 25:
        player1.level = 5
    elif 25 <= player1.xp < 30:
        player1.level = 6
    elif 30 <= player1.xp < 35:
        player1.level = 7
    elif 35 <= player1.xp < 40:
        player1.level = 8
    elif 40 <= player1.xp < 45:
        player1.level = 9
    elif 45 <= player1.xp < 50:
        player1.level = 10

def battle(monster1, player1):
    print(f'You encounterd a \n--{monster1.monster}--\nstrength: {monster1.monster_strength}\nHealth: {monster1.monster_health}')
    while monster1.monster_health > 0 and player1.hp > 0:
        print("""
                1. Attack
                2. Flee
                                """)
        Action = input("Attack or Flee ")
        if Action == "1":
            monster1.monster_health -= player1.strength
            print(f"{monster1.monster} Health:{monster1.monster_health} {player1.name} Health:{player1.hp}")
            if monster1.monster_health <= 0:
                player1.xp += 5
                print(f"You killed the {monster1.monster}\nYou gained 5 experience")
                level(player1)
                break
            else:
                player1.hp -= monster1.monster_strength
        elif Action == "2":
            print("You fled")
            break



def travel(player1, trap, pack):
    departure = rand.randint(1, 3)
    if departure == 1:
        monster1 = Monster(player1)
        battle(monster1, player1)
    elif departure == 2:
        chestitems = Items()
        print("You found a chest!")
        if chestitems.name == "longbow" or chestitems.name == "iron sword":
            player1.strength *= (chestitems.strength_bonus + 1)
            print(f"Your strength increased by {round(chestitems.strength_bonus, 1)*100}%")
        else:
            player1.hp *= (chestitems.hp_bonus + 1)
            print(f"Your health increased by {round(chestitems.hp_bonus, 1)*100}%")
        print(f"You got a new {chestitems.name}")
        pack.append(chestitems.name)
    elif departure == 3:
        print("You encountered a trap")
        if rand.random() < 0.5:
            trap.trigger(player1)
        else:
            print("You avoided the trap and got away safely")

def menu(player1):
    print("**********Welcome to The Dark Dungeons**********\n")
    pack = []
    while player1.hp > 0:
        camp = input("""
                        1. Begin your adventure
                        2. Stats
                        3. Backpack

                        Please enter your choice: """)
        if camp == "1":
            trap = Trap(player1)
            travel(player1, trap, pack)
        elif camp == "2":
            display_stats(player1)
        elif camp == "3":
            print(backpack(pack))
        


def main():
    player1 = Player()
    intro(player1)
    menu(player1)
main()

