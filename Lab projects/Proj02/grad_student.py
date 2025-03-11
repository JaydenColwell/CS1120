# Project No.: 2
# Author: Jayden Colwell
# Description: GradStudent initializes with Student attributes and list of papers
# Methods to get and update list of published papers and print data

from student import Student

class GradStudent(Student):
    # Initializes Student also with list of published papers (because grad)
    def __init__(self, name, student_id):
        Student.__init__(self, name, student_id)

        self.__paper_list = list()

    # Returns number of published papers
    def get_paper_num(self):
        return len(self.__paper_list)

    # Updates published papers list
    def publish_paper(self, paper_name):
        self.__paper_list.append(paper_name)

    # Prints Student data with papers published and number of papers
    def print_data(self):
        for i in range(len(self.__paper_list)):
            print(f'Publication #{i + 1}: {self.__paper_list[i]}')
        Student.print_data(self)
        print(f'Number of publications: {len(self.__paper_list)}')