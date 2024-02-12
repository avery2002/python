# this is going to be a text-based sim for the week 5 assignment. The user will get different options based on their choices

#requirements: 3 blocks of if/else chunks, ideally there should be nesting 3 levels deep

# include lots of comments and a nice user experience

# welcome the user to our program, present first choice
print("Welcome to my text-based sim. Please play as many times as you wish!")
print("\nWhile on an adventure, you find yourself at a crossroads. Which path will you take?")
print("1. Follow the path through the forest.")
print("2. Take an old bridge over a river.")

# Need to gather input from the suer for what path they take
# use an input statement here, assign the user input to a variable
choice1 = int(input("Enter your choice (1 or 2): "))


# THIS IS MY FIRST IF BLOCK 1/3
if choice1 == 1:
    # If the user chooses option 1, then go down some path
    # Print out the next scenario
    print("\n\nYou decide to enter the dense forest. Within the forest, you begin to hear a strange noise. Which path will you take?")
    print("1. Investigate the strange noise.")
    print("2. Ignore the noise and walk the other way.")

    # Need to gather input from the suer for what path they take
    # use an input statement here, assign the user input to a variable
    choice2 = int(input("Enter your choice (1 or 2): "))
        
        
    # THIS IS MY SECOND IF BLOCK 2/3
    if choice2 == 1:
        # If the user chooses option 1, then go down some path
        print("\n\nFollowing the noise, you enter a clearing. The noise is louder and sounds to be in front of you. What will you do?")
        print("1. Keep walking towards the noise. You have to know what it is!")
        print("2. Ignore the noise and walk the other way. You've done enough investigating.")
        
        # Need to gather input from the suer for what path they take
        # use an input statement here, assign the user input to a variable
        choice3 = int(input("Enter your choice (1 or 2): "))
           
        # THIS IS MY THIRD IF BLOCK 2/3
        if choice3 == 1:
            # If the user has picked choice 1 three times, they win!
            print("\n\nYou keep walking towards the noise and discover some people digging up a treasure chest. Intimidated by you. they give you half of the treasure. Congratulations! You win!")  
        elif choice3 == 2:
            # the user loses
            print("\n\nYou ran the other way, and the noise seems to follow right behind you. You eventually reach a cliff with no way forward. What happens next is far too tragic of a tale to tell. You lose!")
        else:
            print("Please input either 1 or 2 next time :). Let's play again to go further!")


    elif choice2 == 2:
        print("\n\nYou walk away from the noise and find a river crossing. You see a boat waiting in the distance. What will you do?")
        print("1. Walk towards the boat and get on it. The noise was scary, but this is exciting!")
        print("2. Ignore the boat and keep walking. You've decided today is the day you mind your business.")
        
        # Need to gather input from the suer for what path they take
        # use an input statement here, assign the user input to a variable
        choice3 = int(input("Enter your choice (1 or 2): "))
        
        # If the user chooses option 1
        if choice3 == 1:
            # The user neither wins nor loses
            print("\n\nYou get on the boat and discover it is filled with a pirate crew. Perhaps fearing for your life, you decide to join them! Welcome to your new life!")
        #If the user chooses option 2
        elif choice3 == 2:
            # The user wins
            print("\n\nWhile walking on the riverbank, you discover a briefcase full of gold. Congratulations! You win!")
        else:
            print("\n\nPlease input either 1 or 2 next time :). Let's play again to go further!")
            
            
        
        
    # If the user chooses option 2, go down a diferent path
    # This could be another set of nested if/else statements or could be a dead end
elif choice1 == 2:
    print("\n\nAs you get closer, you see the bridge is broken. You can't cross it. Play again and choose another option to go further :)")
# create a catch all else statement for anythin not 1 or 2
else:
    print("\n\nPlease input either 1 or 2 next time :). Let's play again to go further!")

# say goodbye to the user
    # TODO set up a loop so that the program will automatically run again
print("\nThank you for playing! Please play again by running the Python code again.")