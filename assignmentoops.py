class Student:
    def __init__(self):
        self.__name = None
        self.__rollNumber = None
    def setName(self, name):
        self.__name = name
    def getName(self):
        return self.__name
    def setRollNumber(self, rollNumber):
        self.__rollNumber = rollNumber
    def getRollNumber(self):
        return self.__rollNumber
name = input()
rollnumber = int(input())
student = Student()
student.setName(name)
student.setRollNumber(rollnumber)
name = student.getName()
rollNumber = student.getRollNumber()
print("Name:", name)
print("Roll Number:", rollNumber)
