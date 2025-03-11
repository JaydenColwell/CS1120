# Project No.: 2
# Author: Jayden Colwell
# Description: Student class Initializes with needed attributes. Contains methods for getting name and credits,
# taking a class, and printing data.

class Student:
    # Initializes Student with needed attributes
    def __init__(self, name, student_id):
        self.__name = name
        self.__student_id = student_id
        self.__total_credits = 0
        self.__class_list = list()
        self.__credit_list = list()

    # Returns student name
    def get_name(self):
        return self.__name

    # Returns student credit amount
    def get_credits(self):
        return  self.__total_credits

    # Adds course taken. Updates list of classes, list of credits for that class, and total credits for that student
    def take_course(self, course_name, course_credits):
        self.__class_list.append(course_name)
        self.__credit_list.append(course_credits)
        self.__total_credits += course_credits

    # Prints every course taken by the student and the total credits
    def print_data(self):
        for i in range(len(self.__class_list)):
            print(f'Course taken: {self.__class_list[i]} ({self.__credit_list[i]} credits)')

        print(f'\nCredits completed {self.__total_credits}')