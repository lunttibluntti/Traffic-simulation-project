class Square:
    """
    The class Square represents a single square in a robot world.
    A square can contain either a wall or a robot or it can be empty.
    """

    def __init__(self, is_wall=False):
        """
        Creates a new square. Initially there is no robot in the square.

        Parameter is_wall_square is a boolean value stating whether there is a wall in the square or not: boolean
        """
        self.vehicle = None     # most-recent holder (None if no robot in square)
        self.is_wall = is_wall  # flag (one-way currently, since walls can not be removed


    def get_vehicle(self):
        """
        Returns the robot in the square or None if there is no robot in the square: Robot
        """
        return self.vehicle



    def is_wall_square(self):
        """
        Returns a boolean value stating whether there is a wall in the square or not: boolean
        """
        return self.is_wall


    def is_empty(self):
        """
        Returns a boolean value stating whether the square is empty (A square is empty if it does not contain a wall or a robot) or not: boolean
        """
        return not self.is_wall_square() and self.vehicle is None


    def set_vehicle(self, vehicle):
        """
        Marks the square as containing a robot, if possible.
        If the square was not empty, the method fails to do anything.

        Parameter robot is the robot to be placed in this square: Robot

        Returns a boolean value indicating if the operation succeeded: boolean
        """
        if self.is_empty():
            self.vehicle = vehicle
            return True
        else:
            return False


    def set_wall(self):
        if self.is_empty():
            self.is_wall = True
            return True
        else:
            return False

    def remove_vehicle(self):
        removed_vehicle = self.get_vehicle()
        self.vehicle = None
        return removed_vehicle

