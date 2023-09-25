class box_office(object):
    cash = 0

    def __init__(self, c):
        self.cash = c

    def top_up(self, x):
        self.cash += x

    def count_1000(self):
        return self.cash // 1000

    def take_away(self, y):
        self.cash -= y
        if self.cash < 0:
            print('Ошибка')


money = box_office(23900)
money.top_up(140)
print(money.cash)
print(money.count_1000())
money.take_away(1500)
print(money.cash)
money.take_away(50000)


