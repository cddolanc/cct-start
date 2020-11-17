# try:
#     f = open('testfile','w')
#     f.write('Test write this!')
# except IOError:
#     # This will only check for an IOError exception and then execute this print statement
#     print("Error: Could not find file or read data")
# else:
#     print("Content written successfully")
#     f.close()

# try:
#     f = open('testfile','r')
#     f.write('Test write this')
# except:
#     # This will only check for an IOError exception and then execute this print statement
#     print("Error: Could not find file or read data")
# else:
#     print("Content written successfully")
#     f.close()

# try:
#     f = open("testfile", "r")
#     f.write("Test write statement")
#     f.close()
# finally:
#     print("Always execute finally code blocks")

def askint():
    while True:
        try:
            val = int(input("Please enter an integer: "))
        except:
            print("Looks like you did not enter an integer!")
            continue
        else:
            print("Yep That's an integer!")
            print(val)
            break
        finally:
            print("Finally, I executed!")
        print(val)

askint()


from math import sqrt

def ask():
    while True:
        try:
            number1 = int(input('Please enter an integer: ')
                print(sqrt(number1)
        except:
            print("That is not an integer!")

ask()
