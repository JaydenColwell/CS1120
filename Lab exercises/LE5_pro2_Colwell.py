# Written by Jayden Colwell
import csv

def main():
    add_students()
    display_students()

def add_students():
    # Asks for input for full name and 3 exam scores and writes to csv
    with open("grades.csv", 'w', newline='') as outfile:
        writer = csv.writer(outfile)
        for i in range(3):
            print(f'Student {i + 1}')
            first_name = input("First name: ")
            last_name = input("Last name: ")
            exam1 = int(input("exam 1: "))
            exam2 = int(input("exam 2: "))
            exam3 = int(input("exam 3: "))
            print()
            writer.writerow([first_name, last_name, exam1, exam2, exam3])

def display_students():
    # Opens csv file and displays names, grades, and averages
    with open("grades.csv", 'r', newline='') as infile:
        reader = csv.reader(infile)
        avg_exam1 = 0
        avg_exam2 = 0
        avg_exam3 = 0
        for line in reader:
            first_name, last_name, exam1, exam2, exam3 = line
            exam1 = int(exam1)
            avg_exam1 += exam1
            exam2 = int(exam2)
            avg_exam2 += exam2
            exam3 = int(exam3)
            avg_exam3 += exam3
            print(f'{first_name} {last_name} {exam1} {exam2} {exam3} {(exam1+exam2+exam3)/3:.2f}')

        # formatted output with averages
        print(f'\t\t\t\t{avg_exam1/3:.0f} {avg_exam2/3:.0f} {avg_exam3/3:.0f}')
main()