########################################################### unittest

# 1) Write a function that emulates the game "rock, scissors, paper"
# At the entrance, your function accepts your version printed from
# the console, the computer makes a decision randomly.
import random

def game_rockscissorspaper():
    player1 = get_player1('Input rock, scissors or paper: ')
    player1 = player1.lower()
    if player1 == '':
        return "You've not made a choice"
    else:
        print('Your choice: ', player1)
        player2 = get_computer()
        print('Choice computer: ', player2)
        return determine_the_winner(player1, player2)

def get_player1(text):
    var = input(text)
    return var

def get_computer():
    return str(random.choice(('rock', 'scissors', 'paper')))

def determine_the_winner(player1, player2):
    var_list = ('rock', 'scissors', 'paper')
    if player1 in var_list:
        if (player1 == 'rock' and player2 == 'scissors') or + \
                (player1 == 'paper' and player2 == 'rock') or + \
                (player1 == 'scissors' and player2 == 'paper'):
            return 'You won'
        elif player1 == player2:
            return 'Draw'
        else:
            return 'Computer won'
    else:
        return 'Try again'

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
# encrypt("banana") ➞ "0n0n0ba"
# encrypt("karaca") ➞ "0c0r0ka"
# encrypt("burak") ➞ "k0r3ba"
# encrypt("alpaca") ➞ "0c0pl0a"

def encrypt():
    word = get_word('Input word: ')
    if len(word.split(' ')) == 1:
        if word.startswith('_'):
            word = word[1:].lower()
        if word.isalpha() or (True in [item == '-' or item == "'" for item in word]):
            if word.isascii():
                # Step 1: Reverse the input: "elppa"
                word1 = word[::-1]
                # Step 2: Replace all vowels using the following chart:
                d = {'a': 0, 'e': 1, 'i': 2, 'o': 2, 'u': 3}
                word2 = ''.join(map(str, [d[x] if x in d.keys() else x for x in word1]))
                return word2
            else:
                return 'Only latin'
        else:
            return 'Only letters or start with _'
    else:
        return 'Only one word'

def get_word(text):
      return input(text)

########################################################### pytest

# Задача-1
# У вас есть список(list) IP адрессов. Вам необходимо создать
# класс который будет иметь методы:
# 1) Получить список IP адресов
# 2) Получить список IP адресов в развернутом виде
# (10.11.12.13 -> 13.12.11.10)
# 3) Получить список IP адресов без первых октетов
# (10.11.12.13 -> 11.12.13)
# 4) Получить список последних октетов IP адресов
# (10.11.12.13 -> 13)

class Ip:
    def __init__(self, ip):
        self._ip = ip

    def get_ip(self):
        return self._ip

    def get_ip_expand(self):
        res = []
        for item in self._ip:
            self.ip_expand = item.split('.')
            self.ip_expand = '.'.join(self.ip_expand[::-1])
            res.append(self.ip_expand)
        return res

    def get_ip_without_first(self):
        res = []
        for item in self._ip:
            self.ip_without_first = item[3:]
            res.append(self.ip_without_first)
        return res

    def get_last_ip(self):
        res = []
        for item in self._ip:
            self.last_ip = item[-2:]
            res.append(self.last_ip)
        return res
