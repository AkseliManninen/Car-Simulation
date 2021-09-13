from PyQt5 import QtWidgets, QtCore

# Imports for drawing
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QBrush, QPen, QColor
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap

class GUI(QtWidgets.QMainWindow):

    def __init__(self, city, square_size):
        super().__init__()
        self.city = city
        self.setCentralWidget(QtWidgets.QWidget()) # QMainWindown must have a centralWidget to be able to add layouts
        self.horizontal = QtWidgets.QHBoxLayout() # Horizontal main layout
        self.centralWidget().setLayout(self.horizontal)
        self.square_size = square_size
        self.init_window()
        self.draw_squares()


        # Set a timer to call the update function periodically
        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.update_all)
        self.timer.start(20)


    def init_window(self):
        """
        Sets up the window.
        """
        self.setGeometry(300, 100, 900, 900)
        self.setWindowTitle('Traffic Simulation')
        self.show()

        # Add a scene for drawing 2d objects
        self.scene = QtWidgets.QGraphicsScene()
        self.scene.setSceneRect(0, 0, 800, 800)

        # Add a view for showing the scene
        self.view = QtWidgets.QGraphicsView(self.scene, self)
        self.view.adjustSize()
        self.view.show()
        self.horizontal.addWidget(self.view)
        self.scene.setBackgroundBrush(QColor(156, 211, 219))

    # Draws (100 x 100) squares
    # If square is wall, color is yellow, if square is road color is gray

    def draw_squares(self):

        pen = QPen(Qt.NoPen)

        for x in range(100):
            for y in range(100):
                if self.city.squares[x][y].is_wall:
                    brush = QBrush(QColor(249, 224, 141)) # Sand (249, 224, 141) Retro (101, 13, 137)

                else:
                    brush = QBrush(QColor(50, 50, 50)) # Asphalt (50,50,50) Retro (32, 13, 58)

                rect = QGraphicsRectItem(x * self.square_size, y * self.square_size, self.square_size, self.square_size)
                rect.setBrush(brush)
                rect.setPen(pen)
                self.scene.addItem(rect)

    # Removes all cars from scene
    def remove_old_drawings(self):
        for item in self.scene.items():
            if item.__class__ == QGraphicsPixmapItem:
                self.scene.removeItem(item)

    # Adds cars to scene
    def draw_cars(self):
        for car_image in self.city.car_images:
            car_image.car.update_velocity()
            car_on_scene = self.scene.addPixmap(car_image.image)
            car_on_scene.setPos(car_image.car.location[0], car_image.car.location[1])

            angle = car_image.car.rotate()

            if angle != "zero_velocity":
                car_on_scene.setRotation(angle)

            car_image.car.location = (car_image.car.location[0]+car_image.car.velocity_x, car_image.car.location[1]+car_image.car.velocity_y)

    # Draws goals
    def draw_goals(self):
        for car in self.city.cars:
            goal_image = QPixmap('gasoline.png').scaledToHeight(30)
            goal = self.scene.addPixmap(goal_image)
            goal.setPos(car.goal[0] - 15, car.goal[1] - 15)

    # Draws everything by calling other methods
    def update_all(self):
        self.remove_old_drawings()
        self.draw_cars()
        self.draw_goals()




