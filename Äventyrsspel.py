import random as rand
import time
import sys

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
        self.monster_strength = rand.randint(1, 20) + player1.level
        self.monster_health = rand.randint(1, 100) + player1.level
        self.monster = rand.choice(["Goblin", "Zombie", "Ogre", "Pig", "Hippo", "Skeleton", "Fox"])
        
class Trap:
    def __init__(self, player1):
        self.trap_name = rand.choice(["Bear trap", "Spike trap", "Goblin gang", "Wolf pack", "Electric lake", "Lava pool", "Loot lake"])
        self.trap_damage = rand.randint(player1.hp // 4, player1.hp // 2)
        self.right_answer = rand.choice(["1", "2", "3"])

    def trigger(self, player1):
        if self.trap_name == "Electric lake" or self.trap_name == "Lava pool" or self.trap_name == "Loot lake":
            print(f"""
        You fell into the {self.trap_name} and lost {self.trap_damage} hp""")
            player1.hp -= self.trap_damage
            print(f"Your hp is now {int(player1.hp)}")
        elif self.trap_name == "Bear trap" or self.trap_name == "Spike trap":
            print(f"""
        You triggered the {self.trap_name}!""")
            player1.hp -= self.trap_damage
            print(f"You lost {self.trap_damage} hp")
            print(f"Your hp is now {int(player1.hp)}")
        else:
            print(f"""
        You got attacked by the {self.trap_name}""")
            player1.hp -= self.trap_damage
            print(f"You lost {self.trap_damage} hp")
            print(f"Your hp is now {int(player1.hp)}")

class Items:
    def __init__(self):
        self.name = rand.choice(["longbow", "iron sword", "iron armor", "iron shield", "Health potion"])
        if self.name == "longbow" or self.name == "iron sword":
            self.strength_bonus = rand.uniform(0.1, 0.2)
        elif self.name == "Health potion":
            pass
        elif self.name == "iron armor" or self.name == "iron shield":
            self.hp_bonus = rand.uniform(0.1, 0.2)

def print_slow(string, tim):
    for letter in string:
        sys.stdout.write(letter)
        sys.stdout.flush()
        time.sleep(tim)

def display_stats(player1):
    print(f"""
 ___________________________
|  _______________________  |
 \ |                     | / 
        {player1.name}""")
    print_slow(f"""
         Health: {int(player1.hp)}
""", 0.01)                         
    print_slow(f"""
       Strenght: {int(player1.strength)}
""", 0.01)                        
    print_slow(f"""
          Level: {player1.level}
""", 0.01)                       
    print_slow(f"""
          xp: {player1.xp}/{(player1.level)*10}
""", 0.01)   
    print("""                    
_/ |_____________________| \_
|___________________________|""")
    


def intro(player1):
    player1.name = str(input("""
--?-- What is your name, adventurer?: """))
    
    print_slow(f"""
--?-- So {player1.name}, what could an adventurer like you be doing In Eldrath with all these
      monsters roaming around?
""", 0.04)
    answer1 = "1"
    answer2 = "2"
    answer3 = "3"
    response1 = ""
    while response1 != answer1 or answer2 or answer3:
        print("""
1. I'm just passing through
2. The kingdom needs my help to survive!
3. Say nothing""")
        response1 = str(input(""))
        if response1 == "1":
            print_slow("""
--?-- I understand, but before you go on with your adventure 
      you need to read this letter from the king""", 0.04)
            break
        if response1 == "2":
            print_slow("""
--?-- You are brave and noble, read this letter from the king
      to continue your journey""", 0.04)
            break
        if response1 == "3":
            print_slow("""
*You decide not to say anything and continue on your journey.*
*Suddenly a small letter falls from the sky and lands in your hands,*

It reads:""", 0.04)
            break
    
    print_slow(f"""
  _____________________________________          
 / \                                   \.
| O | In the forsaken realm of Eldrath, |.
 \_ | A once-prosperous kingdom,        |.
    | Now teeters on the edge,          |.
    | Of darkness.                      |.
    |                                   |.
    | A sinister portal has unleashed,  |.
    | A horde of nightmarish monsters,  |.
    | Terrorizing the land and          |.
    | Plunging it into chaos.           |.
    |                                   |.
    | Will you rise as the hero,        |.
    | Eldrath needs, only YOU can       |.
    | decide the kingdom's ultimate     |.
    | Destiny, We believe in you Hero!  |.
    |   ________________________________|___
    |  /      Sincerely, King Fabian VI    /.
    \_/___________________________________/.
""", 0.001)
    input("""
Press Enter To Continue""")

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
        print(f"You leveled up to level {player1.level}!\n")
        
def battle(monster1, player1, pack):
    time.sleep(1)
    while monster1.monster_health > 0 and player1.hp > 0:
        print(f'''
________________________________________________________
            
--{monster1.monster}--
{monster1.monster} Strength: {int(monster1.monster_strength)}
{monster1.monster} Health:   {int(monster1.monster_health)}

--{player1.name}--
{player1.name}  Strenght: {int(player1.strength)}
{player1.name}  Health:   {int(player1.hp)}    
''')
        print (f"{player1.name}'s turn")
        print_slow("""
        1. Attack
        2. Use Health potion
        3. Flee
""", 0.0075)
        Action = input("\nWhat will you do?: ")
        if Action == "1":
            print("\nAttacking...")
            time.sleep(1)
            monster1.monster_health -= player1.strength
            if monster1.monster_health <= 0:
                monster1.monster_health == 0
            print_slow(f"""
{player1.name} did {int(player1.strength)} damage
The {monster1.monster} has {monster1.monster_health} health left
                    """, 0.02)
            if monster1.monster_health <= 0:
                player1.xp += 5
                print(f"""
You killed the {monster1.monster}

You gained 5 experience""")
                level_up(player1)
                break
            else:
                print()
                print(f"{monster1.monster} attacking...")
                time.sleep(1)
                player1.hp -= monster1.monster_strength
                print_slow(f"""
The {monster1.monster} did {monster1.monster_strength} damage
Your health is now {int(player1.hp)}
                    """, 0.02)
        elif Action == "3":
            print("""
You fled""")
            break
        elif Action == "2":
            if "Health potion" in pack:
                player1.hp += 20
                if player1.hp > player1.max_hp:
                    player1.hp = player1.max_hp
                pack.remove ('Health potion')
                print(f"""
You used a Health potion and recovered 20 hp

Your current HP is {int(player1.hp)}/{int(player1.max_hp)}

Inventory: {pack}""")
            else:
                print ('''
You do not have any health potions
                       ''')

def travel(player1, trap, pack, monster1):
    departure = rand.randint(1, 3)
    chestitems = Items()
    door1 = "left"
    door2 = "middle"
    door3 = "right"
    response2 = ""
    while response2 != door1 or door2 or door3:
        print("""
________________________________________________________
              
  .-----.-----.     .-----.-----.     .-----.-----.     
:|      |      |: :|      |      |: :|      |      |:
:]      |      [: :]      |      [: :]      |      [:
:|    (O|O)    |: :|    (O|O)    |: :|    (O|O)    |:
:|      |      |: :|      |      |: :|      |      |:
:]      |      [: :]      |      [: :]      |      [:
:|______|______|: :|______|______|: :|______|______|:
              
     --Left--         --Middle--        --Right--
              
        There are three doors in front of you. 
        Left, middle and right""")
        response2 = input("""
Which one do you want to open? """)
        if response2 == "left":
            print(f"""
        You decided to open the {response2} door""")
            break
        if response2 == "middle":
            print(f"""
        You decided to open the {response2} door""")
            break
        if response2 == "right":
            print(f"""
        You decided to open the {response2} door""")
            break

    if departure == 1:
        print(rand.choice([f"""
        In the heart of the Whispering Woods, 
        where trees share secrets in hushed tones, 
        a mysterious mist clings to the air. 
        As you venture deeper, the ethereal whispers grow louder, 
        weaving tales of ancient magic. Suddenly, 
        the foliage shivers, 
        and from the shadows emerges a fearsome....""", 
                           f"""
        Beneath the moonlit graveyard lies a network of cursed crypts, 
        their stone doors sealed with ominous runes. 
        As you explore the shadowy catacombs, 
        whispers of long-forgotten souls fill the air. 
        An ancient curse awakens, and the ground trembles. 
        From the darkness rises the creature, 
        an undead behemoth with a hunger for the living."""]))
        input("""
                    Press Enter To Continue""")
        print_slow("You encountered a...", 0.04)
        monster1 = Monster(player1)
        print("""
                    Approaching...""")
        time.sleep(1)
        if monster1.monster == ("Skeleton"):
            print(r'''
          .-.
         (o.o)
          |3|
         __|__
       //.=|=.\\
      // .=|=. \\
      \\ .=|=. //
       / (_=_) \
        (:| |:)
         || ||
         () ()
         || ||
         || ||
        ==' '==
''')
        if monster1.monster == ("Goblin"):
            print(r'''
             ,      ,
            /(.-""-.)\
        |\  \/      \/  /|
        | \ / =.  .= \ / |
        \( \   o\/o   / )/
         \_, '-/  \-' ,_/
           /   \__/   \
           \ \__/\__/ /
         ___\ \|--|/ /___
       /`    \      /    `\
      /       '----'       \
''')
        if monster1.monster == ("Zombie"):
            print(r'''
              ,
          _,-""-._
        ,"        ".
       /    ,-,  ,"\
      "    /   \ | o|
      \    `-o-"  `-',
       `,   _.--'`'--`
         `--`---'                    
           ,' '      
         ./ ,  `,    
         / /     \
        (_)))_ _,"
           _))))_,
          (_,-._)))
''')
        if monster1.monster == ("Pig"):
            print(r'''
        &_--~- ,_
        {        ",
        (  )_ ,{ ,_@
         |/  {|\{
         ""   " "
''')
        if monster1.monster == ("Hippo"):
            print(r'''
          c~~p ,---------. 
     ,---'oo  )           \
    ( O O                  )/
     `=^='                 /
           \    ,     .   /
           \\  |-----'|  /
           ||__|    |_|__|
''')
        if monster1.monster == ("Fox"):
            print(r'''
       /|_/|
      / ^ ^(_o
     /    __.'
     /     \
    (_) (_) '._
      '.__     '. .-''-'.
         ( '.   ('.____.''
         _) )'_, )
        (__/ (__/
''')
        if monster1.monster == ("Ogre"):
            print(r'''
               __,='`````'=/__
              '//  (o) \(o) \ `'         _,-,
              //|     ,_)   (`\      ,-'`_,-\
            ,-~~~\  `'==='  /-,      \==```` \__
           /        `----'     `\     \       \/
        ,-`                  ,   \  ,.-\       \
       /      ,               \,-`\`_,-`\_,..--'\
      ,`    ,/,              ,>,   )     \--`````\
     (      `\`---'`  `-,-'`_,<   \      \_,.--'`
       `.      `--. _,-'`_,-`  |    \
        [`-.___   <`_,-'`------(    /
        (`` _,-\   \ --`````````|--`
         >-`_,-`\,-` ,          |
        <`,'     ,  /\          /
           \/\,-/ `/  \/`\_/V\_/
           (  ._. )    ( .__. )
           |      |    |      |
            \,---_|    |_---./
            ooOO(_)    (_)OOoo
''')
        battle(monster1, player1, pack)
    elif departure == 2:
        print("""
        You found a chest!""")
        if len(pack) < 5:
            print(f"""
You got a new {chestitems.name}!""")
            pack.append(chestitems.name) 
            if chestitems.name == "longbow" or chestitems.name == "iron sword":
                player1.strength *= (chestitems.strength_bonus + 1)
                print(f"""
Your strength increased by {round(chestitems.strength_bonus, 2) * 100}%""")
            elif chestitems.name == "iron armor" or chestitems.name == "iron shield":
                player1.hp *= (chestitems.hp_bonus + 1)
                print(f"""
Your health increased by {round(chestitems.hp_bonus, 2) * 100}%""")
        else:
            print(f"""
You would have gotten a {chestitems.name},
But your backpack is full. 
""")
            response3 = ""
            while response3 != "1" or "2":
                print(f"""
Would you like to delete an item to carry the {chestitems.name}?
1. Yes
2. No
""")
                response3 = input("")
                if response3 == "1":
                    response4 = ""
                    while response4 != "1" or "2" or "3" or "4" or "5":
                        print("What item would you like to delete?")
                        response4 = input(f"\n{pack}\n\nEnter the number of the item you want to delete: ")
                        if response4 == "1" or "2" or "3" or "4" or "5":
                            if response4 == "1":
                                response4 = 1
                            if response4 == "2":
                                response4 = 2
                            if response4 == "3":
                                response4 = 3
                            if response4 == "4":
                                response4 = 4
                            if response4 == "5":
                                response4 = 5
                            pack.pop(response4-1)
                            print(f"You deleted an item and you now have a {chestitems.name}")
                            print(f"""
You got a new {chestitems.name}!""")
                            pack.append(chestitems.name) 
                            if chestitems.name == "longbow" or chestitems.name == "iron sword":
                                player1.strength *= (chestitems.strength_bonus + 1)
                                print(f"\nYour strength increased by {round(chestitems.strength_bonus, 2) * 100}%")
                            elif chestitems.name == "iron armor" or chestitems.name == "iron shield":
                                player1.hp *= (chestitems.hp_bonus + 1)
                                print(f"\nYour health increased by {round(chestitems.hp_bonus, 2) * 100}%")
                        break
                    break
                if response3 == "2":
                    print("You did not delete an item")
                    break
                    
            
    elif departure == 3:
        print(f"""
        You encountered a {trap.trap_name}""")
        while True:
            player_answer = input("Guess a number between 1 and 3 to have a chance to escape!: ")
            if player_answer == "1" or player_answer == "2" or player_answer == "3":
                break
        if player_answer == trap.right_answer:
            print(f"""
        You avoided the {trap.trap_name} and got away safely
                  """)
        elif player_answer != trap.right_answer:
            trap.trigger(player1)



def menu(player1, monster1):
    print_slow("""                         
,--.   ,--.      ,--.                                  ,--.             ,--------.,--.                 
|  |   |  |,---. |  |,---. ,---. ,--,--,--.,---.     ,-'  '-. ,---.     '--.  .--'|  ,---. ,---.       
|  |.'.|  | .-. :|  | .--'| .-. ||        | .-. :    '-.  .-'| .-. |       |  |   |  .-.  | .-. :      
|   ,'.   \   --.|  \ `--.' '-' '|  |  |  \   --.      |  |  ' '-' '       |  |   |  | |  \   --.      
'--'   '--'`----'`--'`---' `---' `--`--`--'`----'      `--'   `---'        `--'   `--' `--'`----'      
,------.                 ,--.        ,------.                                                          
|  .-.  \  ,--,--.,--.--.|  |,-.     |  .-.  \ ,--.,--.,--,--,  ,---.  ,---.  ,---. ,--,--,  ,---.     
|  |  \  :' ,-.  ||  .--'|     /     |  |  \  :|  ||  ||      \| .-. || .-. :| .-. ||      \(  .-'     
|  '--'  /\ '-'  ||  |   |  \  \     |  '--'  /'  ''  '|  ||  |' '-' '\   --.' '-' '|  ||  |.-'  `)    
`-------'  `--`--'`--'   `--'`--'    `-------'  `----' `--''--'.`-  /  `----' `---' `--''--'`----' 
                                                               `---'
               




          """, 0.001)
    pack = []
    while player1.hp > 0:
        print_slow("""
        1.  Explore 
        2.  Stats 
        3.  Backpack 

Please Enter Your Choice: """, 0.0075)
        camp = input ('')
        if camp == "1":
            trap = Trap(player1)
            travel(player1, trap, pack, monster1)
        elif camp == "2":
            display_stats(player1)
        elif camp == "3":
            print(backpack(pack))
    if player1.hp < 0:
        print("""
        You got killed, better luck next time.
              """)

def main():
    player1 = Player()
    monster1 = Monster(player1)
    intro(player1)
    menu(player1, monster1)
main()