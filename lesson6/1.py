import time


class TrafficLight:
    __color = ['красный', 'желтый', 'зеленый']

    def running(self):
        while True:
            print(self.__color[0])
            time.sleep(7)
            print(self.__color[1])
            time.sleep(2)
            print((self.__color[2]))
            time.sleep(4)
            print(self.__color[1])
            time.sleep(2)


test_light = TrafficLight()
test_light.running()
