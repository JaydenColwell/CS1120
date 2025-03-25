# Project No.: 4
# Author: Jayden Colwell
# Description: Main program that takes input from files, creates lists for domestic and import cars,
# and prints tables with info for multiple purposes.
from ImportCar import ImportCar
from DomesticCar import DomesticCar

def main():
    # Initializes domestic and import car lists
    domestic_list = list()
    import_list = list()
    print("Step One:")
    # Calls add_cars function to add cars in stock and proceeds to print if file opens.
    import_list, domestic_list, proceed = add_cars(import_list, domestic_list, "Cars in Stock")
    if proceed:
        print_all(import_list, domestic_list)
        print("\nStep Two")
        # Calls add_cars function to add cars expected to arrive and proceeds if file opens.
        import_list, domestic_list, proceed = add_cars(import_list, domestic_list, "Cars expected to arrive")
        if proceed:
            print_all(import_list, domestic_list)
            print("\nStep Three")
            # Increases import tax by 5% on Japanese cars and raises price by 15% on domestic cars.
            for car in import_list:
                car.tax_by_country("Japan", 5)
            for car in domestic_list:
                car.increase_price(15)
            # Prints all cars, prints cars below $15,000, then prints total price of all cars.
            print_all(import_list, domestic_list)
            print_price(import_list, domestic_list, 15000)
            get_total_price(import_list, domestic_list)

def add_cars(import_list, domestic_list, info):
    file_name = input(f'Please enter a file name (with information about {info}):')
    print(f'Input file name for {info}: {file_name}')
    try:
        # Opens file, adds new object to corresponding domestic or import list.
        with open(file_name) as file:
            for car in file:
                s_car = car.split()
                if s_car[0] == 'D':
                    domestic_list.append(DomesticCar(s_car[1], s_car[2], s_car[3], s_car[4], s_car[5], s_car[6]))
                elif s_car[0] == 'I':
                    import_list.append(ImportCar(s_car[1], s_car[2], s_car[3], s_car[4], s_car[5], s_car[6], s_car[7]))
                else:
                    print("Error: Neither Import nor Domestic car")
    except FileNotFoundError or PermissionError:
        # Prints if error opening file and returns lists with just 0 and false to break from main program.
        print(f'The file name {file_name} does not exist.')
        return [0], [0], False
    else:
        # Returns full lists and true to proceed in main.
        return import_list, domestic_list, True

def print_all(import_list, domestic_list):
    # Prints tabular formatted tables of all the cars in the lists.
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
    # Prints tabular formatted tables of the cars equal or less than the provided price.
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
    # Gets and prints total price of all cars including import taxes and sales tax.
    total_price = 0
    for car in import_list:
        total_price += (car.get_price() * (car.get_tax()/100 + 1))
    for car in domestic_list:
        total_price += car.get_price()
    total_price *= 1.06
    print(f'\nTotal price of cars in the Stock: {total_price:,.2f}')
main()