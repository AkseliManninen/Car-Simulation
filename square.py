class Square():

    """
    Instances of the class Square represent squares of a City.

    A square can contain a wall or be empty.
    """

    def __init__(self, is_wall=False):
        self.is_wall = is_wall

    # Returns a boolean value stating whether there is a wall in the square or not: boolean
    def is_wall_square(self):
        return self.is_wall

    # Sets a wall in this square, if possible.
    # If the square was not empty, the method fails to do anything.
    # Returns a boolean value indicating if the operation succeeded: boolean
    def set_wall(self):
        if self.is_wall_square() == False:
            self.is_wall = True
            return True
        else:
            return False

