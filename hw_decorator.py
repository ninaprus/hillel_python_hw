# ЗАДАЧА-1
# Написать свой декоратор который будет проверять остаток от деления числа 100 на результат работы функции ниже.
# Если остаток от деления = 0, вывести сообщение "We are OK!», иначе «Bad news guys, we got {}» остаток от деления.
import functools

def divide_by_100(func):
    @functools.wraps(func)
    def wrapper_divide_by_100(*args, **kwargs):
        value = func(*args, **kwargs)
        remainder = 100 % value
        if not remainder:
            print(f'We are OK!')
        else:
            print(f'Bad news guys, we got {remainder}')
        return value
    return wrapper_divide_by_100

@divide_by_100
def math_func(number):
    res = sum([i for i in range(number)])
    return res

print(math_func(5))

# ЗАДАЧА-2
# Написать декоратор который будет выполнять предпроверку типа аргумента который передается в вашу функцию.
# Если это int, тогда выполнить функцию и вывести результат, если это str(),
# тогда зарейзить ошибку ValueError (raise ValueError(“string type is not supported”))

def type_arg(func):
    @functools.wraps(func)
    def wrapper_type_arg(args):
        if type(args)==int:
            value = func(args)
            return value
        elif type(args)==str:
            raise ValueError('String type is not supported')
        else:
            pass
    return wrapper_type_arg

@type_arg
def my_func(number):
    res = sum([i for i in range(number)])
    return res

print(my_func('10'))

# ЗАДАЧА-3
# Написать декоратор который будет кешировать значения аргументов и результаты работы вашей функции и записывать
# его в переменную cache. Если аргумента нет в переменной cache и функция выполняется, вывести сообщение
# «Function executed with counter = {}, function result = {}» и количество раз сколько эта функция выполнялась.
# Если значение берется из переменной cache, вывести сообщение «Used cache with counter = {}» и
# количество раз обращений в cache.
