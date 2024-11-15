# Python contains many libraries which gives us access to useful functions and additional features so that we don't have to create them.
import random  

# A variable is a reference to a certain value that we assign to that variable.

# This is a function which is a set of code that only runs when it is called.
# Indentation matters in python, so everthing inside the function has to be tabbed. 
def get_choices():
    """ 
    Creating a variable that contains a string (a collection of letters).
    Using the = sign means we are assigning a value. AKA an ASSIGNMENT OPERATOR

    Lists - used to store multiple items in a single variables

    Dictionaries - used to store data in key - value pairs
    The value in a dictionary can be anything and any variable, while the key has to be a non-mutable unique (no duplicates) value. 

    The input() function is used to prompt the user for input and that input is then stored in a variable to use later. 
    """

    # Variable
    player_choice = input("Enter a choice (rock, paper, scissors): ")

    # List
    options = ["rock", "paper", "scissors"]

    # Using the random library to store a random element inside the list in a variable.  
    computer_choice = random.choice(options)  # The .choice outputs a random element from this list.

    # Dictionary
    choices = {"player" : player_choice, "computer": computer_choice}

    return choices  # This is a return statement which basically stores a value and returns it when the function is called. 

# Function arguments - Functions receive data when called, and the data are called arguments.
def check_win(player, computer):  # We specify the arguments inside the parantheses. 
    """
    The parameters of this function are 2 variables, player and computer. When calling the function, we assign
    new pieces of information to the variable, which we can use inside the function. 

    If statements - allows a program to do different things based on certain conditions.
    Will first check a condition and if the condition is true, then all the lines of code under the if statement will execute. 
    <= >= != == < > are all signs used inside of an if statement. 
    
    elif and else statements are used to check multiple conditions in an if statement. Can also use nested if statements.  

    String concatenation is just combining strings with other values.

    """
    # Using f-string to string concatenate.
    print(f"You chose {player}, computer chose {computer}")

    if player == computer:
        return "It's a tie!"
    elif player == "rock":
        if computer == "scissors":
            return "Rock smashes scissors! You win!"
        else:
            return "Paper covers rock! You lose."
    elif player == "paper":
        if computer == "scissors":
            return "Paper covers rock! You win!"
        else:
            return "Scissors cuts paper! You lose."
    elif player == "scissors":
        if computer == "rock":
            return "Rock smashes scissors! You lose."
        else:
            return "Scissors cuts paper! You win!"
    
choices = get_choices()

# Accessing Dictionary values - index by key
p_choice = choices["player"]
c_choice = choices["computer"]

result = check_win(p_choice, c_choice)
print(result)




