class MoneyBox:
    def __init__(self, capacity):
        # конструктор с аргументом – вместимость копилки
        self.capacty = capacity
        self.money = 0


    def can_add(self, v):
        # True, если можно добавить v монет, False иначе
        return self.money + v <= self.capacty


    def add(self, v):
        # положить v монет в копилку
        if self.can_add(v):
            self.money += v

x = MoneyBox(10)
x.add(5)
x.add(11)