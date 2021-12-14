from Student import Student
from Teacher import Teacher

if __name__ == "__main__":
    test1 = Student("John Smith", "166 Piccadilly, St. James's, London W1J 9EF, UK.")
    print(test1.toString())
    test1.addCourseGrade("math", 100)
    test1.addCourseGrade("physic", 95)
    test1.addCourseGrade("geography", 80)
    test1.addCourseGrade("history", 99)
    test1.addCourseGrade("biology", 85)
    test1.printGrades()
    print(test1.getAverageGrade())

    test2 = Teacher("James Gordon", "3499 NW 1st Ct, Fort Lauderdale, FL")
    print("\n" + test2.toString())
    test2.addCourse("gourmet")
    test2.addCourse("dog training")
    test2.addCourse("fitness training")
    test2.addCourse("boxing")
    test2.removeCourse("dog training")
    test2.printCourses()