# st = 'Print only the words that start with s in this sentence'
# for word in st.split():
#     if word[0] == 's':
#         print(word)


# print(list(range(0,11,2)))


# print([x for x in range(1,51) if x % 3 == 0])


# st = 'Print only the words that start with s in this sentence'
# for word in st.split():
#     if len(word)%2 == 0:
#         print(word+"  even.")

# for num in range(1,101):
#     if num%3 ==0 and num%5 == 0:
#         print('FizzzBUZZ')
#     elif num%3 == 0:
#         print('Fizz')
#     elif num%5 == 0:
#         print('Buzz')
#     else:
#         print(num)

# st = 'Print only the words that start with s in this sentence'
# print([word[0] for word in st.split()])

import random
ran1 = (random.randint(0,101))
print(ran1)
lst = [0]
lst = input('Please guess a number between 1 and 100: ')

print(lst)

while lst != ran1:
    print('Please try again: ')
    lst
    if lst == ran1:
        print('Correct!')
