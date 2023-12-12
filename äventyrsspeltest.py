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
            print("Attacking...")
            time.sleep(1)
            monster1.monster_health -= player1.strength
            print_slow(f"""
--{monster1.monster}--
{monster1.monster} Strength: {int(monster1.monster_strength)}
{monster1.monster} Health:   {int(monster1.monster_health)}
""", 0.04)
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