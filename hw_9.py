# Задача-1
# Реализовать дескриптор валидации для аттрибута email.
# Ваш дескриптор должен проверять формат email который вы пытаетесь назначить
import re

class EmailDescriptor:

    def __get__(self, instance, owner):
        return self.email

    def __set__(self, instance, value):
        regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$' #
        if re.search(regex, value):
            print("Valid Email")
            self.email = value
        else:
            raise AttributeError('Invalid Email')

class MyClass:
    email = EmailDescriptor()


my_class = MyClass()
my_class.email = "validemail@gmail.com"

my_class.email = "novalidemail"
# Raised Exception


# Задача-2
# Реализовать синглтон метакласс(класс для создания классов синглтонов).

class Singleton(type):
    cache = {}
    def __call__(instance, *args, **kwargs):
        if instance not in Singleton.cache:
            Singleton.cache[instance] = super().__call__(*args, **kwargs)
            return Singleton.cache[instance]
        else:
            return Singleton.cache[instance]


class MyClass(metaclass=Singleton):
    pass


c = MyClass()
b = MyClass()
assert id(c) == id(b)


# Задача-3
# реализовать дескриптор IngegerField(), который будет хранить уникальные
# состояния для каждого класса где он объявлен

class IngegerField:

    def __get__(self, instance, owner):
        return instance._number

    def __set__(self, instance, value):
        instance._number = value


class Data:
    number = IngegerField()


data_row = Data()
new_data_row = Data()

data_row.number = 5
new_data_row.number = 10
print(data_row.number)

assert data_row.number != new_data_row.number


# Задача4
# Необходимо создать модели работы со складскими запасами товаров и процесса оформления заказа этих товаров.
# Cписок требований:
# 1) Создайте товар с такими свойствами, как имя(name), подробные сведения(description or details),
# количество на складе(quantity), доступность(availability), цена(price).

# Добавить к этой задаче дескриптор для аттрибута цена.
# При назначении цены товара будет автоматически добавлен НДС 20%
# При получении цены товара, цена возврщается уже с учетом НДС
class VAT:

    def __get__(self, instance, owner):
        return instance._price * 1.2

    def __set__(self, instance, value):
        instance._price = value


class Product:
    _warehouse = {}

    def __init__(self, name, details, quantity, price, category=None):
        self._name = name
        self._details = details
        self._quantity = self.add_to_warehouse(quantity)
        self._price = price
        self._availability = self.get_availb()

    price = VAT()

    @property
    def name(self):
        return self._name

    @property
    def quantity(self):
        return self._warehouse[self.name]

    def get_availb(self):
        if self.quantity > 0:
            return True
        else:
            return False

# 2) Добавить товар на склад
    def add_to_warehouse(self, quantity):
        if self.name in self._warehouse:
            self._warehouse[self.name] += quantity
        else:
            self._warehouse[self.name] = quantity
        print(f'Product {self.name} {quantity} added to warehouse')
        self.get_availb()
        self._update_quantity(self._warehouse[self.name])
        return self._warehouse[self.name]

    def _update_quantity(self, quantity):
        self._quantity = quantity
        return self._quantity

    def get_total_price(self, quantity):
        return quantity * self.price

# 3) Удалить товар со склада
    def remove_from_warehouse(self, quantity=None):
        if self.name in self._warehouse:
            if quantity is None:
                print(f'Product {self.name} removed from warehouse')
                self._warehouse[self.name] = 0
            elif quantity <= self.quantity:
                print(f'Product {self.name} {quantity} removed from warehouse')
                self._warehouse[self.name] -= quantity
            else:
                print(f'Product {self.name} {quantity} cannot be removed from warehouse')
                return 0
        self.get_availb()
        self._update_quantity(self._warehouse[self.name])

# 4) Распечатать остаток товара по его имени
    def __str__(self):
        return f'{self.quantity}'

# 5) Распечатать остаток всех товаров
    @classmethod
    def get_all_product_quantity(cls):
        print(cls._warehouse)

# 7) Распечатать список товаров с заданной категорией
    @classmethod
    def get_all_product(cls):
        print(cls.__name__, ':', [key for key in cls._warehouse])


