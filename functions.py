# Avery Willets
# 1/12/24

# import the Random library from python
import random


# 4 basics of programming are:


# variables
userName = "Avery"


# functions
# when you create a function in python use the word def
# the function name should ususally be some sort of action
# make sure to include the () and the :
# if you want to have the funciton use variable(s) from other parts of the code, put the variables between the ()
def calcScore(hits, misses):
    # all this function needs to do is some arbitrary math
    # that arbitrary resuslt is passed back to the code that called the function
    return (hits * 10) - (misses * 5)


# Let's create a function to randomly high five
def highFiveFriend():
    # we want to randomly high five the enemy
    return random.choice([True, False])


# let's code a high five game
def playGame():
    # set up our gameplay variables
    hits = 0 # Hit tracker, default to 0
    misses = 0 # miss tracker, default to 0
    totalRounds = 10 # How many rounds you want the game to last
    
    # Welcome message
    print("Welcome to me game! Have fun high-fiving your friend.")
    
    # set up a for loop to run the rounds
    for _ in range(totalRounds):
        print("Press Enter to try to high five your friend...")
        input()
        
        # Call the high five generator, if high five was successful, print such
        if highFiveFriend():
            print("The friend was high fived!")
            hits += 1
        else:
            print("The friend was not high fived!")
            misses += 1
    
    # calculate score
    score = calcScore(hits, misses)
    # tell the user the game is over and their score
    print("Game over!")
    print(f"You scored {score} points!")
    print("Thanks for playing!")

# loops
# in python we have 2 types of loops
# for loop - generally use a for loop when you know (or python knows) how many times you want the loop to run
# while loop - generally use a while loop when you don't know how many times the loop will run
 
# easy way to set up a while loop, this loop will run FOREVER
# remember that True and False have to be capitalized in Python       
while True:
    # Call the play game function
    playGame()
    
    # Let's ask the user if they would like to play again
    # make sure to offer guidance for how the user should answer
    response = input("Do you want to play again? (yes/no)")
    
    # Let's check the user's answer
    # if they respond with anything other than 'yes', they leave the program
    if response != "yes":
        # say goodbye
        print("Thanks for playing!")
        # this break statement will get us out of our infinite while loop
        break

# decision logic (if/else statements)