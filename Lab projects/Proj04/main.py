from ImportCar import ImportCar
from DomesticCar import DomesticCar

def main():
    domestic_list = list()
    import_list = list()
    with open("carsInStock.txt") as file_in_stock:
        for car in file_in_stock:
            s_car = car.split()
            if s_car[0] == 'D':
                domestic_list.append(DomesticCar(s_car[1], s_car[2], s_car[3], s_car[4], s_car[5], s_car[6]))
            elif s_car[0] == 'I':
                import_list.append(ImportCar(s_car[1], s_car[2], s_car[3], s_car[4], s_car[5], s_car[6], s_car[7]))
            else:
                print("Error: Neither Import nor Domestic car")


main()