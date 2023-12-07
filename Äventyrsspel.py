import random as rand
import time
#jief
#fjiwf
#hdhwdi
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
        self.monster = rand.choice(["Goblin", "Zombie", "Ogre", "Pig", "Monkey", "Skeleton"])
        
class Trap:
    def __init__(self, player1):
        self.trap_name = rand.choice(["Bear trap", "Spike trap", "Goblin gang", "Wolf pack", "Electric lake", "Lava pool", "Loot lake"])
        self.trap_damage = rand.randint(player1.hp // 4, player1.hp // 2)
    

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
    print(f"""
 ___________________________
|  _______________________  |
 \ |                     | /               
         Health: {int(player1.hp)}                    
                            
       Strenght: {int(player1.strength)}
                           
        Level: {player1.level}
                           
        xp: {player1.xp}/{(player1.level)*10}                
_/ |_____________________| \_
|___________________________|
""")

def intro(player1):
    player1.name = str(input("""
                    What is your name, adventurer?: """))
    
    print(f"""
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
""")
    input("Press Enter To Continue")

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
    print(f'''
You encountered a
          
                    --{monster1.monster}--
    {monster1.monster} Strength: {int(monster1.monster_strength)}
    {monster1.monster} Health:   {int(monster1.monster_health)}

                    --{player1.name}--
    {player1.name}  Strenght: {int(player1.strength)}
    {player1.name}  Health:   {int(player1.hp)}    
''')
    
    while monster1.monster_health > 0 and player1.hp > 0:
        print (f"{player1.name}'s turn")
        print("""
                    1. Attack
                    2. Use Health potion
                    3. Flee
                                """)
        Action = input("What will you do?: ")
        if Action == "1":
            print("Attacking...")
            time.sleep(1)
            monster1.monster_health -= player1.strength
            if monster1.monster_health <= 0:
                monster1.monster_health == 0
            print(f"""
                    --{monster1.monster}--
                    {monster1.monster} Strength: {int(monster1.monster_strength)}
                    {monster1.monster} Health:   {int(monster1.monster_health)}

                    --{player1.name}--
                    {player1.name}  Strenght: {int(player1.strength)}
                    {player1.name}  Health:   {int(player1.hp)}
                    """)
            if monster1.monster_health <= 0:
                player1.xp += 5
                print_slow(f"""
You killed the {monster1.monster}
You gained 5 experience""", 0.04)
                level_up(player1)
                break
            else:
                print()
                print(f"{monster1.monster} attacking...")
                time.sleep(1)
                player1.hp -= monster1.monster_strength
                print(f"""
--{player1.name}--
{player1.name}  Strenght: {int(player1.strength)}
{player1.name}  Health:   {int(player1.hp)}
                    """)
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
You used a Health potion and recovered 20 hp

Your current HP is {int(player1.hp)}/{int(player1.max_hp)}

Inventory: {pack}""")
            else:
                print ('''
You do not have any health potions
                       ''')

def travel(player1, trap, pack, monster1):
    departure = rand.randint(3, 3)
    chestitems = Items()
    if departure == 1:
        print(rand.choice([f"""
                           In the heart of the Whispering Woods, 
                           where trees share secrets in hushed tones, 
                           a mysterious mist clings to the air. 
                           As you venture deeper, the ethereal whispers grow louder, 
                           weaving tales of ancient magic. Suddenly, 
                           the foliage shivers, and from the shadows emerges a fearsome....""", 
                           f"""
                           Beneath the moonlit graveyard lies a network of cursed crypts, 
                           their stone doors sealed with ominous runes. 
                           As you explore the shadowy catacombs, 
                           whispers of long-forgotten souls fill the air. 
                           An ancient curse awakens, and the ground trembles. 
                           From the darkness rises the creature, 
                           an undead behemoth with a hunger for the living."""]))
        input("Press Enter To Continue")
        monster1 = Monster(player1)
        print("""
Approaching...""")
        time.sleep(1)
        if monster1.monster == ("Skeleton"):
            print(r'''
                                          __ _
                                        .'  Y '>,
            )| \)                      / _   _   \
           //)|\\                      )(_) (_)(|}
          / ^| \ \                     {  4A   } /
         //^| || \\                     \uLuJJ/\l
        >//||| |\\\|                    |3    p)/
        | """""  7/>l__ _____ ____      /nnm_n//
        L>_   _-< 7/|_-__,__-)\,__)(".  \_>-<_/D
        )D" Y "c)  9)       //V     \_"-._.__G G_c__.-__<"/ ( \
         | | |  |(|               < "-._"> _.G_.___)\   \7\
          \"=" // |              (,"-.__.|\ \<.__.-" )   \ \
           '---'  |              |,"-.__"| \!"-.__.-".\   \ \
             |_;._/              (_"-.__"'\ \"-.__.-".|    \_\
             )(" V                \"-.__"'|\ \-.__.-".)     \ \
                (                  "-.__'"\_\ \.__.-"./      \ l
                 )                  ".__"">>G\ \__.-">        V )
                                        ""  G<\ \_.-"        ./7
                                             G<\ \          ///
                                        ___  GD'
                                   /  /             )E_>"
                                 _/  (             |  \()
                                / \ /              |  |
                                /\\|               |  |
                               / '((               |  |
                              /  / )\              \  |
                             /  y  \y              |Y |
                            /  /    (              |  |
                           L ."     |              |  /
                          | \(                     |  |
                           \_|                     |  |
                           |  \                    { "|
                           | ||                    |  |
                           |x||                    \_,/
                           } ||                    / \'
                           | ||                    |_/
                           | (|                    | }\
                           | ||                    } ||
                           | ||                    | ||
                           | ||                    |\||
                           / ||                    | ||
                           | ||                    ( |!
                           | |/                    ) ||
                         _/   \                    | }|
                     _.-"_ ( )|                 ! ||
                  c_"-_-"_    )                    | ||
                   c,-_-'_--""                     { ||
                   "C(_/"                          \ /|
                                                   (! )
                                                   /| \
                                                  /  |(
                                                 /7||\\
                                                ()U cUu
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
  jgs /       '----'       \
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
  --------(_,-._)))-------------------------------
