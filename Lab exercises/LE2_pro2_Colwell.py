# Written by Jayden Colwell
class Employee:
    # Initializes the object with all of the attributes
    def __init__(self, name, id_number, department, job_title):
        self.__name = name
        self.__id_number = id_number
        self.__department = department
        self.__job_title = job_title

    # No setter methods as all attributes are handled in initialization and none are modified

    # Only getter method to make display easier
    def display(self):
        print(f'Name: {self.__name}\tID Number: {self.__id_number}\tDepartment: {self.__department}\tJob Title: {self.__job_title}')

def main():
    # Creates each employee object with attributes and displays the data for each employee
    employee1 = Employee("Susan Meyers",	47899,	"Accounting",	"Vice President")
    employee1.display()
    employee2 = Employee("Mark Jones",	39119,	"IT",	"Programmer")
    employee2.display()
    employee3 = Employee("Joy Rogers",	81774,	"Manufacturing",	"Engineer")
    employee3.display()

# Used so that class can be imported to another program to be used
if __name__ == "__main__":
    main()

# I wasn't sure if you wanted setters and getters for each attribute but the instructions didn't talk about modifying them so I did not.
# Also I wasn't sure if you wanted this in 2 separate programs but all you would do is have the main function in another file with something
# Similar to "from class_file import Employee" to import the class to be used.