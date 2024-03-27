import unittest

import main
from map import Map
from vehicle import Vehicle
from coordinates import Coordinates
from direction import Direction


class Test(unittest.TestCase):

    def test_world(self):
        self.test_world = Map(150, 100)
        main.world_builder(150, 100, self.test_world)

        self.assertEqual(True, self.test_world.get_square(Coordinates(75, 10)).is_wall_square(),
                         "Square at location (75, 10) should be a wall.")
        print("Test passed!")

    def test_vehicle(self):

        self.test_world = Map(150, 100)
        main.world_builder(150, 100, self.test_world)

        test_vehicle = Vehicle(self.test_world)
        if test_vehicle.get_start() == 1:
            headed = Direction.EAST
            test_vehicle.set_facing(headed)
        if test_vehicle.get_start() == 2:
            headed = Direction.WEST
            test_vehicle.set_facing(headed)
        if test_vehicle.get_start() == 3:
            headed = Direction.NORTH
            test_vehicle.set_facing(headed)
        if test_vehicle.get_start() == 4:
            headed = Direction.EAST
            test_vehicle.set_facing(headed)
        self.test_world.add_vehicle(test_vehicle, test_vehicle.start_coordinates, test_vehicle.facing)

        self.test_world.next_full_turn()

        self.assertLess(10, test_vehicle.ai.distance_to_goal(),
                        "Vehicle should be within 10 squares of its goal when the simulation stops running.")
        print("Test passed!")


if __name__ == "__main__":
    unittest.main()
