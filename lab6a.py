#!/usr/bin/env python3
#Nirmal Gautam -ngautam11- OPS445ZAA

class Student:

    def __init__(self, name, number):
        self.name = name
        self.number = str(number)
        self.courses = {}

    def displayStudent(self):
        return 'Student Name: ' + self.name + '\n' + 'Student Number: ' + self.number

    def addGrade(self, course, grade):
        self.courses[course] = grade

    def displayGPA(self):
        gpa = 0.0
        try:
            for course in self.courses.keys():
                gpa = gpa + self.courses[course]
            return 'GPA of student ' + self.name + ' is ' + str(gpa / len(self.courses))
        except ZeroDivisionError:
            return 'GPA of student ' + self.name + ' is 0.0'

    def displayCourses(self):
        return [course for course, grade in self.courses.items() if grade > 0.0]

if __name__ == '__main__':
    student1 = Student('John', 13454900)
    student1.addGrade('uli101', 1.0)
    student1.addGrade('ops245', 2.0)
    student1.addGrade('ops445', 3.0)

    student2 = Student('Jessica', 123456)
    student2.addGrade('ipc144', 4.0)
    student2.addGrade('cpp244', 3.5)
    student2.addGrade('cpp344', 0.0)

    print(student1.displayStudent())
    print(student1.displayGPA())
    print(student1.displayCourses())

    print(student2.displayStudent())
    print(student2.displayGPA())
    print(student2.displayCourses())
