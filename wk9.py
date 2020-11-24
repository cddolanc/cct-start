# def fahrenheit(celsius):
#     return (9/5)*celsius + 32

# temps = [0, 22.5, 40, 100]

# print(temps)

# F_temps = map(fahrenheit, temps)

# #Show
# print(list(F_temps))

# print(list(map(lambda x: (9/5)*x + 32,temps )))

# a = [1,2,3,4]
# b = [5,6,7,8]
# c = [9,10,11,12]

# print(list(map(lambda x,y:x+y,a,b)))

# # Now all three lists
# print(list(map(lambda x,y,z:x+y+z,a,b,c)))

# from functools import reduce

# lst =[47,11,42,13]
# print(lst)
# print(reduce(lambda x,y: x+y,lst))


# from functools import reduce

# lst =[47,11,42,13]

# #Find the maximum of a sequence (This already exists as max())
# max_find = lambda a,b: a if (a > b) else b

# #Find max
# print(reduce(max_find,lst))





# First let's make a function
# def even_check(num):
#     if num%2 ==0:
#         return True

# lst =range(20)

# print (lst)
# print(list(filter(even_check,lst)))


# print(list(filter(lambda x: x%2==0,range(20))))



# x = [1,2,3]
# y = [4,5,6]

# # Zip the lists together
# print(list(zip(x,y)))



# x = [1,2,3]
# y = [4,5,6,7,8]

# # Zip the lists together
# print(list(zip(x,y)))




# d1 = {'a':1,'b':2}
# d2 = {'c':4,'d':5}

# print(list(zip(d1,d2)))

# print(list(zip(d2.values(),d1.values())))



# d1 = {'a':1,'b':2}
# d2 = {'c':4,'d':5}

# def switcharoo(d1,d2):
#     dout = {}
#     for d1key,d2val in zip(d1,d2.values()):
#         dout[d1key] = d2val   
#     return dout

# print(switcharoo(d1,d2))



# def enumerate(sequence, start=0):
#         n = start
#         for elem in sequence:
#             yield n, elem
#             n += 1


# lst = ['a','b','c']

# for number,item in enumerate(lst):
#     print(number)
#     print(item)



# lst = ['a','b','c']

# for count,item in enumerate(lst):
#     if count >= 2:
#         break
#     else:
#         print(item)



# months = ['March','April','May','June']

# print(list(enumerate(months,start=3)))



# lst = [True,True,False,True]
# print(all(lst))

# print(any(lst))


# Create 2+3j
# complex(2,3)

# complex(10,1)



# def word_lengths(phrase):    
#     return print(len(word_lengths))

# word_lengths = ('How, long, are, the, words, in, this, phrase')
# # print(map(word_lengths, ('How long are the words in this phrase')))

# # print(map(word_lengths, phrase))


#prob1:
def word_lengths(phrase):    
     return list(map(len,phrase.split()))

print(word_lengths = ('How, long, are, the, words, in, this, phrase'))