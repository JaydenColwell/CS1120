from Car import Car
class ImportCar:
    def __init__(self, brand, model, year, price, car_type, country, tax):
        Car.__init__(self, brand, model, year, price, car_type)
        self.__country = country
        self.__tax = tax

    def get_country(self):
        return self.__country
    def set_country(self, country):
        self.__country = country
    def get_tax(self):
        return self.__tax
    def set_tax(self, tax):
        self.__tax = tax
    def print_info(self):
        pass