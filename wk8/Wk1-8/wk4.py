# x = 0 # Setup a variable to use for the conditional

# while x <= 10: # Continue looping until x is greater than 10
#     print(x) # Print the current itterations value of x
#     x += 1 # Inrement x by 1 (add 1 to the current value of x)

# print("loop Finished") # This will execute after the loop since it's at a lower indentation level
# # FOR LOOP
# For loops are a bit more complicated than while loops.

# They loop based on iterables, which are things in python that you can iterate over.

# Collections such as lists, and tuples (and even strings) are examples of iterables.

# The terminating condition during for loops is when you hit the end of the iterable (i.e. the last element in a list).

# The basic syntax of a for loop looks like this:

# for variable in iterable:
#     # Code at this indentation executes during the iteration---

# # Code at this indentation does stuff after the loop
# FOR LOOP
# Where variable is an arbitrarily named variable used to hold the current value of the iteration, and iterable is the item to iterate over.

# Let's take the example of a shopping list and say you wanted to loop through the values in the list and print them off one by one, you could use a for loop to do this:

# shopping_list = ["Eggs", "Ham", "Milk"]

# for item in shopping_list: # Iterate through the shopping list
#     print(item) # Print the item at the current iteration
# #This would print:

# # >> Eggs
# # >> Ham
# # >> Milk


# greeting = "Hello-World" # Setting up a string to iterate through

# for character in greeting: # Iterate over the string one letter at a time
#     if "-" in character: # if the current character is a hyphen
#         print("Hyphen detected, ending loop!")
#         break # End the loop
#     else:
#         print(character) # Print the current character

#         x = 0 # Initialize a variable to use in the condition

# x = 0

# while x < 10:
#     x +=1
#     if ((x % 2) == 0): # If the number is even
#         print(x)

#     else: # If the number is odd
#         continue # Go to next iteration

# shopping_lists = [["Eggs", "Milk", "Ham"], 
#                   ["Vinegar", "Mustard", "Ketchup"], 
#                   ["Burgers", "Lettuce", "Mayo"]]

# for current_list in shopping_lists: # Steps through the list of lists
#     for item in current_list: # Steps through each list
#         print(item) # Prints the item in the current shopping list



# while True: # This is an infinite loop
#   number = int(input("Please type a number between 1 and 10: ")) # Take user input

#   if number < 1: # Number is too small
#     print("Number provided is less than 1")

#   elif number > 10: # Number is too large
#     print("Number provided is greater than 10")

#   else: # If the input is in a valid range
#     print("Number is between 1 and 10")
#     break # End the loop


# valid_input = False # Used to mark if input is valid

# while not valid_input: # Loop when valid input is False
#   number = int(input("Please type a number between 1 and 10: ")) # Take user input

#   if number < 1: # Number is too small
#     print("Number provided is less than 1")

#   elif number > 10: # Number is too large
#     print("Number provided is greater than 10")

#   else: # If the input is in a valid range
#     valid_input = True # End the loop


# for number in range(5,11):
#     print(number)



# for number in range(11):
#     print(number)


# # Gameloop
# while turns < 100:             # Game goes until 100 score
#     player_move(player_one) # Player one's move
#     player_move(player_two) # Player two's move
#     turns += 1

# if player_one.score > player_two.score:
#     print("Player One Wins!")
# elif player_one.score < player_two.score:
#     print("Player Two Wins!")


def greet(name="John doe", greeting="Hello there: "):
    """Greets a person with the greeting and their name

    Parameters
    ----------
    name: (str)
        The name to greet by.
    greeting: (str)
        The greeting to greet by.
    """
    print(name, greeting)

greet()
    