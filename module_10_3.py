import threading
from time import sleep
from random import randint


class Bank:

    def __init__(self):
        self.balance = 0
        self.lock = threading.Lock()

    def deposit(self):
        for i in range(100):
            quant = randint(50, 500)
            self.balance += quant
            if self.balance >= 500 and self.lock.locked():
                self.lock.release()
            sleep(0.001)
            print(f'Пополнение: {quant}. Баланс: {self.balance}')

    def take(self):
        for i in range(100):
            quant = randint(50, 500)
            print(f'Запрос на {quant}')
            if quant <= self.balance:
                self.balance -= quant
                print(f'Снятие: {quant}. Баланс: {self.balance}')
            else:
                print(f'Запрос отклонен, недостаточно средств')
                self.lock.acquire()
            sleep(0.001)

bk = Bank()

th1 = threading.Thread(target=Bank.deposit, args=(bk,))
th2 = threading.Thread(target=Bank.take, args=(bk,))

th1.start()
th2.start()
th1.join()
th2.join()


print(f'Итоговый баланс: {bk.balance}')

