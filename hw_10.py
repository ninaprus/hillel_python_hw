# Задача-1
# У вас есть файл из нескольких строк. Нужно создать генератор который будет построчно выводить строки из вашего файла.
# При вызове итерировании по генератору необходимо проверять строки на уникальность.
# Если строка уникальна, тогда ее выводим на экран, если нет - скипаем

def gen(my_file):
    unique_lines = []
    while True:
        for line in my_file:
            if line in unique_lines:
                continue
            unique_lines.append(line)
            yield print(line)
        return

with open('example_10hw.txt') as reader:
    my_gen = gen(reader)
    next(my_gen)
    next(my_gen)
    next(my_gen)
    next(my_gen)
    my_gen.close()

# Задача-2 (оригинальный вариант и его делать не обязательно):
# представим есть файл с логами, его нужно бессконечно контролировать
# на предмет возникнования заданных сигнатур.
#
# Необходимо реализовать пайплайн из корутин, который подключается к существующему файлу
# по принципу команды tail, переключается в самый конец файла и с этого момента начинает следить
# за его наполнением, и в случае возникнования запиcей, сигнатуры которых мы отслеживаем -
# печатать результат
#
# Архитектура пайплайна

#                    --------
#                   /- grep -\
# dispenser(file) <- - grep - -> print
#                   \- grep -/
#                    --------

# Структура пайплайна:
# ```
import time


def coroutine(func):
    def wrapper(*args, **kwargs):
        gen = func(*args, **kwargs)
        next(gen)
        return gen
    return wrapper


@coroutine
def printer():
    while True:
        line = yield
        print(f'{line}')


@coroutine
def grep(pattern, target):
    #print(f'Looking for {pattern}')
    while True:
        line = yield
        if pattern in line:
            target.send(line)


@coroutine
def dispenser(targets):
    while True:
        line = yield
        for target in targets:
            target.send(line)


def follow(file, target):
    file.seek(0, 2)
    for line in file:
        if not line:
            time.sleep(0.2)
            continue
        target.send(line)

# ```
#
# Каждый grep следит за определенной сигнатурой
#
# Как это будет работать:
#
# ```
f_open = open('log.txt') # подключаемся к файлу
follow(f_open,
       # делегируем ивенты
       dispenser([
           grep('python', printer()), # отслеживаем
           grep('is', printer()),     # заданные
           grep('great', printer()),  # сигнатуры
       ])
       )
# ```
# Как только в файл запишется что-то содержащее ('python', 'is', 'great') мы сможем это увидеть
#
# Итоговая реализация фактически будет асинхронным ивент хендлером, с отсутствием блокирующих операций.
#
# Если все плохо - план Б лекция Дэвида Бизли
# [warning] решение там тоже есть :)
# https://www.dabeaz.com/coroutines/Coroutines.pdf


#Задача-3 (упрощенный вариант делаете его если задача 2 показалась сложной)
# Вам нужно создать pipeline (конвеер, подобие pipeline в unix https://en.wikipedia.org/wiki/Pipeline_(Unix)).
#
# Схема пайплайна :
# source ---send()--->coroutine1------send()---->coroutine2----send()------>sink
#
# Все что вам нужно сделать это выводить сообщение о том что было получено на каждом шаге и обработку ошибки GeneratorExit.
#

# Например: Ваш source (это не корутина, не генератор и прочее, это просто функция ) в ней опеделите цикл из 10 элементов
# которые будут по цепочке отправлены в каждый из корутин и в каждом из корутив вызвано сообщение о полученном элементе.
# После вызова .close() вы должны в каждом из корутин вывести сообщение что работа завершена.


@coroutine
def sink():
    try:
        while True:
            line = yield
    except GeneratorExit:
        print('Done : sink')

@coroutine
def coroutine2(sink):
    try:
        while True:
            line = yield
            sink.send(line)
            print(f'Coroutine2 got: {line}')
    except GeneratorExit:
        print('Done : coroutine2')


@coroutine
def coroutine1(coroutine2):
    try:
        while True:
            line = yield
            print(f'Coroutine1 got: {line}')
            coroutine2.send(line)
    except GeneratorExit:
        print('Done : coroutine1')


def source(target):
    for i in range(10):
        target.send(f'{i}')
    target.close()

source(coroutine1(coroutine2(sink())))

