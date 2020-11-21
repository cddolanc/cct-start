# # name = "John"
# # print("Hello,",name)


# # name = "John Doe"

# # greeting = f"Welcome, {name}!"

# # print(greeting) # Prints: Welcome John Doe!

# # name = "John Doe"

# # greeting = f"Welcome, {name}!"

# # name = "Kieran Wood"

# # print(greeting) # Prints: Welcome John Doe!

# # greeting = f"Welcome, {name}!" # Since it's recreated it picks up the new value of name

# # print(greeting) # Prints: Welcome Kieran Wood!

# # import datetime

# # sputnik_launch = datetime.date(1959, 10, 4)


# # falcon_9_first_launch = datetime.date(2010, 6, 4)

# # print(falcon_9_first_launch > sputnik_launch) # prints: True

# # print(sputnik_launch)



# # appolo_11_launch = datetime.date(1959, 9, 13)


# # appolo_11_launch.year # prints: 1959

# # appolo_11_launch.month # Prints: 9

# # appolo_11_launch.day # Prints: 13

# # import datetime

# # current_datetime = datetime.date.today() # Returns datetime object of todays date

# # print(current_datetime)

# # class Animal:
# #   def __init__(self, species_name, regions, common_name):
# #     """A class to represent a generic animal

# #     Attributes
# #     ----------
# #     species_name : (str) 
# #         The technical species name of the animal
# #     regions : (list[str]) 
# #         A list of regions the animal is endemic to
# #     common_name : (str) 
# #         The colloquial name of the animal
# #     """
# #     self.species_name = species_name
# #     self.regions = regions
# #     self.common_name = common_name

# #     leopard_gecko = Animal("Eublepharis macularius",
# #     ["Afghanistan","Pakistan","India", "Iran"],
# #     "Common Leopard Gecko")

# #     print(leopard_gecko.common_name)

# class Animal:
#   def __init__(self, species_name, regions, common_name):
#     """A class to represent a generic animal

#     Attributes
#     ----------
#     species_name : (str) 
#         The technical species name of the animal
#     regions : (list[str]) 
#         A list of regions the animal is endemic to
#     common_name : (str) 
#         The colloquial name of the animal
#     """
#     self.species_name = species_name
#     self.regions = regions
#     self.common_name = common_name
#   def print_info(self):
#     """Prints information about animal instance"""
#     print(f"\nCommon Name: {self.common_name}\nSpecies: {self.species_name}\nRegions: {self.regions}")




# """Prints (not returns)
# Common Name: Common Leopard Gecko
# Species: Eublepharis macularius
# Regions: ['Afghanistan','Pakistan','India', 'Iran']
# """
# leopard_gecko.print_info()
# CLASSES
# There was a lot going on in the last example so lets break down what happened.
# First we start by defining our class (usually called the class definition) with:
# class Classname: # Notice for classes the convention is to start them with a capital
#   def __init__(self): # This method will be explained later on
#     pass
# Following our class definition right away we define a __init__ method.
# # The __init__ method is explained in further detail below.
# # But first let's take a look at that funny self that we've been putting in front of our variables.



# class Animal:
#   counter = 0 # Initialize counter to 0
#   # This ^^ is a class variable since it is outside of __init__ and has no self. in front
#   def __init__(self, species_name, regions, common_name):
#     """A class to represent a generic animal

#    Attributes
#     ----------
#     species_name : (str) 
#         The technical species name of the animal
#     regions : (list[str]) 
#         A list of regions the animal is endemic to
#     common_name : (str) 
#         The colloquial name of the animal
#     """
#     self.species_name = species_name
#     self.regions = regions
#     self.common_name = common_name
#     Animal.counter += 1 # Accessing and incrementing the class counter by 1 on each instantiation of an Animal

