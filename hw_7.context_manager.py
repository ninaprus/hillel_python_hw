# Задача-1
# Создать объект менеджера контекста который будет переходить в папку
# которую он принимает на вход. Так же ваш объект должен принимать
# исключение которое он будет подавлять
# Если флаг об исключении отсутствует, исключение должно быть поднято.
import os

class path_exc:
    def __init__(self, path, *exception):
        self.path = path
        self.exception = exception

    def __enter__(self):
        self.saved_cwd = os.getcwd()  # текущая рабочая директория.
        os.chdir(self.path)  # смена текущей директории

    def __exit__(self, exc_type, exc_val, exc_tb):
        os.chdir(self.saved_cwd)
        return exc_type is not None and issubclass(exc_type, self.exception)


def my_func1():
    res = sum([i for i in range('Hello world')])
    return res


with path_exc('/hillel', TypeError):
    my_func1()
