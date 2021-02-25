#
# class Car:
#     def __init__(self, brand, speed):
#
#         self.__brand = brand
#         self.__speed = speed
#
#     def set_speed(self, speed):
#         self.__speed = speed
#
#     def get_speed(self):
#         return self.__speed
#
#
# rama = Car('Ford', 100)
# rama.__speed = 1000
# print(rama.__speed)


class Car:
    def __init__(self, speed, color):
        self.__speed = speed
        self.__color = color

    def set_speed(self, value):
        self.__speed = value

    def get_speed(self):
        return self.__speed


    def set_color(self, value):
        self.__color = value

    def get_color(self):
        return self.__color

ford = Car(200, 'red')
honda = Car(250, 'blue')
audi = Car(300, 'black')

ford.set_speed(300)
ford.__speed=100
print(ford.get_speed())
print(ford.get_color())
