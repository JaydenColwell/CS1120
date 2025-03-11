# Project No.: 2
# Author: Jayden Colwell
# Description: UndergradStudent initializes with Student attributes and community service hours.
# Methods to get and update community service and print data

from student import Student


class UndergradStudent(Student):
    # Initializes Student also with community service hours (because undergrad)
    def __init__(self, name, student_id):
        Student.__init__(self, name, student_id)

        self.__total_community_service = 0

    # Returns community service hours
    def get_community_service(self):
        return self.__total_community_service

    # Updates community service hours
    def do_community_service(self, hours):
        self.__total_community_service += hours

    # Prints superclass data and community service hours
    def print_data(self):
        Student.print_data(self)
        print(f'Hours of community service: {self.__total_community_service}')