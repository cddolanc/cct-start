"""
    =========== Exercise 1 =============

    I have provided some starter code below
    that creates a result variable, and a number_1
    variable. Your goal is to make number_1 equal 11
    after the operations that have been done to it.
"""

# result = 0
# number_1 = 5
# number_1 += 52

# # Do more operations on number 1 until it equals eleven
# print(number_1)
# number_1 = (number_1 //3)
# number_1 -= 8
# print(number_1)
# result = number_1
# print(result == 11)


"""
    =========== Exercise 2 =============

    Take input from the command line, and convert it to
    an int. Now pick a range (i.e. 0-10), and create a set
    of conditional statements that prints the string
    representation of the number input by the user.

    For example if someone put in 8, then it would print 'eight'.
    
    Hint: Use if, elif and else statements.
"""

# number_2 = int(input("Please enter a number between 1 and 10 : "))
# print(number_2)
# if (number_2 < 0) or (number_2 >10):
#     print('Out of range!')
# elif number_2 == 1:
#     print('One')
# elif number_2 == 2:
#     print('Two')
# elif number_2 ==3:
#     print('Three')
# elif number_2 ==4:
#     print('Four')
# elif number_2 ==5:
#     print('Five')
# elif number_2 ==6:
#     print('Six')
# elif number_2 ==7:
#     print('Seven')
# elif number_2 ==8:
#     print('Eight')
# elif number_2 ==9:
#     print('Three')
# elif number_2 ==10:
#     print('Ten')


"""
    =========== Exercise 3 =============

    Before running the code below try to
    figure out which print statement will
    execute and why. Then uncomment the code
    and check if you were right.
"""

number = 0 # less than 10
number += 15 # between 20 and 30
number //= 2 # between 10 and 20
number *= 6 # 7*6 ¯\_(ツ)_/¯
number -= 4 # between 30 and 40
print(number)
if number < 10:
  print("Less than 10")

elif 10 <= number <= 20:
   print("Between 10 and 20")

elif 20 <= number <= 30:
   print("Between 20 and 30")

elif 30 <= number <= 40:
        print("Between 30 and 40")

else:
    print("¯\_(ツ)_/¯")