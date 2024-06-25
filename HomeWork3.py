"""«адание:
–еализуйте программу, котора€ имитирует доступ к общему ресурсу с использованием механизма блокировки потоков.

 ласс BankAccount должен отражать банковский счет с балансом и методами дл€ пополнени€ и сн€ти€ денег. Ќеобходимо использовать механизм блокировки, чтобы избежать проблемы гонок (race conditions) при модификации общего ресурса.
"""

import threading

class BankAccount:
    def __init__(self, balance, lock, *args, **kwargs):
        super(BankAccount, self).__init__(*args, **kwargs)
        self.balance = balance
        self.lock = lock

    def withdraw(self, amount):
        with self.lock:
            self.balance -= amount
            print(f'Withdrew {amount}, new balance is {self.balance}')

    def deposit(self, amount):
        with self.lock:
            self.balance += amount
            print(f'Deposited {amount}, new balance is {self.balance}')


def deposit_task(account, amount):
    for _ in range(5):
        account.deposit(amount)


def withdraw_task(account, amount):
    for _ in range(5):
        account.withdraw(amount)


lock = threading.Lock()
account = BankAccount( 1500, lock=lock)

deposit_thread = threading.Thread(target=deposit_task, args=(account, 100))
withdraw_thread = threading.Thread(target=withdraw_task, args=(account, 150))

deposit_thread.start()
withdraw_thread.start()

deposit_thread.join()
withdraw_thread.join()

