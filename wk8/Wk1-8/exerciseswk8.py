# try:
#     for i in ['a','b','c']:
   
#         print(i**2)
# except:
#         print("This is not correct")


# try:    
#     x = 5
#     y = 0

#     z = x/y
# except:
#     print("There seems to be a problem")

# finally:
#     print('All Done.')

from math import sqrt

def ask():
    while True:
        try:
            val = int(input("Please enter an integer: "))
        except:
            print("That is not an integer!")
            continue
        else:
            print("Yep That's an integer!")
            print(sqrt(val))
            break
        finally:
            print("Finally, I executed!")
            
ask()