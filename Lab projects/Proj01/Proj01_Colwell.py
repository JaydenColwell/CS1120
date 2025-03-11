# Project No.: 1
# Author: Jayden Colwell
# Description: Checks for user file and creates a dictionary from it with an English word as key,
# and list of spanish words as values. Asks user for length of quiz and quizzes user with random vocab.
# Checks for correct answers and creates an output file with data afterward.
import random

def main():
    # Formatted title and filename. Calls get_dict with filename.
    print("Welcome to the vocabulary quiz program.\n")
    filename = input("Please enter a filename: ")
    procede, quiz_dict = get_dict(filename)

    # If file opens, collect user data.
    if procede:
        print(f'{len(quiz_dict)} entries found.')
        user_name = input("Please enter your full name: ")
        date = input("Please enter the date: ")
        print('\n')
        quiz_length = ''
        # Get number of words to be quizzed on with input validation.
        while not quiz_length.isdigit() or (quiz_length.isdigit() and (int(quiz_length) <= 0 or int(quiz_length) > len(quiz_dict))):
            quiz_length = input("How many words would you like to be quized on? ")
            if not quiz_length.isdigit():
                print("Please enter a valid number.")
            elif int(quiz_length) <= 0 or int(quiz_length) > len(quiz_dict):
                print(f'Please enter a valid number between 1 and {len(quiz_dict)}.')

        # When length of quiz passes, get english word list of that length from keys.
        quiz_length = int(quiz_length)
        eng_word_list = random.sample(list(quiz_dict.keys()), quiz_length)
        correct_guesses = 0
        # Quizes user on each word from random selections.
        for word in eng_word_list:
            guess_list = list()
            print(f'English word: {word}')
            print(f'Enter {len(quiz_dict[word])} equivalent Spanish word(s).', end=' ')
            for i in range(len(quiz_dict[word])):
                temp_guess = input(f'Word [{i+1}]: ')
                guess_list.append(temp_guess)
            # Checks guesses with guess_correct function and outputs answer.
            guess_correct = check_quizWords(word, guess_list, quiz_dict)
            if guess_correct == True:
                correct_guesses += 1
                print("Correct!")
            else:
                print("Incorrect.")
            print("\n---\n")

        print(f'{correct_guesses} out of {len(eng_word_list)} correct.')
        outfile = input("Enter an output file (or press enter to quit): ")

        if outfile != '':
            for word in list(quiz_dict.keys()):
                if word not in eng_word_list:
                    quiz_dict.pop(word)
            make_quizFile(user_name, date, quiz_dict, correct_guesses, outfile)

    print("\nBye!")

def get_dict(filename):
    quiz_dict = dict()
    # Try opening file and splitting into dictionary with English as key and list of spanish as value.
    try:
        with open(filename) as infile:
            for line in infile:
                line = line.rstrip('\n')
                temp_split = line.split(':')
                if ',' in temp_split[1]:
                    temp_split[1] = temp_split[1].split(',')
                else:
                    temp_split[1] = [temp_split[1]]
                quiz_dict[temp_split[0]] = temp_split[1]
    except FileNotFoundError or PermissionError:
        # Prints if error opening file and returns false to skip main.
        print(f'The file name {filename} does not exist.')
        return False, quiz_dict
    else:
        return True, quiz_dict
        
def make_quizFile(userName, date, quizDict, correct_guesses, file):
    # Writes formatted output file unless error opening.
    try:
        with open(file, 'w') as outfile:
            outfile.write(f'Name: {userName}\n')
            outfile.write(f'Date: {date}\n')
            for word in list(quizDict.keys()):
                outfile.write(f'{word}:')
                for answer in range(len(quizDict[word])):
                    if answer == len(quizDict[word]) - 1:
                        outfile.write(f'{quizDict[word][answer]}\n')
                    else:
                        outfile.write(f'{answer}, ')
            outfile.write(f'{correct_guesses} out of {len(quizDict)} correct.\n')
    except FileNotFoundError or PermissionError:
        # Prints if error opening file and returns false to skip main.
        print(f'The file name {file} does not exist and cannot be created.')

def check_quizWords(engWords, spaWords, quizDict):
    correct = True
    # Checks if user entered spanish words are the same as in dictionary.
    if set(spaWords) != set(quizDict[engWords]):
        correct = False

    return correct
    
main()
