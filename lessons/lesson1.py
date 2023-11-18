# 1код  2git
# ООП
# классы
from les4 import Bank

# print(sum1(1, 8))

a = 1, 1.2, '1', True, False, [], {}, (), None
a1 = ()
print(a1)


def sum1(a, b):
    return a + b

sum1(6,8)
#
class Human:
    # атрибуты уровня класса
    # свойства класса
    head = True
    #магический метод
    #конструктор класса

    def __init__(self, name, age):
        self.name = name
        self.age = age

    # метод
    def tprint(self):
        print(self.name,self.head,self.age)

    def summ(self):
        print(self.name)
        self.age += 15

    def __str__(self):
        return f'{self.name},{self.age}'

    def __len__(self):
        return len(self.name)

    def __abs__(self):
        return abs(self.age)

# экземпляры класса,обьекты класса
human = Human('beka',-20)
human2 = Human('ЭРбол',-18)
human3 = Human('Малик',-16)
# print(len())
human.tprint()
human2.tprint()
human3.tprint()
# human.summ()
# human.summ()
human.tprint()

# print(human.__abs__())
print(abs(human))
# print(Human.tprint(self=human))