''')
        if monster1.monster == ("Pig"):
            print(r'''
              ,
              , `.
              |   `.
              `     `.
               \___   \
     ,---._   ,'   -`./
  ,-"      "-/ .__ /* `._
  `.         |  * ,-.  _ `
    `.       ,  , `-' ,'  `
      `-----"| '`----"    |
             \       /    |
              \           "
               `.        /_
                 `._   _/| \
                  (  ".  '  \
                   \   `.`.  .
                   |`    \"  |\
                   | `.   `.,' .
                   |   `.   \  |
                   |    ,`   | |
                   |    `-`-"  ,
                   `          ,
                    `.     _,'
                      `.--" |
                       | || |  .-.
                       | |, `,'   )
                   ___,' \       ,
                  /      /------"
                  \____,"  
''')
        if monster1.monster == ("Monkey"):
            print(r'''
                      __,__
             .--.  .-"     "-.  .--.
            / .. \/  .-. .-.  \/ .. \
           | |  '|  /   Y   \  |'  | |
           | \   \  \ 0 | 0 /  /   / |
            \ '- ,\.-"`` ``"-./, -' /
             `'-' /_   ^ ^   _\ '-'`
             .--'|  \._ _ _./  |'--.
           /`    \   \.-.  /   /    `\
          /       '._/  |-' _.'       \
         /          ;  /--~'   |       \
        /        .'\|.-\--.     \       \
       /   .'-. /.-.;\  |\|'~'-.|\       \
       \       `-./`|_\_/ `     `\'.      \
        '.      ;     ___)        '.`;    /
          '-.,_ ;     ___)          \/   /
           \   ``'------'\       \   `  /
            '.    \       '.      |   ;/_
     jgs  ___>     '.       \_ _ _/   ,  '--.
        .'   '.   .-~~~~~-. /     |--'`~~-.  \
       // / .---'/  .-~~-._/ / / /---..__.'  /
      ((_(_/    /  /      (_(_(_(---.__    .'
                | |     _              `~~`
                | |     \'.
                 \ '....' |
                  '.,___.'
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
                   <`_,'     ,  /\          /
                    `  \/\,-/ `/  \/`\_/V\_/
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
You got a new {chestitems.name}""")
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
            print("""
Your backpack is full. You cannot carry more items.
                  """)
    elif departure == 3:
        right_answer = 3
        print(f"""
                You encountered a {trap.trap_name}""")
        while True:
            player_answer = input("Guess a number between 1 and 3 to have a chance to escape!: ")
            if player_answer == "1" or player_answer == "2" or player_answer == "3":
                break
        if player_answer == right_answer:
            print(f"""
You avoided the {trap.trap_name} and got away safely
                  """)
        elif player_answer != right_answer:
            trap.trigger(player1)


def menu(player1, monster1):
    print("""                         
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
          """)
    pack = []
    while player1.hp > 0:
        camp = input("""
                1.  Explore 
                2.  Stats 
                3.  Backpack 

Please Enter Your Choice: """)
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