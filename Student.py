from Person import Person

class Student(Person):
    def __init__(self, name = "", address = ""):
        super().__init__(name, address)
        self.__cg = {}
        self.__numCourses = 0

    def toString(self):
        return "Student: " + super().toString()

    def addCourseGrade(self, course = "", grade = 0):
        self.__cg[course] = grade
        self.__numCourses = self.__numCourses + 1

    def printGrades(self):
        for i in self.__cg:
            print(i + ": ", self.__cg[i])

    def getAverageGrade(self):
        return sum(self.__cg.values())/self.__numCourses
