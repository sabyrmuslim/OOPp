class Bank:
    def __init__(self,name,balance):
        self.name = name
        self.balance = balance
        
    def moneyX(self):
        money = input("добавить счёт:")
        self.balance += money
        print(f"клиент добавил деньги.Счет:{self.balance}")
    