# from collections import Counter

# #Counter() with lists
# lst = [1,2,2,2,2,3,3,3,1,2,1,12,3,2,32,1,21,1,223,1]

# print(Counter(lst))

# print(Counter('aabsbsbsbhshhbbsbs'))


# # Counter with words in a sentence
# s = 'How many times does each word show up in this sentence word times each each word'

# words = s.split()

# print(Counter(words))

# # Methods with Counter()
# c = Counter(words)

# print(c.most_common(2))


# sum(c.values())                 # total of all counts
# c.clear()                       # reset all counts
# list(c)                         # list unique elements
# set(c)                          # convert to a set
# dict(c)                         # convert to a regular dictionary
# c.items()                       # convert to a list of (elem, cnt) pairs
# Counter(dict(list_of_pairs))    # convert from a list of (elem, cnt) pairs
# c.most_common()[:-n-1:-1]       # n least common elements
# c += Counter()                  # remove zero and negative counts


# from collections import defaultdict

# d = {}

# d['one'] 

# d  = defaultdict(object)

# d['one'] 

# for item in d:
#     print(item)




# d = defaultdict(lambda: 0)

# print(d['one'])

# for item in d:
#     print(item)



# t = (12,13,14)

# print(t[0])



# from collections import namedtuple

# Dog = namedtuple('Dog',['age','breed','name'])

# sam = Dog(age=2,breed='Lab',name='Sammy')

# frank = Dog(age=2,breed='Shepard',name="Frankie")

# print(sam)
# print(frank)

# print(sam.age)

# print(sam.breed)
# print(frank.breed)

# print(sam[0])

# prints path that you are in
# import os
# pwd = os.system("pwd")
# print(pwd)

# f = open('practice.txt','w+')
# f.write('test')
# f.close()


# import os

# print(os.getcwd())
# print(os.listdir())


# import shutil

# shutil.move('practice.txt','/workspace/cct-start')

# os.listdir()

# shutil.move('/workspace/cct-start/practice.txt',os.getcwd())

# os.listdir()



# import send2trash

# print(os.listdir())

# send2trash.send2trash('practice.txt')

# print(os.listdir())





# os.getcwd()

# os.listdir()

# for folder , sub_folders , files in os.walk("wk8s"):

#     print("Currently looking at folder: "+ folder)
#     print('\n')
#     print("THE SUBFOLDERS ARE: ")
#     for sub_fold in sub_folders:
#         print("\t Subfolder: "+sub_fold )

#     print('\n')

#     print("THE FILES ARE: ")
#     for f in files:
#         print("\t File: "+f)
#     print('\n')

#     # Now look at subfolders



# import datetime

# t = datetime.time(4, 20, 1)

# # Let's show the different components
# print(t)
# print('hour  :', t.hour)
# print('minute:', t.minute)
# print('second:', t.second)
# print('microsecond:', t.microsecond)
# print('tzinfo:', t.tzinfo)


# print('Earliest  :', datetime.time.min)
# print('Latest    :', datetime.time.max)
# print('Resolution:', datetime.time.resolution)


# today = datetime.date.today()
# print(today)
# print('ctime:', today.ctime())
# print('tuple:', today.timetuple())
# print('ordinal:', today.toordinal())
# print('Year :', today.year)
# print('Month:', today.month)
# print('Day  :', today.day)

# print('Earliest  :', datetime.date.min)
# print('Latest    :', datetime.date.max)
# print('Resolution:', datetime.date.resolution)


# d1 = datetime.date(2015, 3, 11)
# print('d1:', d1)

# d2 = d1.replace(year=1990)
# print('d2:', d2)


# d1

# d2

# print(d1-d2)





# x = [1,3,4]
# y = 2
# z = 3

# result = y + z
# print(result)
# result2 = y+x
# print(result2)


import pdb

x = [1,3,4]
y = 2
z = 3

result = y + z
print(result)

# Set a trace using Python Debugger
pdb.set_trace()

result2 = y+x
print(result2)