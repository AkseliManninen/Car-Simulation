from PyQt5 import QtWidgets
from PyQt5.QtGui import QPixmap

class CarImage(QtWidgets.QGraphicsItem):

    def __init__(self, car, square_size):
        super(CarImage, self).__init__()
        self.car = car
        self.square_size = square_size
        self.update_location()
        self.image = QPixmap('red_car.png').scaledToHeight(12)

    # Updates location of CarImage to be same as Car's location scaled by square size
    def update_location(self):

        x = self.car.location[0] * self.square_size
        y = self.car.location[1] * self.square_size

        self.setX(x)
        self.setY(y)


