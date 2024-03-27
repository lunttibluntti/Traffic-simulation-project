from coordinates import *
from vehicleai import VehicleAI
import random


class Vehicle:

    def __init__(self, world):

        self.license_plate = self.set_license_plate()
        self.world = world
        self.location = None
        self.facing = None
        self.start_goal = random.sample([1, 2, 3, 4], 2)
        self.start = self.start_goal[0]
        self.goal = self.start_goal[1]
        self.start_coordinates = self.randomize_start()
        self.goal_coordinates = self.randomize_goal()
        self.ai = self.set_ai()
        self.first_turn = 0
        self.last_square = None
        self.finished = 0
        self.where_to_go = []
        self.moved_last_turn = True

    def did_not_move(self):
        self.moved_last_turn = False

    def did_move_last_turn(self):
        return self.moved_last_turn

    def set_finished(self):
        self.finished = 1

    def is_finished(self):
        if self.finished == 1:
            return True
        else:
            return False

    def set_facing(self, headed):
        self.facing = headed

    def randomize_start(self):
        start_coordinates = []
        if self.start == 1:
            i = random.randint(1, 9)
            j = 1
            start_coordinates.append(i)
            start_coordinates.append(j)
            start_coordinates = Coordinates(start_coordinates[0], start_coordinates[1])
        if self.start == 2:
            i = random.randint(self.world.get_width() - 9, self.world.get_width() - 1)
            j = 0
            start_coordinates.append(i)
            start_coordinates.append(j)
            start_coordinates = Coordinates(start_coordinates[0], start_coordinates[1])
        if self.start == 3:
            i = self.world.get_width() - 1
            j = random.randint(self.world.get_height() - 5, self.world.get_height() - 1)
            start_coordinates.append(i)
            start_coordinates.append(j)
            start_coordinates = Coordinates(start_coordinates[0], start_coordinates[1])
        if self.start == 4:
            i = random.randint(1, 9)
            j = self.world.get_height() - 1
            start_coordinates.append(i)
            start_coordinates.append(j)
            start_coordinates = Coordinates(start_coordinates[0], start_coordinates[1])

        self.location = start_coordinates
        return start_coordinates

    def randomize_goal(self):
        goal_coordinates = []
        if self.goal == 1:
            i = random.randint(0, 2)
            j = random.randint(0, 2)
            goal_coordinates.append(i)
            goal_coordinates.append(j)
            goal_coordinates = Coordinates(goal_coordinates[0], goal_coordinates[1])
        if self.goal == 2:
            i = random.randint(self.world.get_width() - 3, self.world.get_width() - 1)
            j = random.randint(0, 2)
            goal_coordinates.append(i)
            goal_coordinates.append(j)
            goal_coordinates = Coordinates(goal_coordinates[0], goal_coordinates[1])
        if self.goal == 3:
            i = random.randint(self.world.get_width() - 3, self.world.get_width() - 1)
            j = random.randint(self.world.get_height() - 3, self.world.get_height() - 1)
            goal_coordinates.append(i)
            goal_coordinates.append(j)
            goal_coordinates = Coordinates(goal_coordinates[0], goal_coordinates[1])
        if self.goal == 4:
            i = random.randint(2, 4)
            j = random.randint(self.world.get_height() - 3, self.world.get_height() - 1)
            goal_coordinates.append(i)
            goal_coordinates.append(j)
            goal_coordinates = Coordinates(goal_coordinates[0], goal_coordinates[1])

        self.goal = goal_coordinates
        return goal_coordinates

    def get_start(self):
        return self.start

    def get_goal(self):
        return self.goal

    def get_start_coordinates(self, start_coordinates):
        return self.start_coordinates

    def get_goal_coordinates(self, goal_coordinates):
        return self.goal_coordinates

    def set_license_plate(self):

        chars = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        nums = '0123456789'
        letters = ''
        numbers = ''
        for c in range(3):
            letters += random.choice(chars)

        for c in range(3):
            numbers += random.choice(nums)
        self.license_plate = letters + numbers
        return self.license_plate

    def get_license_plate(self):

        return self.license_plate

    def get_world(self):

        return self.world

    def get_location(self):

        return self.location

    def get_location_square(self):

        return self.get_world().get_square(self.get_location())

    def get_facing(self):

        return self.facing

    def set_world(self, world, location, facing):

        target_square = world.get_square(location)
        if not target_square.is_empty():
            return False
        else:
            self.world = world
            self.location = location
            self.facing = facing
            return True

    def set_ai(self):
        return VehicleAI(self, self.goal_coordinates)

    def spin(self, headed):

        self.facing = headed

    def take_turn(self):
        if self.finished == 0:
            self.where_to_go = self.ai.steering()

            ahead = self.get_location().get_neighbor(self.facing)
            ahead_square = self.get_world().get_square(ahead)
            if ahead_square.vehicle:
                return
            for i in self.where_to_go:
                if self.move(i):
                    return
            third_direction = Direction.get_next_clockwise(Direction.get_next_clockwise(self.where_to_go[1]))
            if self.move(third_direction):
                return

    def move(self, try_to_go):

        """Making sure the vehicles are able to leave the starting areas"""
        if self.first_turn < 10:
            ahead = self.get_location().get_neighbor(self.facing)
            ahead_square = self.get_world().get_square(ahead)
            current_square = self.get_location_square()
            if ahead_square.is_empty():
                self.last_square = current_square
                current_square.remove_vehicle()
                self.location = ahead
                ahead_square.set_vehicle(self)
                self.first_turn += 1
                return True
            return True

        if try_to_go == self.facing:
            wall_ahead = self.get_location().get_relative(try_to_go, 2)
            wall_ahead_square = self.get_world().get_square(wall_ahead)
            if wall_ahead_square.is_wall_square():
                return False
            target = self.get_location().get_neighbor(self.facing)
            current_square = self.get_location_square()
            target_square = self.get_world().get_square(target)
            if self.move_square(current_square, target_square, target):
                return True
            else:
                return False

        if try_to_go == Direction.get_next_clockwise(self.facing):
            target = self.get_location().get_neighbor(try_to_go)
            current_square = self.get_location_square()
            target_square = self.get_world().get_square(target)
            if target_square.is_empty():
                self.spin(try_to_go)
            if self.move_square(current_square, target_square, target):
                return True
            else:
                return False

        if try_to_go == Direction.get_next_counter_clockwise(self.facing):
            target = self.get_location().get_relative(try_to_go, 2)
            target = target.get_relative(self.facing, 1)
            should_you_turn = target.get_relative(self.facing, 1)
            check_turn_square = self.get_world().get_square(should_you_turn)
            if not check_turn_square.is_wall_square():
                return False
            current_square = self.get_location_square()
            target_square = self.get_world().get_square(target)
            if target_square.is_empty():
                self.spin(try_to_go)
            if self.move_square(current_square, target_square, target):
                return True
            else:
                return False

        self.moved_last_turn = False

    def move_square(self, current_square, target_square, target):
        if target_square.is_empty():
            self.last_square = current_square
            current_square.remove_vehicle()
            self.location = target
            target_square.set_vehicle(self)
            self.moved_last_turn = True
            return True
        else:
            self.moved_last_turn = False
            return False

    def __str__(self):
        return self.get_license_plate() + ' at location ' + str(self.get_location())
