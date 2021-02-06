# 1) Write a function that emulates the game "rock, scissors, paper"
# At the entrance, your function accepts your version printed from the console, the computer makes a decision randomly.
import random
def game_rockscissorspaper():
    def determine_the_winner(var1, var2):
        if (var1 == 'rock' and var2 == 'scissors') or + \
                (var1 == 'paper' and var2 == 'rock') or + \
                (var1 == 'scissors' and var2 == 'paper'):
            print('You won')
        elif var1 == var2:
            print('Draw')
        else:
            print('Computer won')

    var_list = ('rock', 'scissors', 'paper')
    var1 = input('Input rock, scissors or paper: ')
    var2 = str(random.choice(var_list))
    print('Choice computer: ', var2)
    determine_the_winner(var1, var2)

game_rockscissorspaper()

# 2)Try to imagine a world in which you might have to stay home for (Corona virus) 14 days at any given time.
# Do you have enough toilet paper(TP) to make it through?
# Although the number of squares per roll of TP varies significantly, we'll assume each roll has 500 sheets,
# and the average person uses 57 sheets per day.

# Create a function that will receive a dictionary with two key/values:
# "people" ⁠— Number of people in the household.
# "tp" ⁠— Number of rolls.
# Return a statement telling the user if they need to buy more TP!

SHEETS_PER_ROLL = 500
SHEETS_PER_DAY = 57
DAYS = 14

def toilet_paper(**dict):
    people = int(dict["people"])
    tp = int(dict["tp"])

    sheets_for_people = SHEETS_PER_DAY * people
    sheets_for_14_days = sheets_for_people * DAYS

    if sheets_for_14_days % SHEETS_PER_ROLL:
        need_roll = (sheets_for_14_days // SHEETS_PER_ROLL) + 1
    else:
        need_roll = sheets_for_14_days // SHEETS_PER_ROLL
    if tp >= need_roll:
        return print('You have enough toilet paper')
    else:
        buy = need_roll - tp
        return print('You need to buy', buy, 'TP!')

d = {}
print('Number of people in the household ', end='')
d["people"] = input()
print('Number of rolls ', end='')
d["tp"] = input()

toilet_paper(**d)


# 3) Make a function that encrypts a given input with these steps:
# Input: "apple"
# Step 1: Reverse the input: "elppa"
# Step 2: Replace all vowels using the following chart:
# a => 0
# e => 1
# i => 2
# o => 2
# u => 3
# # "1lpp0"
# Example:
# encrypt("banana") ➞ "0n0n0baca"
# encrypt("karaca") ➞ "0c0r0kaca"
# encrypt("burak") ➞ "k0r3baca"
# encrypt("alpaca") ➞ "0c0pl0aca"
def encrypt(word):

    # Step 1: Reverse the input: "elppa"
    word1 = word[::-1]

    # Step 2: Replace all vowels using the following chart:
    d = {'a': 0, 'e': 1, 'i': 2, 'o': 2, 'u': 3}
    word2 = ''.join(map(str, [d[x] if x in d.keys() else x for x in word1]))

    return print(word2)

word = input('Input word: ')

encrypt(word)

# **4)Given a 3x3 matrix of a completed tic-tac-toe game, create a function that returns whether the game is a win
# for "X", "O", or a "Draw", where "X" and "O" represent themselves on the matrix, and "E" represents an empty spot.
# Example:
# tic_tac_toe([
#     ["X", "O", "X"],
#     ["O", "X", "O"],
#     ["O", "X", "X"]
# ]) ➞ "X"
#
# tic_tac_toe([
#     ["O", "O", "O"],
#     ["O", "X", "X"],
#     ["E", "X", "X"]
# ]) ➞ "O"
#
# tic_tac_toe([
#     ["X", "X", "O"],
#     ["O", "O", "X"],
#     ["X", "X", "O"]
# ]) ➞ "Draw"

def game_tic_tac_toe(matrix):
    winO = False
    winX = False

    def determine_the_winner(d):
        if ''.join(x for x in d) == 'OOO':
            nonlocal winO
            winO = True
            return print('O')
        elif ''.join(x for x in d) == 'XXX':
            nonlocal winX
            winX = True
            return print('X')

    d1 = []
    d2 = []
    for i in range(len(matrix)):
        d1.append(matrix[i][i])
        d2.append(matrix[i - 1][-i])
    determine_the_winner(d1)
    determine_the_winner(d2)

    # rows
    for i in range(len(matrix)):
        determine_the_winner(matrix[i])

    # colms
    colm0 = []
    colm1 = []
    colm2 = []
    for i in range(len(matrix)):
        colm0.append(matrix[i][0])
        colm1.append(matrix[i][1])
        colm2.append(matrix[i][2])
    determine_the_winner(colm0)
    determine_the_winner(colm1)
    determine_the_winner(colm2)

    if not winX and not winO : return print('Draw')

a = [["X", "X", "O"],
     ["X", "1", "O"],
     ["E", "X", "O"]]

game_tic_tac_toe(a)
