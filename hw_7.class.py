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
        print(self._ip)

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
import os.path

class FileTools:

    def __init__(self, file_1):
        self._file_1 = file_1

    def write_this(self, text):
        with open(self._file_1, 'w') as writer:
            writer.write(text)

    def read_it(self):
        try:
            with open(self._file_1, 'r') as reader:
                for line in reader:
                    print(line, end='')
        except FileNotFoundError:
            print('File does not exist')

    def merger(self, file_2):
        try:
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
        except FileNotFoundError:
            print('File does not exist')

    def abspath(self):
        print(f'{os.path.abspath(self._file_1)}')

    def relpath(self):
        import pathlib
        print(f'{pathlib.Path(self._file_1)}')


c = FileTools('example_json_1.json')
c.abspath()
c.read_it()
#c.merger('example_json_2.json')

# Задача-3
#
# Создайте класс который будет хранить параметры для
# подключения к физическому юниту(например switch). В своем
# списке атрибутов он должен иметь минимальный набор
# (unit_name, mac_address, ip_address, login, password).
# Вы должны описать каждый из этих атрибутов в виде гетеров и
# сеттеров(@property). У вас должна быть возможность
# получения и назначения этих атрибутов в классе.

class Unit:

    def __init__(self, unit_name, mac_address, ip_address, login, password):
        self._unit_name = unit_name
        self._mac_address = mac_address
        self._ip_address = ip_address
        self._login = login
        self._password = password

    @property
    def unit_name(self):
        return self._unit_name
    @property
    def mac_address(self):
        return self._mac_address
    @property
    def ip_address(self):
        return self._ip_address
    @property
    def login(self):
        return self._login
    @property
    def password(self):
        return self._password

    @unit_name.setter
    def unit_name(self, new_unit_name):
        self._unit_name = new_unit_name
    @mac_address.setter
    def mac_address(self, new_mac_address):
        self._mac_address = new_mac_address
    @ip_address.setter
    def ip_address(self, new_ip_address):
        self._ip_address = new_ip_address
    @login.setter
    def login(self, new_login):
        self._login = new_login
    @password.setter
    def password(self, new_password):
        self._password = new_password

unit = Unit('my_name', '00.1A.3F', '10.11.12.13', 'my_login', 'my_password')
print(unit.login)
