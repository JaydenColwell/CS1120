# Written by Jayden Colwell
def part1():
    orders = [ ["34587", "Learning Python, Mark Lutz", 4, 40.95],
               ["98762", "Programming Python, Mark Lutz", 5, 56.80],
               ["77226", "Head First Python, Paul Barry", 3,32.95],
               ["88112", "Einführung in Python3, Bernd Klein",   3, 24.99]]

    # Prints a list of tuples mapped to an if else checking whether each quantity * price is over 100, if not it adds 10.
    # Prints [(order number, rounded price),...]
    print(list(map(lambda x:(x[0], round(x[2] * x[3],2)) if x[2] * x[3] >= 100 else (x[0], round(x[2] * x[3] + 10,2)), orders)))

def part2():
    orders = [[1, ("5464", 4, 9.99), ("8274", 18, 12.99), ("9744", 9, 44.95)],
              [2, ("5464", 9, 9.99), ("9744", 9, 44.95)],
              [3, ("5464", 9, 9.99), ("88112", 11, 24.99)],
              [4, ("8732", 7, 11.99), ("7733", 11, 18.99), ("88112", 5, 39.95)]]

    # Prints a list of tuples with the order number and the sum of prices * quantities for the whole order.
    # Prints [(order number, rounded price),...]
    print([(order[0], round(sum(item[1] * item[2] for item in order[1:]), 2)) for order in orders])

part1()
part2()