from my_func_hw import game_rockscissorspaper
from my_func_hw import encrypt
from my_func_hw import Ip
import unittest
from unittest.mock import patch

########################################################### unittest - 1
# class TestHomework1(unittest.TestCase):
#
#     @patch('my_func_hw.get_player1', return_value='paper')
#     @patch('my_func_hw.get_computer', return_value='scissors')
#     def test_game_rockscissorspaper_cwon(self, player1, player2):
#         self.assertEqual(game_rockscissorspaper(), 'Computer won')
#
#     @patch('my_func_hw.get_player1', return_value='pApER')
#     @patch('my_func_hw.get_computer', return_value='scissors')
#     def test_game_rockscissorspaper_cwon2(self, player1, player2):
#         self.assertEqual(game_rockscissorspaper(), 'Computer won')
#
#     @patch('my_func_hw.get_player1', return_value='pApERrr')
#     @patch('my_func_hw.get_computer', return_value='scissors')
#     def test_game_rockscissorspaper_again(self, player1, player2):
#         self.assertEqual(game_rockscissorspaper(), 'Try again')
#
#     @patch('my_func_hw.get_player1', return_value='rock')
#     @patch('my_func_hw.get_computer', return_value='scissors')
#     def test_game_rockscissorspaper_ywon(self, player1, player2):
#         self.assertEqual(game_rockscissorspaper(), 'You won')
#
#     @patch('my_func_hw.get_player1', return_value='rock')
#     @patch('my_func_hw.get_computer', return_value='rock')
#     def test_game_rockscissorspaper_draw(self, player1, player2):
#         self.assertEqual(game_rockscissorspaper(), 'Draw')
#
#     @patch('my_func_hw.get_player1', return_value='')
#     def test_game_rockscissorspaper_draw(self, player1):
#         self.assertEqual(game_rockscissorspaper(), "You've not made a choice")
#
# ########################################################### unittest - 2
#
# class TestHomework2(unittest.TestCase):
#     @patch('my_test_hw.get_word', return_value='apple')
#     def test_encrypt_ok(self, word):
#         self.assertEqual(encrypt(), '1lpp0')
#
#     @patch('my_test_hw.get_word', return_value='apple apple')
#     def test_encrypt_words(self, word):
#         self.assertEqual(encrypt(), 'Only one word')
#
#     @patch('my_test_hw.get_word', return_value='11111')
#     def test_encrypt_integer(self, word):
#         self.assertEqual(encrypt(), 'Only letters or start with _')
#
#     @patch('my_test_hw.get_word', return_value='привет')
#     def test_encrypt_cyrillic(self, word):
#         self.assertEqual(encrypt(), 'Only latin')
#
#     @patch('my_test_hw.get_word', return_value='new-york')
#     def test_encrypt_with(self, word):
#         self.assertEqual(encrypt(), 'kr2y-w1n')
#
#     @patch('my_test_hw.get_word', return_value='AAAaaa')
#     def test_encrypt_lower(self, word):
#         self.assertEqual(encrypt(), '000AAA')
#
#     @patch('my_test_hw.get_word', return_value='_AAAaaa')
#     def test_encrypt_startswith(self, word):
#         self.assertEqual(encrypt(), '000000')
#
#     @patch('my_test_hw.get_word', return_value="\\\\")
#     def test_encrypt_symbol1(self, word):
#         self.assertEqual(encrypt(), 'Only letters or start with _')
#
#     @patch('my_test_hw.get_word', return_value='_-----')
#     def test_encrypt_symbol2(self, word):
#         self.assertEqual(encrypt(), '-----')
#
#     @patch('my_test_hw.get_word', return_value="ladies'")
#     def test_encrypt_symbol3(self, word):
#         self.assertEqual(encrypt(), "'s12d0l")
#
# if __name__ == "__main__":
#     unittest.main()
#
#
# ########################################################### pytest
#
# import pytest
#
# @pytest.fixture(scope='session')
# def ip():
#     return Ip(['12.13.15.14', '10.11.12.13'])
#
#
# def test_get_ip(ip):
#     actual = ip.get_ip()
#     expected = ['12.13.15.14', '10.11.12.13']
#     assert_equal(actual, expected)
#
#
# def test_get_ip_expand(ip):
#     actual = ip.get_ip_expand()
#     expected = ['14.15.13.12', '13.12.11.10']
#     assert_equal(actual, expected)
#
#
# def test_get_ip_without_first(ip):
#     actual = ip.get_ip_without_first()
#     expected = ['13.15.14', '11.12.13']
#     assert_equal(actual, expected)
#
#
# def test_get_last_ip(ip):
#     actual = ip.get_last_ip()
#     expected = ['14', '13']
#     assert_equal(actual, expected)
#
#
# def assert_equal(x, y):
#     assert x == y, f'{x} != {y}'

########################################################### doctest

import doctest

# ЗАДАЧА-2
# Написать декоратор который будет выполнять предпроверку типа аргумента который передается в вашу функцию.
# Если это int, тогда выполнить функцию и вывести результат, если это str(),
# тогда зарейзить ошибку ValueError (raise ValueError(“string type is not supported”))
import functools

def type_arg(func):
    """Decorator checks the type argument that is passed to your function."""
    @functools.wraps(func)
    def wrapper_type_arg(args):
        try:
            if isinstance(args, int) or isinstance(args, float):
                value = func(int(args))
                return value
            elif isinstance(args, str):
                raise ValueError('String type is not supported')
            else:
                raise TypeError('Type is not supported')
        except MemoryError:
            print('Too large')
    return wrapper_type_arg


@type_arg
def my_func(number):
    """ The function sums the value in the list and returns the result
    >>> my_func()
    Traceback (most recent call last):
    ...
    TypeError: wrapper_type_arg() missing 1 required positional argument: 'args'
    >>> my_func(5)
    10
    >>> my_func(5.0)
    10
    >>> my_func(5*2)
    45
    >>> my_func(5.856)
    10
    >>> my_func(-5)
    0
    >>> my_func('5')
    Traceback (most recent call last):
    ...
    ValueError: String type is not supported
    >>> my_func((5,))
    Traceback (most recent call last):
    ...
    TypeError: Type is not supported
    >>> my_func(None)
    Traceback (most recent call last):
    ...
    TypeError: Type is not supported
    >>> my_func(1e100)
    Too large
    """
    res = sum([i for i in range(number)])
    return res

if __name__ == "__main__":
    doctest.testmod()