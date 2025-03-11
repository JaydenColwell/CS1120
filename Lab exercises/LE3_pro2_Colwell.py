# Written by Jayden Colwell
class Person:
    def __init__(self, name, address, phone_no):
        self.__name = name
        self.__address = address
        self.__phone_no = phone_no

    def display_info(self):
        print(f'Name: {self.__name}')
        print(f'Address: {self.__address}')
        print(f'Phone number: {self.__phone_no}')

class Customer:
    def __init__(self, name, address, phone_no, customer_no, mail_bool):
        Person.__init__(self,name, address,phone_no)

        self.__customer_no = customer_no
        self.__mail_bool = mail_bool
        
    def display_info(self):
        Person.display_info(self)
        print(f'Customer number: {self.__customer_no}')
        print(f'Mail list: {self.__mail_bool}')

def main():
    person1 = Customer("Jayden Colwell", "123 Main", 5173330000,2384, False)
    person1.display_info()

# Used so that class can be imported to another program to be used
if __name__ == "__main__":
    main()