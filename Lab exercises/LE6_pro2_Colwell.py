# Written by Jayden Colwell
list_num = [1,2,3,4,5,6,7,8,9,10]

# Function for checking even or not
def even_check(n):
    if n % 2 == 0:
        return True
    else:
        return False
# Function for multiplying by 3
def triple(n):
    return n * 3
# Filters to only even, multiplies by 3, then sums. Prints output
print(sum(map(triple, filter(even_check, list_num))))


total = 0
# Makes list of even numbers
list2 = [x for x in list_num if x % 2 == 0]
# Makes list of numbers * 3
list3 = [y * 3 for y in list2]
# sums numbers
for z in list3:
    total += z
# Prints total
print(total)
