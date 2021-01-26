# def func():
#     return 1

# print(func())


# s = 'Global Variable'

# def check_for_locals():
#     print(locals())

# print(globals())

# print(globals().keys())




# def hello(name='Jose'):
#     return 'Hello '+name

# # print(hello())

# greet = hello

# # greet

# # print(greet())

# del hello

# # print(hello())

# print(greet())


# def hello(name='Jose'):
#     print('The hello() function has been executed')

#     def greet():
#         return '\t This is inside the greet() function'

#     def welcome():
#         return "\t This is inside the welcome() function"

#     print(greet())
#     print(welcome())
#     print("Now we are back inside the hello() function")

# hello()

# welcome()

# def hello(name='Jose'):

#     def greet():
#         return '\t This is inside the greet() function'

#     def welcome():
#         return "\t This is inside the welcome() function"

#     if name == 'Jose':
#         return greet
#     else:
#         return welcome

# x = hello()

# print(x())





# def hello(name='Jose'):

#     def greet():
#         return '\t This is inside the greet() function'

#     def welcome():
#         return "\t This is inside the welcome() function"

#     if name == 'Jose':
#         return greet
#     else:
#         return welcome

# x = hello

# print(x(name= 'Sam')())




# def hello():
#     return 'Hi Jose!'

# def other(func):
#     print('Other code would go here')
#     print(func())

# other(hello)


def new_decorator(func):

    def wrap_func():
        print("Code would be here, before executing the func")
        func()
        print("Code here will execute after the func()")
    return wrap_func

# def func_needs_decorator():
#     print("This function is in need of a Decorator")

# func_needs_decorator()

# Reassign func_needs_decorator
# func_needs_decorator = new_decorator(func_needs_decorator)

# func_needs_decorator()


# @new_decorator
# def func_needs_decorator():
#     print("This function is in need of a Decorator")

# func_needs_decorator()




# # Generator function for the cube of numbers (power of 3)
# def gencubes(n):
#     for num in range(n):
#         yield num**3

# for x in gencubes(10):
#     print(x)





# def genfibon(n):
#     """
#     Generate a fibonnaci sequence up to n
#     """
#     a = 0
#     b = 1
#     for i in range(n):
#         yield a
#         a,b = b,a+b

# for num in genfibon(100):
#     print(num)




# def simple_gen():
#     for x in range(3):
#         yield x

# # Assign simple_gen 
# g = simple_gen()
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))




# s = 'hello'

# #Iterate over string
# for let in s:
#     print(let)

# s_iter = iter(s)

# next(s_iter)

# next(s_iter)


# def gensquares(N):
#     for num in range(N):
#          yield num**2

# for x in gensquares(10):
#     print(x)


# import random

# random.randint(1,10)

# def rand_num(low,high,n):
#     for x in range(n):
#          yield random.randint(low, high)


# for num in rand_num(1,10,12):
#     print(num)


s ='hello'

s= iter(s)

print(next(s))
print(next(s))
print(next(s))
print(next(s))
print(next(s))
