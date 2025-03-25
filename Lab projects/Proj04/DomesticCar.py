from Car import Car
class DomesticCar(Car):
    def __init__(self, brand, model, year, price, car_type, state):
        Car.__init__(self, brand, model, year, price, car_type)
        self.__state = state

    def get_state(self):
        return self.__state
    def set_state(self, state):
        self.__state = state
    def increase_price(self, percent):
        Car.set_price(self, Car.get_price(self)*(1+(percent/100)))
    def print_info(self):
        Car.print_info(self)
        print("{:<4}".format(self.__state))