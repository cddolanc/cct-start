# num1 = int(input('Please enter a number: '))
# if num1 %2 == 0 and num1 > 50:
#     print("That's even bigger than I thought! ")
# elif num1 %2 == 0 and num1 < 50:
#     print("That's smaller than I thought")
# else:
#     print("Hmmm...That's odd!")

# class Student:
#     def _init_:
#         name_student = input(print('Please enter tour name: '),
#         email_student = input(print('Please enter tour name: '),

# print(name_student)

# student()


# class Student:
#     def __init__(self, Name, Study, Email):
#         self.name = Name
#         self.study = Study
#         self.email = Email

#     def study(self):
#         print("Is studying:" + self.study + " and my name is " + self.name)

# show = Student("Oisin","Computer science", "...@gmail.com")
# show.study()


class Student:
    def __init__(self, name, course, email):
        self.name = name
        self.course = course
        self.email = email
        
    def study(self):
        print(f'My name is {self.name} and I am busy studying {self.course}')

me = Student("Michael", "test@bigcorp.com", "AI")
me.study()
