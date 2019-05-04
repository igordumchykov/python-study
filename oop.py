#! venv/bin/python3.6


class Person:

    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age

    def display_name(self):
        print(self.name)

    def display_age(self):
        print(self.age)

    def __str__(self):
        return self.name + ' ' + str(self.age)

    def __add__(self, other):
        name = self.name + ' and ' + other.name
        age = self.age + other.age
        return self.__class__(name, age)

    def print_all_fields(self):
        print(
            list(
                zip(
                    self.__dict__.keys(), self.__dict__.values()
                )
            )
        )


class Manager(Person):

    def __init__(self, name: str, age: int, bonus: int):
        print('Manager creation')
        super().__init__(name, age)
        self.bonus = bonus

    def __str__(self):
        return 'Manager ' + Person.__str__(self) + ', bonus: ' + str(self.bonus)

    def __getitem__(self, item):
        return item


from abc import ABCMeta, abstractmethod


class Super(metaclass=ABCMeta):
    def delegate(self):
        self.action()

    @abstractmethod
    def action(self):
        pass


class Provider(Super):
    def action(self):
        print("Provider: action")


class A:
    __X = 10

    def printX(self):
        print(self.__X)


class B:
    __X = 20

    def printX(self):
        print(self.__X)


class C(A, B):
    def printX(self):
        print(self.__X)


class D:

    def __init__(self, name):
        self.name = name

    def foo(self):
        print(self.name)

    @staticmethod
    def boo(a, b):
        print(a + b)


class ListInstance:
    """ Примесный класс, реализующий получение форматированной строки при вызове функций print() и str()
        с экземпляром в виде аргумента, через наследование метода __str__, реализованного здесь; отображает
        только атрибуты экземпляра; self – экземпляр самого нижнего класса в дереве наследования;
        во избежание конфликтов с именами атрибутов клиентских классов использует имена вида __X
    """

    def __str__(self):
        return '< Instance of % s, address % s:\n % s >' % (self.__class__.__name__, id(self), self.__attrnames())

    def __attrnames(self):
        result = ''
        for attr in sorted(self.__dict__):
            result += '\tname % s = % s\n' % (attr, self.__dict__[attr])
        return result


class Example(ListInstance):

    def __init__(self) -> None:
        self.data1 = 'food'


class Methods:

    @staticmethod
    def static():
        print("Static")

    @classmethod
    def cls(cls):
        print("Cls: ", cls)

    def simple(self):
        print("Simple: ", self)


if __name__ == '__main__':
    # p1 = Manager('Igor', 29, 100)
    # p2 = Person('Sasha', 30)
    #
    # p1.print_all_fields()
    #
    # p2.print_all_fields()

    # db = shelve.open('persondb')
    # for p in p1, p2:
    #     db[p.name] = p.age
    # db.close()
    # print(list(db.keys()))

    # p = Super()
    # p.action()

    # p = Manager('Igor', 29, 100)
    # print(p[1])

    # d = D('igor')
    # foo = d.foo
    #
    # f = D('sasha')
    #
    # D.foo(d)
    # D.foo(f)

    m1 = Methods()

    m1.static()
    m1.cls()
    m1.simple()

    print("=========")

    Methods.static()
    Methods.cls()
    Methods.simple(m1)

    print()
