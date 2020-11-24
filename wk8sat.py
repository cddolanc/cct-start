# print(type(1))
# print(type([]))
# print(type(()))
# print(type({}))

# Create a new object type called Sample
# class Sample:
#     pass

# # Instance of Sample
# x = Sample()

# print(type(x))


# class Dog:

#     species = 'mammal'    

#     def __init__(self,breed):
#         self.breed = breed


# sam = Dog(breed='Lab')
# frank = Dog(breed='Huskie')

# print(sam.breed)
# print(sam.species)


# class Circle:
#     pi = 3.14

#     # Circle gets instantiated with a radius (default is 1)
#     def __init__(self, radius=1):
#         self.radius = radius 
#         self.area = radius * radius * Circle.pi

#     # Method for resetting Radius
#     def setRadius(self, new_radius):
#         self.radius = new_radius
#         self.area = new_radius * new_radius * self.pi

#     # Method for getting Circumference
#     def getCircumference(self):
#         return self.radius * self.pi * 2

# c = Circle()

# c.setRadius(2)

# print('Radius is: ',c.radius)
# print('Area is: ',c.area)
# print('Circumference is: ',c.getCircumference())


# class Animal:
#     def __init__(self):
#         print("Animal created")
#     def whoAmI(self):
#         print("Animal")
#     def eat(self):
#         print("Eating")

# class Dog(Animal):
#     def __init__(self):
#         Animal.__init__(self)
#         print("Dog created")
#     def whoAmI(self):
#         print("Dog")
#     def bark(self):
#         print("Woof!")

# d = Dog()
# d.whoAmI()
# d.eat()
# d.bark()

# c = Animal()
# c.whoAmI()
# c.eat()


# class Dog:
#     def __init__(self, name):
#         self.name = name
#     def speak(self):
#         return self.name+' says Woof!'

# class Cat:
#     def __init__(self, name):
#         self.name = name
#     def speak(self):
#         return self.name+' says Meow!' 

# niko = Dog('Niko')
# felix = Cat('Felix')

# # for pet in [niko,felix]:
# #     print(pet.speak())

# def pet_speak(pet):
#     print(pet.speak())

# pet_speak(niko)
# pet_speak(felix)



# class Animal:
#     def __init__(self, name):    # Constructor of the class
#         self.name = name
#     def speak(self):              # Abstract method, defined by convention only
#         raise NotImplementedError("Subclass must implement abstract method")

# class Dog(Animal):  
#     def speak(self):
#         return self.name+' says Woof!'

# class Cat(Animal):
#     def speak(self):
#         return self.name+' says Meow!'

# fido = Dog('Fido')
# isis = Cat('Isis')

# print(fido.speak())
# print(isis.speak())

# print(len('book'))


# class Book:
#     def __init__(self, title, author, pages):
#         print("A book is created")
#         self.title = title
#         self.author = author
#         self.pages = pages
#     def __str__(self):
#         return "Title: %s, author: %s, pages: %s" %(self.title, self.author, self.pages)
#     def __len__(self):
#         return self.pages
#     def __del__(self):
#         print("A book is destroyed")
# def __eq__(self, other):
#         return self.title == other.title

# book = Book("Python Rocks!", "Jose Portilla", 159)





# #Special Methods
# print(book)
# print(len(book))
# del book


# def square(num):
#     return num**2

# my_nums = [1,2,3,4,5]

# # To get the results, either iterate through map() 
# # or just cast to a list
# for item in map(square,my_nums):
#     print(item)

# list(map(square,my_nums))


# def splicer(mystring):
#     if len(mystring) % 2 == 0:
#         return 'even'
#     else:
#         return mystring[0]
# mynames = ['John','Cindy','Sarah','Kelly','Mike']
# print(list(map(splicer,mynames)))


# def check_even(num):
#     return num % 2 == 0 

# nums = [0,1,2,3,4,5,6,7,8,9,10]

# print(nums)
# print(list(filter(check_even,nums)))

# for n in filter(check_even,nums):
#     print(n)



# def square(num):
#     result = num**2
#     return result

# print(square(2))



# def square(num): return num**2

# print(square(2))



# square = lambda num: num ** 2

# print(square(2))


# nums = [0,1,2,3,4,5,6,7,8,9,10]

# my_nums = [1,2,3,4,5]

# print(list(map(lambda num: num ** 2, my_nums)))
# print(list(filter(lambda n: n % 2 == 0,nums)))

# lambda s: s[0]

# lambda s: s[::-1]

# lambda x,y : x + y


# x = 25

# def printer():
#     x = 50
#     return x

# print(x)
# print(printer())


# # x is local here:
# f = lambda x:x**2


# name = 'This is a global name'

# def greet():
#     # Enclosing function
#     name = 'Sammy'
#     def hello():
#         name = 'John'
#         print('Hello '+name)
#     hello()

# greet()


# x = 50

# def func(x):
#     print('x is', x)
#     x = 2
#     print('Changed local x to', x)

# func(x)
# print('x is still', x)


# x = 50

# def func():
#     global x
#     print('This function is now using the global x!')
#     print('Because of global x is: ', x)
#     x = 2
#     print('Ran func(), changed global x to', x)

# print('Before calling func(), x is: ', x)
# func()
# print('Value of x (outside of func()) is: ', x)

# def myfunc(a,b,c=0,d=0):
#     return sum((a,b))*.05

# myfunc(40,60,80)

# def myfunc(a=0,b=0,c=0,d=0,e=0):
#     return sum((a,b,c,d,e))*.05

# myfunc(40,60,20)


# def myfunc(*args):
#     return sum(args)*.05

# print(myfunc(40,60,80,10))


# def myfunc(*spam):
#     return sum(spam)*.05

# print(myfunc(40,60,80,10))

# def myfunc(**kwargs):
#     if 'fruit' in kwargs:
#         print(f"My favorite fruit is {kwargs['fruit']}")  # review String Formatting and f-strings if this syntax is unfamiliar
#     else:
#         print("I don't like fruit")

# myfunc(fruit='pineapple')

# myfunc()


def myfunc(*args, **kwargs):
    if 'fruit' and 'juice' in kwargs:
        print(f"I like {' and '.join(args)} and my favorite fruit is {kwargs['fruit']}")
        print(f"May I have some {kwargs['juice']} juice?")
    else:
        pass

myfunc('eggs','spam',fruit='cherries',juice='orange')