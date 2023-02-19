import numpy as np
import random

def parse_file(filepath):
    # Parse Questions into a dictionary
    # Key - int: line number of question
    # Value - stiring: the question
    questions = {}
    with open(filepath, 'r') as file:
        for count, line in enumerate(file):
            questions[count] = line.replace('\\n', '\n')

        file.close()

    return questions

def create_board(questions):
    # Create an empty list w/ len 25, ensure unique keys from questions are used
    keys_array = [-1 for x in range(25)]
    for x in range(len(keys_array)):
        rand_num = random.randint(0, len(questions) - 1)

        while rand_num in keys_array:
            rand_num = random.randint(0, len(questions) - 1)

        keys_array[x] = rand_num

    # Convert 1D-key array into 2D string array
    board = [['' for x in range(5)] for x in range(5)]
    for x in range(5):
        for y in range(5):
            # Add the corressponding question to the board, removing ending newline
            board[x][y] = questions[keys_array[x * 5 + y]][:-1]
    
    return board


dict = parse_file(filepath='./Squares.txt')

board = create_board(dict)

for row in board:
    print(row)