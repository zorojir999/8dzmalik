# модули в пайтон
import turtle
import colorama, art

# 1 встроенные модули
import random
# 1 импорт всего модуля import namefile
import math
# print(math.pi)
# 2 from namefile import
from math import e as num_e

# num_e=e
print(num_e)

# 2 собвственные модули
from les import Bank

# print(Bank.mro())
p = Bank('beka', 1_000_000, '1234rdfewr')
# print(p)

p2 = random.randint(1, 9)
# print(p)

# 3 внешние модули
# venv-виртуальное окружение
# зависимости

import colorama
from art import tprint

print(colorama.Back.WHITE)
print('')
print(colorama.Fore.BLACK)
print(colorama.Style.BRIGHT)
tprint('1234rwefw3')
tprint('MY BEST""" GROUP')

