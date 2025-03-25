from ImportCar import ImportCar
from DomesticCar import DomesticCar

def main():
    domestic_list = list()
    import_list = list()
    import_list, domestic_list = add_cars(import_list, domestic_list, "carsInStock.txt")
    print_all(import_list, domestic_list)
    import_list, domestic_list = add_cars(import_list, domestic_list, "carsExpectedToArrive.txt")
    for car in import_list:
        car.tax_by_country("Japan", 5)
    for car in domestic_list:
        car.increase_price(15)
    print_all(import_list, domestic_list)
    print_price(import_list, domestic_list, 15000)
    get_total_price(import_list, domestic_list)

def add_cars(import_list, domestic_list, file_name):
    with open(file_name) as file_in_stock:
        for car in file_in_stock:
            s_car = car.split()
            if s_car[0] == 'D':
                domestic_list.append(DomesticCar(s_car[1], s_car[2], s_car[3], s_car[4], s_car[5], s_car[6]))
            elif s_car[0] == 'I':
                import_list.append(ImportCar(s_car[1], s_car[2], s_car[3], s_car[4], s_car[5], s_car[6], s_car[7]))
            else:
                print("Error: Neither Import nor Domestic car")
    return import_list, domestic_list

def print_all(import_list, domestic_list):
    print("\nImported Cars")
    for car in import_list:
        car.print_info()
    print("\nDomestic Cars")
    for car in domestic_list:
        car.print_info()
    print(f'\nNumber of imported cars = {len(import_list)}')
    print(f'Number of domestic cars = {len(domestic_list)}')
    print(f'Total = {len(import_list) + len(domestic_list)}')

def print_price(import_list, domestic_list, price):
    count = 0
    print(f'\nFilter price less than: {price:.2f}')
    for car in import_list:
        if car.get_price() <= price:
            car.print_info()
            count += 1
    for car in domestic_list:
        if car.get_price() <= price:
            car.print_info()
            count += 1
    print(f'\nNumber of cars = {count}')

def get_total_price(import_list, domestic_list):
    total_price = 0
    for car in import_list:
        total_price += (car.get_price() * (car.get_tax()/100 + 1))
    for car in domestic_list:
        total_price += car.get_price()
    total_price *= 1.06
    print(f'\nTotal price of cars in the Stock: {total_price:,.2f}')
main()