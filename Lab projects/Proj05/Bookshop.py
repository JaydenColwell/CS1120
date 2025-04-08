class Bookshop:
    def __init__(self):
        self.orders = [[1, ("5464", 4, 9.99), ("8274", 18, 12.99), ("9744", 9, 44.95)],
                       [2, ("5464", 9, 9.99), ("9744", 9, 44.95)],
                       [3, ("5464", 9, 9.99), ("88112", 11, 24.99)],
                       [4, ("8732", 7, 11.99), ("7733", 11, 18.99), ("88112", 5, 39.95)]]

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

    def total_cost(self):
        new_list = list()
        for order in self.orders:
            total = 0
            for book in order[1:]:
                total += book[1] * book[2]
            total = round(total, 2)
            new_list.append((order[0], total))
        return new_list

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

    def step8(self):
        total = 0
        for order in self.orders:
            for book in order[1:]:
                total += book[1]
        return total

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

    def step10(self):
        new_list = list()
        for order in self.orders:
            new_list.append(len(order))
        return new_list

