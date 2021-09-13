import sys

from PyQt5.QtWidgets import QApplication
from gui import GUI

from city import *
from car import *
from car_image import *
from coordinates import *


def main():

    test_city = City(100, 100)

    global app
    app = QApplication(sys.argv)

    square_size = 8

    # Creating walls

    for i in range(37, 42):
        for j in range(47, 52):
            wall_coordinates = Coordinates(i, j)
            test_city.add_wall(wall_coordinates, i, j)

    for i in range(16, 21):
        for j in range(47, 52):
            wall_coordinates = Coordinates(i, j)
            test_city.add_wall(wall_coordinates,i,j)

    for i in range(58, 63):
        for j in range(47, 52):
            wall_coordinates = Coordinates(i, j)
            test_city.add_wall(wall_coordinates,i,j)

    for i in range(79, 84):
        for j in range(47, 52):
            wall_coordinates = Coordinates(i, j)
            test_city.add_wall(wall_coordinates,i,j)

    for i in range(0, 100):
        for j in range(0, 2):
            wall_coordinates = Coordinates(i, j)
            test_city.add_wall(wall_coordinates, i, j)

    for i in range(0, 2):
        for j in range(0, 100):
            wall_coordinates = Coordinates(i, j)
            test_city.add_wall(wall_coordinates, i, j)

    for i in range(98, 100):
        for j in range(0, 100):
            wall_coordinates = Coordinates(i, j)
            test_city.add_wall(wall_coordinates, i, j)

    for i in range(0, 100):
        for j in range(98, 100):
            wall_coordinates = Coordinates(i, j)
            test_city.add_wall(wall_coordinates, i, j)


    # Creating cars

    car_1 = Car(test_city, (80, 400), (120 ,200))
    car_image_1 = CarImage(car_1, square_size)
    test_city.add_car(car_1)
    test_city.add_car_image(car_image_1)

    car_2 = Car(test_city, (120, 200), (80, 400))
    car_image_2 = CarImage(car_2, square_size)
    test_city.add_car(car_2)
    test_city.add_car_image(car_image_2)

    car_3 = Car(test_city, (100, 100), (650, 150))
    car_image_3 = CarImage(car_3, square_size)
    test_city.add_car(car_3)
    test_city.add_car_image(car_image_3)

    car_4 = Car(test_city, (50, 100), (60, 150))
    car_image_4 = CarImage(car_4, square_size)
    test_city.add_car(car_4)
    test_city.add_car_image(car_image_4)

    car_5 = Car(test_city, (90, 600), (60, 600))
    car_image_5 = CarImage(car_5, square_size)
    test_city.add_car(car_5)
    test_city.add_car_image(car_image_5)

    gui = GUI(test_city, square_size)

    gui.show()

    sys.exit(app.exec_())

    # Any code below this point will only be executed after the gui is closed.

if __name__ == "__main__":
    main()

