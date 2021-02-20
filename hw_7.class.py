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
        for item in self._ip:
            self.ip_expand = item.split('.')
            self.ip_expand = '.'.join(self.ip_expand[::-1])
            print(f'{self.ip_expand}')

    def get_ip_without_first(self):
        for item in self._ip:
            self.ip_without_first = item[3:]
            print(self.ip_without_first)

    def get_last_ip(self):
        for item in self._ip:
            self.last_ip = item[-2:]
            print(self.last_ip)

d=Ip(['12.13.15.14', '10.11.12.13'])
d.get_ip()
d.get_ip_expand()
d.get_ip_without_first()
d.get_last_ip()

# Задача-2
# У вас несколько JSON файлов. В каждом из этих файлов есть
# произвольная структура данных. Вам необходимо написать
# класс который будет описывать работу с этими файлами, а
# именно:
# 1) Запись в файл
# 2) Чтение из файла
# 3) Объединение данных из файлов в новый файл
# 4) Получить путь относительный путь к файлу
# 5) Получить абсолютный путь к файлу
#
def get_file_tools(my_file):
    """ Function creates an instance of the FileTools class.
    Actions: reading and writing to a file, merging files
    getting relative and absolute paths"""
    import os.path

    if os.path.exists(my_file):

        class FileTools:

            def __init__(self, file_1):
                self._file_1 = file_1

            def write_this(self, text):
                with open(self._file_1, 'w') as writer:
                    writer.write(text)

            def read_it(self):
                with open(self._file_1, 'r') as reader:
                    for line in reader:
                        print(line, end='')

            def merger(self, file_2):
                if os.path.exists(file_2):
                    new_file = 'new_example_json.json'
                    with open(self._file_1) as reader1, open(file_2) as reader2:
                        with open(new_file, 'w') as writer:
                            for line in reader1:
                                writer.write(line)
                            writer.write('\n')
                            for line in reader2:
                                writer.write(line)
                else:
                    print(f'File {file_2} doesn\'t exist')

            def abspath(self):
                import os
                print(f'{os.path.abspath(self._file_1)}')

            def relpath(self):
                import pathlib
                print(f'{pathlib.Path(self._file_1)}')

        return FileTools(my_file)
    else:
        print('File doesn\'t exist')

a = get_file_tools('example_json_1.json')
print(a.abspath())
a.merger('example_json_2.json')

# Задача-3
#
# Создайте класс который будет хранить параметры для
# подключения к физическому юниту(например switch). В своем
# списке атрибутов он должен иметь минимальный набор
# (unit_name, mac_address, ip_address, login, password).
# Вы должны описать каждый из этих атрибутов в виде гетеров и
# сеттеров(@property). У вас должна быть возможность
# получения и назначения этих атрибутов в классе.
