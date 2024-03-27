import math
from direction import Direction


class VehicleAI:

    def __init__(self, body, goal):

        self.body = body
        self.goal = goal
        self.begin = 0
        self.world = self.body.get_world()

    """
    Steering method for vehicles. Determines the 2 most desired directions and returns them to Vehicle class as a list.
    The direction with the longer distance to the goal is prioritized.
    """

    def steering(self):
        headed = []
        location = self.body.get_location()
        if self.distance_to_goal() <= 2:
            self.body.set_finished()
            headed.append(Direction.NORTH)
            headed.append(Direction.SOUTH)
            return headed
        if self.goal != location:
            distance_x = self.goal.get_x() - location.get_x()
            distance_y = self.goal.get_y() - location.get_y()
            if math.fabs(distance_x) >= math.fabs(distance_y):
                if distance_x >= 0:
                    headed.append(Direction.EAST)
                    if distance_y >= 0:
                        headed.append(Direction.SOUTH)
                    else:
                        headed.append(Direction.NORTH)
                if distance_x < 0:
                    headed.append(Direction.WEST)
                    if distance_y < 0:
                        headed.append(Direction.NORTH)
                    else:
                        headed.append(Direction.SOUTH)

                return headed
            else:
                if distance_y >= 0:
                    headed.append(Direction.SOUTH)
                    if distance_x >= 0:
                        headed.append(Direction.EAST)
                    else:
                        headed.append(Direction.WEST)
                if distance_y < 0:
                    headed.append(Direction.NORTH)
                    if distance_x < 0:
                        headed.append(Direction.WEST)
                    else:
                        headed.append(Direction.EAST)

                return headed


    """
    Calculate the Euclidean distance between `pos` and `goal`
    """
    def distance_to_goal(self):

        pos = self.body.get_location()
        return ((pos.get_x() - self.goal.get_x()) ** 2 + (pos.get_y() - self.goal.get_y()) ** 2) ** 0.5





