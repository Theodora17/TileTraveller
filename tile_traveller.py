# Functions for each movement - North, South, East and West
# Function that updates the position
# Function that checks if the movement wanted is possible

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
