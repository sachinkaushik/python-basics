# creating class 

class Student:
    #name = 'Champ'
    #grade = 10

    # we can gie any name here for self.. other name also alloweed, but self is a standard way

    # __init__ method - constructor, value intialize
    # self paramaeter - reference or connection build bw class n object
    def __init__(self, name, grade, percentage):
        self.name = name
        self.grade = grade
        self.percentage = percentage


    def student_details(self):
        print(f"{self.name} is in grade {self.grade}, percentage {self.percentage}")


#create object  - instance of class
student1 = Student('Champ1', 1, 98) #object 1
print(student1.name)
print(student1.grade)
student1.student_details()

print(student1.__dict__)

student2 = Student('champ2', 2, 99) #object 2
print(student2.name)
print(student2.grade)


# modeify object property

student1.percentage = 99
student1.student_details()

# delete object property
del student1.percentage
print(student1.__dict__)

# delete object
del student1
print(student1)