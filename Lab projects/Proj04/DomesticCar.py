from Car import Car
class DomesticCar:
    def __init__(self, brand, model, year, price, car_type, state):
        Car.__init__(self, brand, model, year, price, car_type)
        self.__state = state

    def get_state(self):
        return self.__state
    def set_state(self, state):
        self.__state = state
    def print_info(self):
        pass