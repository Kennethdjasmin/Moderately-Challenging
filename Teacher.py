from Person import Person

class Teacher(Person):
    def __init__(self, name = "", address = ""):
        super().__init__(name, address)
        self.__numCourses = 0
        self.__courses = []

    def toString(self):
        return "Teacher: " + super().toString()

    def addCourse(self, course = ""):
        if course in self.__courses:
            return False
        else:
            self.__courses.append(course)

    def removeCourse(self, course):
        if course in self.__courses:
            self.__courses.remove(course)
        else:
            return False

    # this is just for testing
    def printCourses(self):
        for i in self.__courses:
            print(i)