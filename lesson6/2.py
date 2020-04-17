class Road:
    def __init__(self, length, width):
        self._length = length
        self._width = width

    def result(self, m, thickness):
        return self._length * self._width * m * thickness / 1000


road = Road(5000, 20)
print(int(road.result(25, 5)), 'т')
