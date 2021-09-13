from square import Square

class City():

    def __init__ (self, width, height):

        self.squares = [None] * width

        for x in range(self.get_width()):      # stepper
            self.squares[x] = [None] * height
            for y in range(self.get_height()):    # stepper
                self.squares[x][y] = Square()    # fixed value

        self.cars = []                        # containers
        self.car_images = []
        self.walls = []

    # Adds a car to city.cars
    def add_car(self, car):
        self.cars.append(car)

    # Adds a car_image to city.car_images
    def add_car_image(self, car_image):
        self.car_images.append(car_image)

    # Adds a wall
    def add_wall(self, location, i, j):
        self.walls.append((i,j))
        return self.get_square(location).set_wall()

    # Returns width of the city
    def get_width(self):
        return len(self.squares)

    # Returns height of the city
    def get_height(self):
        return len(self.squares[0])

    # Returns the square that is located at the given location.
    def get_square(self, coordinates):
        if self.contains(coordinates):
            return self.squares[coordinates.get_x()][coordinates.get_y()]
        else:
            return Square(True)

    # Returns if the city contains the coordinates
    def contains(self, coordinates):
        x_coordinate = coordinates.get_x()
        y_coordinate = coordinates.get_y()
        return 0 <= x_coordinate < self.get_width() and 0 <= y_coordinate < self.get_height()


