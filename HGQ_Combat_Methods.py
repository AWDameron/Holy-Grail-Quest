import random

def player_turn(player_name,player_weapon_name):
    print(f"{player_name} strikes out with their {player_weapon_name}")
    enemy_attack = random.randint(4,10)
    match enemy_attack:
        case 1:
            print("The attack misses!")
            player_damage = 0
        case 10:
            print("The attack is !CRITICAL!")
            player_damage = (random.randint(4,10) + random.randint(4,10))
        case _:
            print("The attack hits!")
            player_damage = random.randint(4,10)
    
    return player_damage


def enemy_turn(enemy_name,enemy_weapon_name):
    print(f"{enemy_name} strikes out with their {enemy_weapon_name}")
    enemy_attack = random.randint(4,10)
    match enemy_attack:
        case 1:
            print("The attack misses!")
            enemy_damage = 0
        case 10:
            print("The attack is !CRITICAL!")
            enemy_damage = (random.randint(4,10) + random.randint(4,10))
        case _:
            print("The attack hits!")
            enemy_damage = random.randint(4,10)
    
    return enemy_damage

def combat(player_name,enemy_name,player_health,enemy_health,player_weapon_name,enemy_weapon_name,player_penalty,enemy_penalty):
    turn = 1
    #Penalty System
    if player_penalty:
        player_health -= random.randint(1,10)
        print(f"The {enemy_name} gets a suprise attack!")
        print(f"{player_name:<15}: {player_health:>3} | {enemy_name:<15}: {enemy_health:>3}")
        print("---------------------------------------------------------------------")

    if enemy_penalty:
        enemy_health -= random.randint(1,10)
        print(f"{player_name} gets a suprise attack!")
        print(f"{player_name:<15}: {player_health:>3} | {enemy_name:<15}: {enemy_health:>3}")
        print("---------------------------------------------------------------------")

    #Combat Loop
    while player_health > 0 and enemy_health > 0:
        print(f"--- Turn: {turn} ---")
        player_damage = player_turn(player_name, player_weapon_name)
        player_health -= player_damage
        enemy_damage = enemy_turn(enemy_name,enemy_weapon_name)
        enemy_health -= enemy_damage
        turn += 1
        print(f"{player_name:<15}: {player_health:>3} | {enemy_name:<15}: {enemy_health:>3}")
        print("---------------------------------------------------------------------")
        input()
    
    #Victory Message
    if enemy_health <= 0:
        print(f"{player_name} has defeated {enemy_name}!")
        print(f"{player_name} has achieved victory for Pythonia!")
    
    
    #Defeat Message
    if player_health <= 0:
        print(f"{enemy_name} has put an end to the quest for the Holy Grail")
        print(f"{player_name} has fallen!")
        print("Please Try Again!")
        exit()
                


