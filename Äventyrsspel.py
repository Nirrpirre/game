import random as rand
import time
#jief
class Player:
    def __init__(self):
        self.name = ""
        self.max_hp = 100
        self.hp = 100
        self.strength = 10
        self.level = 1
        self.xp = 0
class Monster:
    def __init__(self, player1):
        self.monster_strength = rand.randint(1, 10) + player1.level
        self.monster_health = rand.randint(1, 100) + player1.level
        self.monster = rand.choice(["Goblin", "Zombie", "Orc", "Pig", "Monkey"])

class Trap:
    def __init__(self, player1):
        self.trap_name = rand.choice(["Bear trap", "Spike trap", "Electric lake", "Lava pool"])
        self.trap_damage = rand.randint(player1.hp // 4, player1.hp // 2)

    def trigger(self, player1):
        if self.trap_name == "Electric lake" or "Lava pool":
            print(f"""
        You fell into the {self.trap_name}""")
        else:
            print(f"""
        You triggered a {self.trap_name}!""")
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
        self.name = rand.choice(["longbow", "iron sword", "iron armor", "iron shield", "Health potion"])
        if self.name == "longbow" or self.name == "iron sword":
            self.strength_bonus = rand.uniform(0.1, 0.2)
        elif self.name == "Health potion":
            pass
        elif self.name == "iron armor" or self.name == "iron shield":
            self.hp_bonus = rand.uniform(0.1, 0.2)

def display_stats(player1):
    print(f"Health: {int(player1.hp)}")
    print(f"Strength: {int(player1.strength)}")
    print(f"Level: {player1.level}")
    print(f"Xp: {player1.xp}")

def intro(player1):
    player1.name = str(input("""
                    What is your name, adventurer?: """))
    
    if input("Enter 1 to read the story or any other key to continue with the adventure: ") == "1":
        print("""
    In the forsaken realm of Eldrath, 
    a once-prosperous kingdom now teeters on the edge of darkness. 
    A sinister portal has unleashed a horde of nightmarish monsters, 
    terrorizing the land and plunging it into chaos. 
    As the last descendant of an ancient monster-slaying lineage, 
    you emerge as the kingdom's reluctant savior.

    Will you rise as the hero Eldrath needs, 
    purging the land of its monstrous scourge, 
    or succumb to the relentless darkness that threatens to consume all? 
    The battle against the monsters has begun, 
    and only YOU can decide the kingdom's ultimate destiny.
          
    We believe in you, our hero!
\n""")
    else:
        print(f"""
                    I understand {player1.name}, maybe another time""")

def backpack(pack):
    if not pack:
        return """
Your backpack is empty"""
    else:
        return pack

def level_up(player1):
    xp_required = player1.level * 10
    if player1.xp >= xp_required:
        player1.level += 1
        player1.strength += 2
        player1.hp += 20
        player1.xp = 0
        print(f"""
You leveled up to level {player1.level}!""")
        


def battle(monster1, player1, pack):
    print(f'You encountered a \n--{monster1.monster}--\nstrength: {monster1.monster_strength}\nHealth: {monster1.monster_health}')
    while monster1.monster_health > 0 and player1.hp > 0:
        print (f"{player1.name}s turn")
        print("""
                1. Attack
                2. Use Health potion
                3. Flee
                                """)
        Action = input("Attack, Use Health potion, Flee?: ")
        if Action == "1":
            monster1.monster_health -= player1.strength
            if monster1.monster_health <= 0:
                monster1.monster_health = 0
            print(f"""
                    --{monster1.monster}--
                    {monster1.monster} Strength: {monster1.monster_strength}
                    {monster1.monster} Health:   {monster1.monster_health}

                    --{player1.name}--
                    {player1.name}  Strenght: {player1.strength}
                    {player1.name}  Health:   {player1.hp}
                    """)
            if monster1.monster_health <= 0:
                player1.xp += 5
                print(f"""
You killed the {monster1.monster}
You gained 5 experience""")
                level_up(player1)
                break
            else:
                player1.hp -= monster1.monster_strength
        elif Action == "3":
            print("You fled")
            break
        elif Action == "2":
            if "Health potion" in pack:
                player1.hp += 20
                if player1.hp > player1.max_hp:
                    player1.hp = player1.max_hp
                pack.remove ('Health potion')
                print(f"""
You used a health potion and recovered 20 hp
Your hp is now: {player1.hp}""")
            else:
                print ('You do not have any health potions')


def travel(player1, trap, pack, monster1):
    departure = rand.randint(1, 3)
    chestitems = Items()
    if departure == 1:
        print(rand.choice([f"""
                           In the heart of the Whispering Woods, 
                           where trees share secrets in hushed tones, 
                           a mysterious mist clings to the air. 
                           As you venture deeper, the ethereal whispers grow louder, 
                           weaving tales of ancient magic. Suddenly, 
                           the foliage shivers, and from the shadows emerges a fearsome --{monster1.monster}--.""", 
                           f"""
                           Within the crumbling walls of an abandoned asylum, 
                           the air is thick with the lingering despair of tortured souls. 
                           As your group explores the decaying corridors, 
                           distant cries echo through the darkness. 
                           A cold wind sweeps the hallway, extinguishing torches, 
                           and in the pitch-black silence, a ghastly --{monster1.monster}-- materializes before you.""",
                           f"""
                           Across the vast expanse of the Frozen Tundra, 
                           where icy winds howl and snow blankets the land, 
                           an ominous stillness settles. As your party trudges through the deep snow, 
                           strange footprints appear, leading to an ancient, frozen structure. 
                           Suddenly, the icy winds form into an icy --{monster1.monster}-- that hungers for warmth.""", 
                           f"""
                           Beneath the city, 
                           a labyrinth of forgotten catacombs hides the bones of countless generations. 
                           Torchlight flickers on damp walls as your party delves into the depths. 
                           Unearthly whispers fill the air, 
                           and shadows meld into a monstrous --{monster1.monster}-- that hungers for the living.""", 
                           f"""
                           Perched atop a mountain, 
                           the celestial observatory offers a breathtaking view of the cosmos. 
                           As your party marvels at the stars, 
                           a sudden cosmic alignment triggers a surge of otherworldly energy. 
                           The air crackles, and a celestial --{monster1.monster}-- descends from the heavens, 
                           drawn by the celestial convergence.""", 
                           f"""
                           In the ocean's abyssal depths, 
                           where sunlight struggles to penetrate, 
                           a hidden abyss conceals unspeakable horrors.
                           Your submarine descends into the crushing pressure, 
                           and strange, luminescent creatures swim by. Suddenly, 
                           a colossal --{monster1.monster}-- emerges, 
                           its tentacles reaching out with malicious intent.""", 
                           f"""
                           Amidst the ruins of a once-thriving hamlet, 
                           a ghostly mist clings to the dilapidated buildings. 
                           The wind carries distant whispers of tragedy, 
                           and as your party explores, 
                           the mournful wails coalesce into a haunting --{monster1.monster}-- 
                           that seeks to bind the living to its sorrowful fate.""",
                           f"""
                           Amidst the bubbling lava and ashy plumes of a volcanic caldera, 
                           your party ventures toward an ancient altar. 
                           Unbeknownst to them, the molten rock stirs, 
                           and the ground trembles. 
                           Rivers of magma flow as a fiery {monster1.monster} emerges from the depths, 
                           hungry for the intruders."""]))
        
        monster1 = Monster(player1)
        battle(monster1, player1, pack)
    elif departure == 2:
        print("You found a chest!")
        if len(pack) < 5:
            if chestitems.name == "longbow" or chestitems.name == "iron sword":
                player1.strength *= (chestitems.strength_bonus + 1)
                print(f"Your strength increased by {round(chestitems.strength_bonus, 2) * 100}%")
            elif chestitems.name == "iron armor" or chestitems.name == "iron shield":
                player1.hp *= (chestitems.hp_bonus + 1)
                print(f"""
Your health increased by {round(chestitems.hp_bonus, 2) * 100}%""")
            print(f"""
You got a new {chestitems.name}""")
            pack.append(chestitems.name) 
        else:
            print("""
Your backpack is full. You cannot carry more items.""")
    elif departure == 3:
        rätt_svar = rand.randint(1,3)
        print(f"You encountered a {trap.trap_name}")
        while True:
            player_answer = input("""
Guess a number between 1 and 4 to have a chance to escape!: """)
            if player_answer == "1" or player_answer == "2" or player_answer == "3" or player_answer == "4":
                break
        if player_answer == (rätt_svar):
            print("You avoided the trap and got away safely")
        elif player_answer != (rätt_svar):
            trap.trigger(player1)

def menu(player1, monster1):
    print("""
            *********Welcome to The Dark Dungeons*********
          """)
    pack = []
    while player1.hp > 0:
        camp = input("""
                1.  Begin your adventure
                2.  Stats 
                3.  Backpack 

Please enter your choice: """)
        if camp == "1":
            trap = Trap(player1)
            travel(player1, trap, pack, monster1)
        elif camp == "2":
            display_stats(player1)
        elif camp == "3":
            print(backpack(pack))
    if player1.hp < 0:
        print("""
You got killed, better luck next time.""")

def main():
    player1 = Player()
    monster1 = Monster(player1)
    intro(player1)
    menu(player1, monster1)

main()