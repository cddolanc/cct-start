# class Line:
#     def __init__(self,coor1,coor2):
#         self.coor1 = coor1
#         self.coor2 = coor2
#     def distance(self):
#         x1,y1 = self.coor1
#         x2,y2 = self.coor2
#         return ((x2-x1)**2 + (y2-y1)**0.5)
#     def slope(self):
#         x1,y1 = self.coor1
#         z2,y2 = self.coor2
#         return (((y2-y1)/(x2-x1))


# # # EXAMPLE OUTPUT
# coordinate1 = (3,2)
# coordinate2 = (8,10)

# li = Line(coordinate1,coordinate2)

# li.distance() # 9.433981132056603

# print(li.slope() # 1.6


# # ((x2-x1)**2 + (y2-y1)**2)**0.5 # distance

# # (y2-y1)/(x2-x1) #slope

# print(li.distance())



# class Line:
#     def __init__(self,coor1,coor2):
#         self.coor1 = coor1
#         self.coor2 = coor2
#     def distance(self):
#         x1,y1 = self.coor1
#         x2,y2 = self.coor2
#         return ((x2-x1)**2 + (y2-y1)**2)**0.5
#     def slope(self):
#         x1,y1 = self.coor1
#         x2,y2 = self.coor2
#         return (y2-y1)/(x2-x1)
# coordinate1 = (3,2)
# coordinate2 = (8,10)
# li = Line(coordinate1,coordinate2)
# print(li.distance()) # 9.433981132056603
# print(li.slope()) # 1.6

# class Cylinder:
#     def __init__(self,height=1,radius=1):
#         self.height = height
#         self.radius = radius
#     def volume(self):
#         return (self.height*3.14*(self.radius)**2)
#     def surface_area(self):
#          2*(3.14 * (self.radius)**2) + (2*3.14*self.radius*self.height)

# EXAMPLE OUTPUT
# c = Cylinder(2,3)

# print(c.volume() # 56.52

# print(c.surface_area()) # 94.2

# Volume: (self.height*3.14*(self.radius)**2)

# Area: 2*(3.14 * (self.radius)**2) + (2*3.14*self.radius*self.height)


# class Cylinder:
#     def __init__(self,height=1,radius=1):
#         self.height = height
#         self.radius = radius        
#     def volume(self):
#         return self.height*3.14*(self.radius)**2    
#     def surface_area(self):
#         top = 3.14 * (self.radius)**2
#         return (2*top) + (2*3.14*self.radius*self.height)
#     # EXAMPLE OUTPUT
# c = Cylinder(2,3)
# print(c.volume()) # 56.52
# print(c.surface_area()) # 94.2


# class Account:
#     def __init__(self,owner,balance=0):
#         self.owner = owner
#         self.balance = balance

#     def __str__(self):
#         return f'Account owner:{self.owner}\nAccount Balance:{self.balance}'
       
       
#     def deposit(self,dep_amt):
#         self.balance += dep_amt
#         print('Deposit Accepted')

#     def withdraw(self,wd_amt):
#         if self.balance >= wd_amt:
#             self.balance -= wd_amt
#             print('Withdrawl Accepted')
#         else:
#             print('Funds Unavailable!')

# # 1. Instantiate the class
# acct1 = Account('Jose',100)

# # 2. Print the object
# print(acct1) # Account owner: Jose, Account balance: €100


# # 3. Show the account owner attribute
# acct1.owner # 'Jose'


# # 4. Show the account balance attribute
# acct1.balance # 100


# # 5. Make a series of deposits and withdrawals
# acct1.deposit(50) # Deposit Accepted
# acct1.withdraw(75) # Withdrawal Accepted


# # 6. Make a withdrawal that exceeds the available balance
# acct1.withdraw(500) # Funds Unavailable!



# class Account:
#     def __init__(self,owner,balance=0):
#         self.owner = owner
#         self.balance = balance
#     def __str__(self):
#         return f'Account owner: {self.owner}\nAccount balance: €{self.balance}'
#     def deposit(self, dep_amt):
#         self.balance += dep_amt
#         print('Deposit Accepted')
#     def withdraw(self,wd_amt):
#         if self.balance >= wd_amt:
#             self.balance -= wd_amt
#             print('Withdrawl Accepted')
#         else:
#             print('Funds Unavailable!')
# # 1. Instantiate the class
# acct1 = Account('Jose',100)
# # 2. Print the object
# print(acct1) # Account owner: Jose, Account balance: €100
# # 3. Show the account owner attribute
# print(acct1.owner) # 'Jose'
# # 4. Show the account balance attribute
# print(acct1.balance) # 100
# # 5. Make a series of deposits and withdrawals
# acct1.deposit(50) # Deposit Accepted
# acct1.withdraw(75) # Withdrawal Accepted
# # 6. Make a withdrawal that exceeds the available balance
# acct1.withdraw(500) # Funds Unavailable!


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


def check_even(num):
    return num % 2 == 0 

nums = [0,1,2,3,4,5,6,7,8,9,10]

print(nums)
print(list(filter(check_even,nums)))

for n in filter(check_even,nums):
    print(n)