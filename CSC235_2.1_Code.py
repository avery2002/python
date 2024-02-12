# Avery Willets
# 1/18/2024

# For Assignment 2 we need user inpu/output and 2 variables

# Welcome message for user
print("Welcome to my tutorial about the print function in python")

#Ask the user for their name using input function
userName = input("Please enter your name: ")

# print out the name of the user
print("I hope you anjoy the tutorial,", userName)


# add empty print statement to break up space
print("------------------")


# explain some different ways to print in python
print("One way to print out text in Python is like so: ")
print("print('The weather in Phoenix is great', 75)")
print("You can separate different things to print with a comma. A space will be added with each instance of the comma.")
print("print('The weather in Phoenix is great', 75', 'is today's high temp')")


# add empty print statement to break up space
print("------------------")


# show another way to use the print statement
print("Another way to print out text in Python is like so: ")
print("print('The weather in Phoenix is great' + 75)")


# add empty print statement to break up space
print("------------------")


# Let's ask the user how they would rate my tutorial
ratingStr = input("Please let me know how you rate my tutorial so far (1-10, 10 being highest): ")
ratingInt = 0

# check to see if the user entered a number
if ratingStr.isnumeric():
    # This code is indented, so it belongs to the if statement
    # we can cast the user statement to an int because we know the user entered a number
    ratingInt = int(ratingStr)
    print("Nice job following directions! :)")
else:
    # the user did not enter a number for some unknown reason
    print("Please pay better attention next time :(")
    

# add empty print statement to break up space
print("------------------")


# let's talk about f string formatting
# make sure to include the f at the start of the print statement, otherwise you will get a funky result
print(f"Here is the information you have entered so far: Your name: {userName} and your rating of my awesome tutorial: {ratingInt}")

# add empty print statement to break up space
print("------------------")


# another way to print is using the f string (formatting)
print("A third way to use the print statement is like so: ")
print("(This is an easy way to print out the values of your variables)")
print("print(f'Here is the information you have entered so far: Your name: {userName} and your rating of my awesome tutorial: {ratingInt}')")


# add empty print statement to break up space
print("------------------")


# tell the user to have a nice day
print("Have a nice day! :)")