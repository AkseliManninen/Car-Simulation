class Coordinates():

    def __init__(self, x, y):
        self.x = x    # the x coordinate
        self.y = y    # the y coordinate

    # Returns the x coordinate
    def get_x(self):
        return self.x

    # Returns the y coordinate
    def get_y(self):
        return self.y

    def __str__(self):
        """
        Returns a string of the form (X, Y) representing of the coordinate pair
        """
        return '({:.0f}, {:.0f})'.format(self.get_x(), self.get_y())