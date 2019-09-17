# Functions for each movement - North, South, East and West
# Function that updates the position
# Function that checks if the movement wanted is possible

def north(first,second) :
    if second < 3 :
        second += 1 
    
    return first, second

def south(first,second) :
    if second > 1 :
        second -= 1 

    return first, second

def west(first,second) :
    if first > 1 :
        first -= 1 
    
    return first, second

def east(first,second) :
    if first < 3 :
        first += 1 

    return first, second

def update_position(choice, first, second):
    if choice == "n":
        second += 1
    elif choice == "s":
        second -= 1
    elif choice == "e":
        first += 1
    elif choice == "w":
        first -= 1

    return first, second

def read_choice():
    choice = input("Direction: ")

    return choice

def get_valid_direction(first, second):
    if second == 1:
        print("You can travel: (N)orth")
    elif first == 1 and second == 2:
        print("You can travel: (N)orth or (E)ast or (S)outh")
    elif first == 1 and second == 3:
        print("You can travel: (E)ast or (S)outh")
    elif first == 2 and second == 3:
        print("You can travel: (W)est or (E)ast")
    elif first == 2 and second == 2:
        print("You can travel: (W)est or (S)outh")
    elif first == 3 and second == 3:
        print("You can travel: (W)est or (S)outh")
    elif first == 3 and second == 2:
        print("You can travel: (N)orth or (S)outh")
    elif first == 3 and second == 1:
        print("Victory!")
    else:
        print("Not a valid direction!")

    return first, second