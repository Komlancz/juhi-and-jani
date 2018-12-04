import os
import sys
import time
import random
import copy


def board(table, check_table):
    print("Press 'Q' to quit")
    print("Press 'M' to go back to menu \n")

    for lists in table:
        print(*lists)
    if table == check_table:
        print("You Won")
        new_game()


def random_table(table, check_table, color, original):
    diff = 0
    while diff not in range(1, 4):
        try:
            os.system("clear")
            diff = int(input("Please choose difficulty firt: \n\
                        1, Easy \n\
                        2, Medium \n\
                        3, Hard\n"))
        except ValueError:
            continue
    os.system("clear")
    diff_num = 0

    if diff == 1:
        diff_num += 10
    elif diff == 2:
        diff_num += 20
    elif diff == 3:
        diff_num += 40

    row = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    item = [2, 3, 4, 6, 7, 8, 10, 11, 12]

    for i in range(diff_num):
        x = random.choice(row)
        y = random.choice(item)
        old = check_table[x][y]
        if old != int:
            old = original[x][y]
        del check_table[x][y]
        check_table[x].insert(y, color[old])
        del table[x][y]
        table[x].insert(y, " ")


def game(table, check_table, greencolor, redcolor):
    while table != check_table:

        numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]     # list with the allowed numbers
        item = [2, 3, 4, 6, 7, 8, 10, 11, 12]

        board(table, check_table)
        row = input("Row: ")
        if row == "q":
            os.system("clear")
            break
        elif row == "m":
            main()
        elif row in numbers:
            pass

        try:                          # Error handling: if the user gives letter instead of number
            row = int(row)
            column = int(input("Column:"))
            guess = int(input("Guess:"))
        except ValueError:
            print("Give me a NUMBER betwen 1-9")
            time.sleep(2)
            os.system("clear")
            continue

        if column not in numbers or row not in numbers or guess not in numbers:
            print("Give me number between ONE AND NINE!")
            time.sleep(2)                # Error handling 2: if the user give us bigger number that we accept
            os.system("clear")
            continue

        if column in (1, 2, 3):
            column += 1          # Add +1 or +2 or +3 for the users number to choose the correct index item in the list
        elif column in (4, 5, 6):
            column += 2
        elif column in (7, 8, 9):
            column += 3

        if table[row][column] in numbers:              # Find the row and column, delete, and insert the number
            print(" Its not an empty field")
            time.sleep(2)
        else:
            del table[row][column]
            table[row].insert(column, greencolor[guess])

        if table[row][column] != check_table[row][column]:
            del table[row][column]
            table[row].insert(column, redcolor[guess])
        os.system("clear")


def new_game():
    ask = input("Would you like to play again? (Y/N)")
    if ask == "Y" or ask == "y":
        os.system("clear")
        main()


def main():
    green = ["", '\033[92m'+"1"+'\033[0m', '\033[92m'+"2"+'\033[0m', '\033[92m'+"3"+'\033[0m', '\033[92m'+"4"+'\033[0m',
                 '\033[92m'+"5"+'\033[0m', '\033[92m'+"6"+'\033[0m', '\033[92m'+"7"+'\033[0m', '\033[92m'+"8"+'\033[0m',
                 '\033[92m'+"9"+'\033[0m']
    red = ["", '\x1b[31m'+"1"+'\033[0m', '\x1b[31m'+"2"+'\033[0m', '\x1b[31m'+"3"+'\033[0m', '\x1b[31m'+"4"+'\033[0m',
           '\x1b[31m'+"5"+'\033[0m', '\x1b[31m'+"6"+'\033[0m', '\x1b[31m'+"7"+'\033[0m', '\x1b[31m'+"8"+'\033[0m',
           '\x1b[31m'+"9"+'\033[0m', ]
    original = [[" ", " ", "1", "2", "3", " ", "4", "5", "6", " ", "7", "8", "9", "\n", "-"*25],
                ["1", "|", 9, 4, 3, "|", 2, 7, 5, "|", 6, 1, 8, "|"],
                ["2", "|", 2, 5, 6, "|", 1, 4, 8, "|", 9, 7, 3, "|"],
                ["3", "|", 8, 7, 1, "|", 9, 6, 3, "|", 2, 4, 5, "|", "\n", "-"*25],
                ["4", "|", 6, 8, 5, "|", 7, 3, 2, "|", 1, 9, 4, "|"],
                ["5", "|", 4, 3, 7, "|", 5, 9, 1, "|", 8, 2, 6, "|"],
                ["6", "|", 1, 2, 9, "|", 6, 8, 4, "|", 5, 3, 7, "|", "\n", "-"*25],
                ["7", "|", 7, 6, 2, "|", 3, 5, 9, "|", 4, 8, 1, "|"],
                ["8", "|", 5, 1, 8, "|", 4, 2, 7, "|", 3, 6, 9, "|"],
                ["9", "|", 3, 9, 4, "|", 8, 1, 6, "|", 7, 5, 2, "|", "\n", "-"*25]]

    sudoku_full = copy.deepcopy(original)
    sudoku = copy.deepcopy(original)
    random_table(sudoku, sudoku_full, green, original)
    game(sudoku, sudoku_full, green, red)
    board(sudoku, sudoku_full)


if __name__ == "__main__":
    main()
