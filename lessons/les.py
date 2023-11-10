# инкапсуляция,Абстракция, git clone
# уровни защиты
# публичная 0, _защищенная:protected,скрытая __
# полиморфизм, наследование
# super()

class Bank:
    def __init__(self, fullname, money, key):
        self.fullname = fullname
        self.__money = money
        self._password = key

    def __mon(self):
        money = int(input('введи счет: '))
        self.__money += money

    def mon1(self):
        self.__mon()

    def __str__(self):
        return f'{self.fullname, self.__money}'

    # def getpass(self):
    #     print(self._password)
    #
    # def setpass(self, p):
    #     self._password = p
    @property
    def nameis(self):
        return (self._password)

    @nameis.setter
    def nameis(self, name):
        self._password = name


beka = Bank('bekbolot', 0, '2525')
print(beka)
print(beka.nameis)
beka.nameis = '9990'
print(beka.nameis)


# beka.mon1()
# beka._password = '1111'
# beka.age = 20
# beka._Bank__money = 77777777
# __ = _Classname__name
# beka.__money = 10000000000
# print(dir(beka))
# # print(beka.__money)
# print(beka.age)
# print(beka)
#

class Tea:
    def __init__(self, name):
        self.name = name

    def start(self):
        print('поставил чай ')
        self.__start2()
        self.__cup()
        self._stop()

    def __start2(self):
        print('нагрев воды ')

    def __cup(self):
        print('чай кипит')

    def _stop(self):
        print('выкл')


beko = Tea('beko')
# beko.start()
# beko._stop()
