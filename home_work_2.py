# 1) Сгенерировать dict() из списка ключей ниже по формуле (key : key* key).
#  keys = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] ожидаемый результат:
# {1: 1, 2: 4, 3: 9 …} 

keys = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print({key: key*key for key in keys})

# 2) Сгенерировать массив(list()). Из диапазона чисел
# от 0 до 100 записать в результирующий массив только четные числа. 

print([x for x in range(100) if x%2==0])

# 3)Заменить в произвольной строке согласные буквы на гласные.
#3 Do not forget that case matters. You may add capitalized
# letters to the initial 'vowels' and 'consonants' arrays or
# use the lower() method to convert the input.
def remove_consonants(my_str):
    consonants='bcdfghjklmnpqrstvwxy'
    new_my_str=[]

    for i in my_str.split():
        new_word=''
        for j in i:
            if j.lower() in consonants:
                j = 'a'
            new_word+=j
        new_my_str.append(new_word)

    return ' '.join(new_my_str)

# 4)Дан массив чисел. [10, 11, 2, 3, 5, 8, 23, 11, 2, 5, 76, 43, 2, 32, 76, 3, 10, 0, 1] 
'''
    4.1) убрать из него повторяющиеся элементы

    a=[10, 11, 2, 3, 5, 8, 23, 11, 2, 5, 76, 43, 2, 32, 76, 3, 10, 0, 1]
    #4.1 To remain the initial data type, we should also use list(set(my_list))
    
    b=list(set(my_list))

    4.2) вывести 3 наибольших числа из исходного массива

    c=sorted(a[:])
    c[-3:]

    4.3) вывести индекс минимального элемента массива

    a.index(min(a))

    4.4) вывести исходный массив в обратном порядке 

    a[::-1]

'''
# 5) Найти общие ключи в двух словарях: 
dict_one = { 'a': 1, 'b': 2, 'c': 3, 'd': 4}
dict_two = { 'a': 6, 'b': 7, 'z': 20, 'x': 40}

#5 It is possible to use 'dict_one.keys() & dict_two.keys()'

set(dict_one.keys()).intersection(set(dict_two.keys()))

# 6)Дан массив из словарей 
data = [
    {'name': 'Viktor', 'city': 'Kiev', 'age': 30},
    {'name': 'Maksim', 'city': 'Dnepr', 'age': 20},
    {'name': 'Vladimir', 'city': 'Lviv', 'age': 32},
    {'name': 'Andrey', 'city': 'Kiev', 'age': 34},
    {'name': 'Artem', 'city': 'Dnepr', 'age': 50},
    {'name': 'Dmitriy', 'city': 'Lviv', 'age': 21}]

# 6.1) отсортировать массив из словарей по значению ключа ‘age' 
#6.1 Your solution works. You may consider using the following to minimize the code:
#data_1 = sorted(data, key=lambda x: x['age'])

data_1=data.copy()

for i in range(0, len(data_1)):
    for j in range(0, len(data_1)-1):
        if data_1[j]['age'] > data_1[j+1]['age']:
            data_1[j], data_1[j+1] = data_1[j+1], data_1[j]

print(data_1)

# 6.2) сгруппировать данные по значению ключа 'city' 
#удалить город как-то еще не получилось
data_2=data.copy()
for i in range(len(data_2)):
    data_new = {}
    for j in range(len(data_2)):

        if data_2[j]['city'] in data_new.keys():
            key = data_2[j]['city']
            data_new[key].append(data_2[j])

        else:
            key = data_2[j]['city']
            data_new[key] = []
            data_new[key].append(data_2[j])

print(data_new)

# вывод должен быть такого вида :
result = {
    'Kiev': [
        {'name': 'Viktor', 'age': 30},
        {'name': 'Andrey', 'age': 34}],

    'Dnepr': [{'name': 'Maksim', 'age': 20},
              {'name': 'Artem', 'age': 50}],
    'Lviv': [{'name': 'Vladimir', 'age': 32},
             {'name': 'Dmitriy', 'age': 21}]
}

# =======================================================
# 7) У вас есть последовательность строк. Необходимо определить наиболее часто встречающуюся строку в последовательности.
# Например:
#7 it is possible to make it simpler:
max(set(list_var), key = list_var.count)

def most_frequent(list_var):
    #your code is here
    count={}
    for j in list_var:
        if j in count.keys():
            count[j]+=1
        else:
            count[j]=1

    max_count=max(count, key=count.get)
    return max_count

most_frequent(['a', 'a', 'bi', 'bi', 'bi']) == 'bi'
# =======================================================
# 8) Дано целое число. Необходимо подсчитать произведение всех цифр в этом числе, за исключением нулей.
# Например:
# Дано число 123405. Результат будет: 1*2*3*4*5=120.
#8 'if num:' instead of 'if num != 0:'
a = 123405
res = 1

while a > 0:
    num = a % 10
    if num:
        res *= num
    a = a // 10

print(res)

# =======================================================
# 9) Есть массив с положительными числами и число n (def some_function(array, n)).
# Необходимо найти n-ую степень элемента в массиве с индексом n. Если n за границами массива, тогда вернуть -1.

def some_function(array, n):
    try:
        print(pow(array[n],n))
    except IndexError:
        print('-1')

# =======================================================
# 10) Есть строка со словами и числами, разделенными пробелами (один пробел между словами и/или числами).
# Слова состоят только из букв. Вам нужно проверить есть ли в исходной строке три слова подряд.
# Для примера, в строке "hello 1 one two three 15 world" есть три слова подряд.

str1='hello 1 one two three 15 world'

def find_3_words(str1):
    count=0

    for i in str1.split():
        if i.isalpha():
            count+=1
            if count == 3:
                return print('found 3 words')
        else: count=0
    return print('not found')

# =======================================================


