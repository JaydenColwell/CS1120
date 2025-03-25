# Project No.: 4
# Author: Jayden Colwell
# Description: Domestic car subclass with additional state attribute and methods.
from Car import Car
class DomesticCar(Car):
    # Initializes with superclass init and state attribute.
    def __init__(self, brand, model, year, price, car_type, state):
        Car.__init__(self, brand, model, year, price, car_type)
        self.__state = state

    # setter and getter for state.
    def get_state(self):
        return self.__state
    def set_state(self, state):
        self.__state = state
    # Method to increase price by a certain percent.
    def increase_price(self, percent):
        Car.set_price(self, Car.get_price(self)*(1+(percent/100)))
    # Additional print info for the state attribute in tabular format.
    def print_info(self):
        Car.print_info(self)
        print("{:<4}".format(self.__state))