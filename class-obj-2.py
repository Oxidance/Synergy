class Turtle(object):
    axis_x = 0
    axis_y = 0
    num = 1

    def __init__(self, x, y, s):
        self.axis_x = x
        self.axis_y = y
        self.num = s

    def go_up(self):
        self.axis_y += self.num

    def go_down(self):
        self.axis_y -= self.num

    def go_left(self):
        self.axis_x -= self.num

    def go_right(self):
        self.axis_x += self.num

    def evolve(self):
        self.num += 1

    def degrade(self):
        self.num -= 1
        if self.num <= 0:
            print('Ошибка')

    def count_moves(self, x2, y2):
        a = abs(x2 - self.axis_x) // self.num
        b = abs(y2 - self.axis_y) // self.num
        return a + b


tortilla = Turtle(13, 36, 2)

tortilla.go_up()
tortilla.go_left()
print(tortilla.axis_y, tortilla.axis_x)
tortilla.evolve()
print(tortilla.num)
tortilla.go_down()
print(tortilla.axis_y)
tortilla.degrade()
tortilla.go_right()
print(tortilla.axis_x, tortilla.num)
print(tortilla.count_moves(19, 43))