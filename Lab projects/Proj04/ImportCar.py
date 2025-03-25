# Project No.: 4
# Author: Jayden Colwell
# Description: Import car subclass with additional country and import tax attributes and methods.
from Car import Car
class ImportCar(Car):
    # Initializes with superclass init and country and import tax attributes.
    def __init__(self, brand, model, year, price, car_type, country, tax):
        Car.__init__(self, brand, model, year, price, car_type)
        self.__country = country
        self.__tax = int(tax)

    # Country and tax setters and getters.
    def get_country(self):
        return self.__country
    def set_country(self, country):
        self.__country = country
    def get_tax(self):
        return self.__tax
    def set_tax(self, tax):
        self.__tax = tax
    # Method that can add to the import tax for cars from a certain country.
    def tax_by_country(self, country, tax_addition):
        if self.__country == country:
            self.set_tax(self.__tax + tax_addition)
    # Additional print info for country and tax in tabular format.
    def print_info(self):
        Car.print_info(self)
        print("{:<10} {:>2}%".format(self.__country, self.__tax))