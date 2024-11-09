import random
from HGQ_Combat_Methods import combat,player_turn,enemy_turn

print("Welcome to the Monty Python Adventure!")
print("You are about to embark on a quest for the Holy Grail. Beware of dangerous encounters!")

player_name = input("What is your name, brave adventurer?  ")
player_health = 100
player_weapon = "Fauxcalibur"
print(f"Welcome, Sir {player_name} of Pythonia!")

print("A knight steps in front of you and says, 'None shall pass!'")
print("Make a choice:  ")
print("     1. Battle the knight.")
print("     2. Explain the complexities of sparrows and coconuts")
print("     3. You toss a coconut at your foe and then attack!")
choice = input("Input '1' or '2':  ")
enemy_name,enemy_health,enemy_weapon = "Black Knight",100,"Sword"

match choice:
    case '1':
        print("The black knight draws his sword, it's time for battle!")
        combat(player_name,enemy_name,player_health,enemy_health,player_weapon,enemy_weapon,False,False)
    case '2':
        print("The black knight scoffs at your suggestion that coconuts migrate.")
        print("The black knight draws his sword, it's time for battle!")
        combat(player_name,enemy_name,player_health,enemy_health,player_weapon,enemy_weapon,True,False)
    case '3':
        print("You throw a coconut at the black knight.")
        print("His head is ringing!")
        combat(player_name,enemy_name,player_health,enemy_health,player_weapon,enemy_weapon,False,True)
    case _: 
        print("You hesitate.. and the knight charges")
        combat(player_name,enemy_name,player_health,enemy_health,player_weapon,enemy_weapon,True,False)

player_health = 100

print()
print()

while True:
    decision = input("Do you want to cross the Bridge of Death? (yes/no/fight?)")
    if decision.lower() == 'yes':
        print("A troll appears and asks you three questions!")
        break
    elif decision.lower() == 'no':
        print("You wisely turn back.")
        break
    elif decision.lower() == 'fight':
        enemy_name,enemy_weapon,enemy_health = "Troll","Club",120
        print("Troll: 'Wait, what are you doing?!'")
        print(f"You draw {player_weapon}!")
        combat(player_name,enemy_name,player_health,enemy_health,player_weapon,enemy_weapon,False,True)
    else:
        print("please enter 'yes'/'no'/'fight'")
       

print(f"Sorry, {player_name} but the holy grail is in another castle.")
print(f"---------------------------Farewell--------------------------")

