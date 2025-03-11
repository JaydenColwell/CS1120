# Project No.: 2
# Author: Jayden Colwell
# Description: Recieves student object as input and determines student type and checks graduation requirements by type.
# Prints whether student can graduate or not.

from grad_student import GradStudent
from undergrad_student import UndergradStudent


class GraduationAuditor:
    def __init__(self):
        pass
    
    def audit(self, students):
        for student in students:
            # Learned about isinstance from Dr. Rhodes and https://docs.python.org/3/library/functions.html#isinstance
            # Checks requirements for Undergrad
            if isinstance(student, UndergradStudent):
                if student.get_credits() >= 30 and student.get_community_service() >= 20:
                    print(f'{student.get_name()} can graduate')
                else:
                    print(f'{student.get_name()} cannot graduate')
            # Checks requirements for Grad
            elif isinstance(student, GradStudent):
                if student.get_credits() >= 30 and student.get_paper_num() >= 2:
                    print(f'{student.get_name()} can graduate')
                else:
                    print(f'{student.get_name()} cannot graduate')
            # Prints error if student is not grad or undergrad
            else:
                print("error for student type")