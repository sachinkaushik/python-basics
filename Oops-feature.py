#Abstraction
#Encapsulation
#Inheritance
#Ploymophsim


#1 Abtraction : Hiding internal details and showing only functionality using abstract base classes.

class StudentOld:

    #Constructor (__init__ method) : Called automatically when an object is created.
    def __init__(self, name, grade, percentage, team):
        self.name = name
        self.grade = grade
        self.percentage = percentage
        self.team = team

    def  __del__(self): #Called when an object is destroyed.
        print("Object is destroyed")

    def student_details(self):
        print(f"{self.name} is in grade {self.grade}, percentage {self.percentage}") # methos abstraction


#Encapsulation        : to restrict the properties from the end user
# we can make propery private using double underscore (__) before attribute

class Student:

    def __init__(self, name, grade, percentage):
        self.name = name
        self.grade = grade
        self.__percentage = percentage  # double underscore limits access, now how can we use it ?


    def get_percentage(self): # we can access using function/method
        return self.__percentage

    def student_details(self):
        print(f'Student name is {self.name} , and in grade {self.grade}')

student1 = Student('Champ', 1, 12)
#print(student1.__percentage)         # it wont be accessable like this

print(student1.get_percentage())


## Inheritance : One class can inherit properties of another.

# This is how we implement the Inheritance in Python, we are passing parent class in parenthesis of child class
class GraduateStudent(Student):

    def __init__(self, name, grade, percentage, stream):
        super().__init__(name, grade, percentage) ## this is calling parent class constructor 
        self.stream = stream

    def student_details(self):
        super().student_details()
        print(f'Stream is {self.stream}')


graduateStudent = GraduateStudent('Python', 12, 98, 'CS')        

print(graduateStudent.stream)
print(graduateStudent.name)
print(graduateStudent.get_percentage())
print(graduateStudent.student_details())


# Polymorphism
class MasterStudent(Student):

    def __init__(self, name, grade, percentage, stream):
        super().__init__(name, grade, percentage) ## this is calling parent class constructor 
        self.stream = stream

    def student_details(self): #same method behaves differently for different classes.
        print(f'Master Student : Stream is {self.stream}')

grad_student = GraduateStudent('Python', 6, 96, 'Python')        
grad_student.student_details()

master_student = MasterStudent('Java', 2, 99, 'Java')        
master_student.student_details()
