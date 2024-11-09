import random
from HGQ_Combat_Methods import combat,player_turn,enemy_turn

print("Welcome to Holy Grail Quest 2024!")
print("You are about to embark on a quest for the Holy Grail. Beware of dangerous encounters!")

player_name = input("What is your name, brave adventurer?  ")
player_health = 100
player_weapon = "Fauxcalibur"
print(f"Welcome, Sir {player_name} of Pythonia!")

print()
print()

print("A Black Knight steps in front of you and says, 'None shall pass!'")
print("Make a choice:  ")
print("     1. Battle the knight.")
print("     2. Explain the complexities of sparrows and coconuts")
print("     3. You toss your loyal steed, Chauncy, at your foe and then attack!")
choice = input("Input '1','2','3':  ")
enemy_name,enemy_health,enemy_weapon = "Black Knight",100,"Sword"

match choice:
    case '1':
        print("The Black Knight draws his sword, it's time for battle!")
        combat(player_name,enemy_name,player_health,enemy_health,player_weapon,enemy_weapon,False,False)
    case '2':
        print("The Black Knight scoffs at your suggestion that coconuts migrate.")
        print("The Black Knight draws his sword, it's time for battle!")
        combat(player_name,enemy_name,player_health,enemy_health,player_weapon,enemy_weapon,True,False)
    case '3':
        print("Chauncy hits the Black Knight with a frying pan!")
        print("His head is ringing!")
        combat(player_name,enemy_name,player_health,enemy_health,player_weapon,enemy_weapon,False,True)
    case _: 
        print("You hesitate.. and the knight charges")
        combat(player_name,enemy_name,player_health,enemy_health,player_weapon,enemy_weapon,True,False)

player_health = 100

print()
print()

while True:
    print("A troll stops you, 'I must ask you a riddle three'")
    decision = input("Do you want to cross the Bridge of Death? (yes/no/fight?)")
    if decision.lower() == 'yes':
        print("The troll raises his finger to ask you a question and you walk on by!")
        print("'Wow, more like Sir Butt'")
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

