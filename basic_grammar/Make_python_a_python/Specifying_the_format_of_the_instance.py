class Coord(object):
    def __init__(self, x, y):
        super().__init__()
        self.x, self.y = x, y

    def __str__(self):
        return "({}, {})".format(self.x, self.y)


if __name__ == '__main__':
    point = Coord(2, 3)
    print(point)
    