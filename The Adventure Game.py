# Task 1 Code correction. Buggy Code 

place = input("Choose a place: forest or cave? ")

if place == "forest":
    action = input("climb a tree or cross a river?")
    if action == "climb a tree":
        print("You found a bird's nest!")
    elif action == "cross a river":
        print("You found a boat!")
elif place == "cave":
    print("You found a hidden treasure!")

# Task 2 Based on your corrected code from Task 1, expand the game
#  If the user chooses "cave", ask them if they want to "light a torch" or 
# "proceed in the dark", and provide outcomes for each decision.

    action = input("light a torch or proceed in the dark? ")
    if action == "light a torch":
        print("Light may wake the trolls, be careful!")
    elif action == "proceed in the dark":
        print("Great! follow the moon stone path.")

# Task 3 Default Path If invalid choice is made.         
else:
    pass 