#   def print_info(self):
#     """Prints information about animal instance"""
#     print(f"\nCommon Name: {self.common_name}\nSpecies: {self.species_name}\nRegions: {self.regions}")
# # CLASSES
# # SELF; INSTANCE VS CLASS ATTRIBUTES
# # Now there is a counter variable that can be used to find out how many animals have been instantiated
# # print(Animal.counter) # Prints 0; since no Animal's have been instantiated
# # leopard_gecko = Animal("Eublepharis macularius",
# #     ["Afghanistan","Pakistan","India", "Iran"],
# #     "Common Leopard Gecko")

# print(Animal.counter) # Prints 1; since the Leopard Gecko has been instantiated

# arctic_fox = Animal("Vulpes lagopus",
#     ["The Arctic"],
#     "Arctic fox")

# print(Animal.counter) # Prints 2; since the Leopard Gecko, and Arctic fox have been instantiated

# # Both below calls print 2; Class variables are also accessible in any instance
# print(arctic_fox.counter)
# print(leopard_gecko.counter)
# # As you can see because the variable belongs to the class and not the instance, it is available to both the class as a variable, or any instances of the Animal class.
# # CLASSES
# # CLASS METHODS
# # Methods are functions that are accessible through class instances, for example let's say you want to create a function to print all of the attributes of a class you could define the function in the class and then use the self operator to print the information.
# # We have already seen this in fact in the above examples with our Animal class, the print_info() method used earlier is a class method.


class CookieBaker:
  def __init__(self, number_of_cookies):
    """ Example class that is used to show off the __init__ method.
    The __init__ method calls prints 'Cookie Baked' as many times as there are number_of_cookies.

    Attributes
    ----------
    number_of_cookies(int): How many cookies to bake
    """
    print(f"__init__ method called, creating {number_of_cookies} cookie(s):")
    self.number_of_cookies = number_of_cookies
    for cookie in range(number_of_cookies):
      print("Cookie Baked!")
  
def bake_cookie(self):
    """Print's 'Cookie Baked!'."""
    print("Cookie Baked!")


# CookieBaker(5)

# print(Animal.counter) # Prints 0; since no Animal's have been instantiated
# leopard_gecko = Animal("Eublepharis macularius",
#     ["Afghanistan","Pakistan","India", "Iran"],
#     "Common Leopard Gecko")

# print(Animal.counter) # Prints 1; since the Leopard Gecko has been instantiated

# Animal.counter = 35 # Overriding the variable from the class

# print(Animal.counter) # Prints 35; since the attribute has been overridden
# print(leopard_gecko.counter) # Prints 35; since the attribute has been overridden


# print(Animal.counter) # Prints 0; since no Animal's have been instantiated
# leopard_gecko = Animal("Eublepharis macularius",
#     ["Afghanistan","Pakistan","India", "Iran"],
#     "Common Leopard Gecko")

# print(Animal.counter) # Prints 1; since the Leopard Gecko has been instantiated

# Animal.counter = 35 # Overriding the variable from the class

# print(Animal.counter) # Prints 35; since the attribute has been overridden

# leopard_gecko.counter = 26 # creating an instance variable from the class attribute

# print(Animal.counter) # Prints 35; since the class attribute WONT be modified by changing the gecko instance counter
# print(leopard_gecko.counter) # Prints 26; since the instance attribute has been created

import datetime
from dataclasses import dataclass
@dataclass
class user:
  def __init__(self, name, age, sign_up_date, birthday, premium_member):
    """A class to represent a generic animal

    Attributes
    ----------
    name(str): The technical species name of the animal
    age(str): A list of regions the animal is endemic to
    sign_up_date(datetime.datetime): A datetime object of the day the user signed up
    birthday(datetime.datetime): A datetime object of the users birthday
    premium_member(bool): Whether the user is on premium or free subscription
    """
    name:str
    age:str
    sign_up_date:datetime.datetime
    birthday:datetime.datetime
    premium_member:bool


user1 = ('john',52,datetime.date(2020, 1, 13),datetime.date(1961, 4, 12),True)
print(user1.name)