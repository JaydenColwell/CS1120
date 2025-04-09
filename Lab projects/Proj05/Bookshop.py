# Project No.: 5
# Author: Jayden Colwell
# Description: Class bookshop which takes an orders list and manipulates it to get lots of specific data from methods
class Bookshop:
    # Initializes with orders list for each of the methods to use
    def __init__(self):
        self.orders = [[1, ("5464", 4, 9.99), ("8274", 18, 12.99), ("9744", 9, 44.95)],
                       [2, ("5464", 9, 9.99), ("9744", 9, 44.95)],
                       [3, ("5464", 9, 9.99), ("88112", 11, 24.99)],
                       [4, ("8732", 7, 11.99), ("7733", 11, 18.99), ("88112", 5, 39.95)]]

    # reduces list to total price instead of price and quantity. Also adds $10 if less than $100 total
    def book_to_total(self):
        new_list = list()
        for order in self.orders:
            temp = [order[0]]
            for book in order[1:]:
                if (book[1] * book[2]) < 100:
                    temp.append((book[0],book[1] * book[2] + 10))
                else:
                    temp.append((book[0], book[1] * book[2]))
            new_list.append(temp)
        return new_list

    # Gets the minimum total price for each order and returns the list of each
    def remove_min(self):
        new_list = list()
        for order in self.orders:
            minimum_book = order[1][0]
            minimum_price = order[1][1] * order[1][2]
            for book in order[2:]:
                if book[1] * book[2] < minimum_price:
                    minimum_book = book[0]
                    minimum_price = book[1] * book[2]
            new_list.append((order[0], minimum_book))
        return new_list

    # Gets the maximum total price for each order and returns the list of each
    def remove_max(self):
        new_list = list()
        for order in self.orders:
            maximum_book = order[1][0]
            maximum_price = order[1][1] * order[1][2]
            for book in order[2:]:
                if book[1] * book[2] > maximum_price:
                    maximum_book = book[0]
                    maximum_price = book[1] * book[2]
            new_list.append((order[0], maximum_book))
        return new_list

    # Calculates total order price and returns a list of bookshop order number and total prices
    def total_cost(self):
        new_list = list()
        for order in self.orders:
            total = 0
            for book in order[1:]:
                total += book[1] * book[2]
            total = round(total, 2)
            new_list.append((order[0], total))
        return new_list

    # Makes a dictionary with book numbers and total ordered price and returns the biggest
    def step5(self):
        new_list = list()
        temp_dict = dict()
        for order in self.orders:
            for book in order[1:]:
                if book[0] in temp_dict:
                    temp_dict[book[0]] += book[1] * book[2]
                else:
                    temp_dict[book[0]] = book[1] * book[2]
        max_book = ''
        max_price = 0
        for book, price in temp_dict.items():
            if price > max_price:
                max_book = book
                max_price = price
        new_list.append(max_book)
        new_list.append(max_price)
        return new_list

    # Makes a dictionary with book numbers and total amount ordered and returns the biggest
    def step6(self):
        new_list = list()
        temp_dict = dict()
        for order in self.orders:
            for book in order[1:]:
                if book[0] in temp_dict:
                    temp_dict[book[0]] += book[1]
                else:
                    temp_dict[book[0]] = book[1]
        max_book = ''
        max_num = 0
        for book, num in temp_dict.items():
            if num > max_num:
                max_book = book
                max_num = num
        new_list.append(max_book)
        new_list.append(max_num)
        return new_list

    # Finds bookshop order numbers and total quantity and returns a list sorted by quantity per order
    def step7(self):
        new_list = list()
        for order in self.orders:
            total = 0
            for book in order[1:]:
                total += book[1]
            total = round(total, 2)
            new_list.append((order[0], total))
        new_list = sorted(new_list, key=lambda x: x[1], reverse=True)
        return new_list

    # Returns total quantity of books ordered
    def step8(self):
        total = 0
        for order in self.orders:
            for book in order[1:]:
                total += book[1]
        return total

    # Returns most ordered book number and least ordered book number
    def step9(self):
        new_list = list()
        temp_dict = dict()
        for order in self.orders:
            for book in order[1:]:
                if book[0] in temp_dict:
                    temp_dict[book[0]] += book[1]
                else:
                    temp_dict[book[0]] = book[1]
        max_book = ''
        max_num = 0
        min_book = ''
        min_num = 1000
        for book, num in temp_dict.items():
            if num > max_num:
                max_book = book
                max_num = num
            if num < min_num:
                min_book = book
                min_num = num
        new_list.append(max_book)
        new_list.append(min_book)
        return new_list

    # Makes a list of the length of each order and returns it
    def step10(self):
        new_list = list()
        for order in self.orders:
            new_list.append(len(order))
        return new_list