# 6) Товар может принадлежать к категории
class Clothes(Product):
    _warehouse = {}

# 8 ) Корзина для покупок, в которой может быть много товаров с общей ценой.
class Basket:

    def __init__(self, product, quantity):
        self._all_total_price = 0
        self._product = product
        self._basket = {}
        self.quantity = self.check_quantity(product, quantity)
        self.total_price = self.get_total_price(product, self.quantity)
        self._basket[product.name] = {'quantity': self.quantity, 'price': self.total_price}

    def check_quantity(self, product, quantity):
        if product.get_availb:
            if quantity <= product.quantity:
                return quantity
        return None

    def get_total_price(self, product, quantity):
        if self.quantity == 0:
            return 0
        else:
            return product.get_total_price(quantity)

    def get_all_total_price(self):
        self._all_total_price = 0
        for product in self._basket:
            self._all_total_price += int(self._basket[product]['price'])
        return self._all_total_price

# 9) Добавить товары в корзину (вы не можете добавлять товары, если их нет в наличии)
    def add_to_basket(self, product, quantity):
        if product.name in self._basket:
            if not self.check_quantity(product, (quantity + self._basket[product.name]['quantity'])) is None:
                print(f'Product {product.name} {quantity} added to basket')
                self._basket[product.name]['quantity'] += quantity
                self._basket[product.name]['price'] = self.get_total_price(product,
                                                                           self._basket[product.name]['quantity'])
            else:
                print(f"Only {product.quantity - self._basket[product.name]['quantity']}")
        else:
            if not self.check_quantity(product, quantity) is None:
                print(f'Product {product.name} {quantity} added to basket')
                self._basket[product.name] = {'quantity': quantity, 'price': self.get_total_price(product, quantity)}
            else:
                print(f'Only {product.quantity}')

# 10) Распечатать элементы корзины покупок с ценой и общей суммой
    def basket_info(self):
        print(f'Items:')
        print('-' * 20)
        for product in self._basket:
            print(f'{product}: {self._basket[product]}', sep='\n')
        print('-'*20)
        print(f'Total price:', end=' ')
        print(f'{self.get_all_total_price()}')

# 11) Оформить заказ и распечатать детали заказа по его номеру
    def create_order(self):
         self._order = Order(self)

    def checkout(self):
        self._order.checkout()


# 12) Позиция заказа, созданная после оформления заказа пользователем.
from datetime import datetime

class Order:
    counter = 1
    orders = {}

    def __init__(self, basket):
        self.order_id = Order.counter
        self.basket = basket
        self.date_purchased = self.get_update_date()
        self.get_info()
        self.status = False
        Order.orders[self.order_id] = self.basket._basket
        Order.counter += 1

    def get_update_date(self):
        return datetime.now()

    def get_info(self):
        print(f'Order id : {self.order_id}')
        self.basket.basket_info()


    def checkout(self):
        if self.status:
            print(f'Order is already closed')
        else:
            for product in Order.orders[self.order_id]:
                item = 'quantity'
                Product.remove_from_warehouse(self.basket._product, self.basket._basket[product][item])

            self.status = True
            print(f'Date : {self.get_update_date()}')
            self.get_info()

# Он будет иметь идентификатор заказа(order_id), дату покупки(date_purchased), товары(items), количество(quantity)
# 13) После оформления заказа количество товара уменьшается на количество товаров из заказа


product_1 = Product('cup', 'blue', 50, 1.5)
product_2 = Product('toy', 'soft', 5, 5)
product_3 = Clothes('dress', 'midi', 5, 8)
product_4 = Clothes('dress2', 'midi2', 15, 6)


product_1.add_to_warehouse(60)
product_1.remove_from_warehouse(10)

basket1 = Basket(product_1, 30)
basket2 = Basket(product_2, 5)
basket3 = Basket(product_2, 5)

basket1.add_to_basket(product_2, 1)
basket1.add_to_basket(product_3, 1)
basket1.add_to_basket(product_4, 10)
print('-'*80)
basket1.create_order()
basket1.add_to_basket(product_4, 1)
basket1.create_order()
basket2.create_order()
print('-'*80)
basket2.checkout()
basket2.checkout()