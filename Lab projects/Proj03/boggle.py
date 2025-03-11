# Project No.: 3
# Author: Jayden Colwell and Haylie Billingsley
# Description: Boggle class with methods to initialize, show the board, check a word
# with a supporting check letter method, and check palindrome.
import random
import string

class Boggle:
    def __init__(self):
        # Initializes random seed, makes boards for letters and whether they have been checked, and calls show_board.
        random.seed(input("Enter seed: "))
        self.__board_size = 4
        self.__board = [[random.choice(string.ascii_uppercase) for i in range(self.__board_size)] for j in range(self.__board_size)]
        self.__checked_board = [[False for i in range(self.__board_size)] for j in range(self.__board_size)]
        self.show_board()

    def check_word(self):
        # Gets word input and loops through board positions to find first letter.
        word = input("Enter word (in UPPERcase): ")
        for i in range(self.__board_size):
            for j in range(self.__board_size):
                if self.__board[i][j] == word[0]:
                    # Sets position to be checked and runs check_letter for the rest of the word.
                    self.__checked_board[i][j] = True
                    if self.check_letter(word, (i, j)):
                        # Formatted output for finding word sucessfully
                        print("Nice Job!")
                        self.check_palindrome(word)
                        self.show_board()
                        return
                    # If word check doesn't work for that start, it sets location checked to false and continues.
                    self.__checked_board[i][j] = False
        # Fomatted output for not finding the word in the board.
        print("I don't see that word.")
        self.check_palindrome(word)
        print("Are we looking at the same board?")

    def check_letter(self, word, location, index = 1):
        # Makes list of directions, left, right, down, up, for array coordinates.
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        # Base case. Full word has been found.
        if index == len(word):
            return True

        # For each direction, sets new x and y from old location plus direction.
        for direction in directions:
            new_x = direction[0] + location[0]
            new_y = direction[1] + location[1]
            # Checks if new location is on board.
            if 0 <= new_x < self.__board_size and 0 <= new_y < self.__board_size:
                # Checks if location has been checked already and if it contains the correct letter.
                if self.__checked_board[new_x][new_y] == False and self.__board[new_x][new_y] == word[index]:
                    # Sets new location to checked.
                    self.__checked_board[new_x][new_y] = True
                    # Recursive call with new location and next letter in word.
                    if self.check_letter(word, (new_x, new_y), index + 1):
                        return True
                    # If check reaches a dead end, sets the location to not checked.
                    self.__checked_board[new_x][new_y] = False
        # If word is not reachable from path, returns false. 
        return False

    def show_board(self):
        frame = "+---+ " * self.__board_size
        for i in range(self.__board_size):
            print(frame)
            for j in range(self.__board_size):
                if self.__checked_board[i][j] == False:
                    print(f'| {self.__board[i][j]} | ', end='')
                else:
                    print(f'|<{self.__board[i][j]}>| ', end='')
            print(f'\n{frame}')

    def check_palindrome(self, word, index = 0):
        if index > len(word) / 2:
            print(f'The word {word} is a palindrome.')
        elif word[index] != word[len(word) - index - 1]:
            print(f'The word {word} is not a palindrome.')
        else:
            self.check_palindrome(word, index + 1)