# Project No.: 4
# Author: Jayden Colwell
# Description: main car class with setters and getters for all attributes as well as a print info method.
class Car:
    # Initializes brand, model, year, price, and car type.
    def __init__(self, brand, model, year, price, car_type):
        self.__brand = brand
        self.__model = model
        self.__year = year
        self.__price = int(price)
        self.__type = car_type

    # Setters and getters for all attributes.
    def get_brand(self):
        return self.__brand
    def set_brand(self, brand):
        self.__brand = brand
    def get_model(self):
        return self.__model
    def set_model(self, model):
        self.__model = model
    def get_year(self):
        return self.__year
    def set_year(self, year):
        self.__year = year
    def get_price(self):
        return self.__price
    def set_price(self, price):
        self.__price = price
    def get_type(self):
        return self.__type
    def set_type(self, car_type):
        self.__type = car_type
    # Prints general car info in adjusted tabular format.
    def print_info(self):
        print("{:<13} {:<12} {:<6} {:>10,.2f} {:<8}".format(self.__brand, self.__model, self.__year, self.__price, self.__type), end=" ")