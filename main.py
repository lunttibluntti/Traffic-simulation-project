import sys
from PyQt6.QtWidgets import QApplication

from gui import GUI
from starting_window import VehicleGenerationWindow

from map import *
from vehicle import *
from vehicleai import *


def world_builder(x, y, world):
    """
    Generates predetermined road map. For the sake of this project not meant to be changed. That's why the world builder
    looks clunky. I did try to construct it in a way that it would be relatively easy to scale as long as x/y ratio is
    being kept the same.
    """

    i = 0
    e = 0
    while i <= x:
        while e <= y:
            if i < 10 and e < 10:
                pass
            elif i < 10 and e >= y - 10:
                pass
            elif i >= x - 10 and e < 10:
                pass
            elif i >= x - 10 and e >= y - 10:
                pass
            # pitkä vaaka
            elif (y / 2) - 2 < e < (y / 2) + 1:
                pass
            # pitkä vaaka oikea ylä
            elif (y / 3) - 2 < e < (y / 3) and (x / 3 + x / 3) < i:
                pass
            #pitkä vaaka vasen ylä
            elif (y / 3) - 2 < e < (y / 3) and i < (x / 3):
                pass
            # vasen ala vaaka
            elif 9 < i < (x / 2 + 1) and y - 3 < e:
                pass
            # ala keski pysty
            elif (x / 3) - 2 < i < (x / 3) + 1:
                pass
            # vasen ala pysty
            elif (x / 2) - 2 < i < (x / 2) + 1 and (y / 2) - 2 < e < y - 2:
                pass
            # vasen ala reuna pysty
            elif i < 2 and (y / 2) - 2 < e < y - 2:
                pass
            # oikea ala pysty
            elif (x / 3 + x / 3 - 2) < i < (x / 3 + x / 3 + 1):
                pass
            # oikea ala reuna pysty
            elif x - 3 < i < x and (y / 2) - 2 < e < y - 10:
                pass
            # oikea ala vaaka reuna
            elif (x / 3 + x / 3) < i < x - 10 and y - 3 < e < y:
                pass
            # oikea ala vaaka
            elif (y - y / 3) + 8 < e < (y - y / 3) + 10:
                pass
            # vasen ylä vaaka
            elif i < (x / 3) and e < 2:
                pass
            # vasen ylä pysty
            elif (y / 3) < i < (y / 3) + 2 and 1 < e < (y / 2) + 1:
                pass
            # vasen ylä reuna pysty
            elif i < 2 and 1 < e < (y / 3) - 2:
                pass

            # oikea ylä vaaka
            elif (x / 3 + x / 3) < i and e < 2:
                pass
            # oikea ylä pysty
            elif (3 * x / 4) + 9 < i < (3 * x / 4) + 11 and 1 < e < (y / 2) + 1:
                pass
            # oikea ylä reuna
            elif x - 3 < i < x and 9 < e < (y / 3) - 2:
                pass
            else:
                wall = Coordinates(i, e)
                world.add_wall(wall)
            e += 1
        e = 0
        i += 1


"""
The main function of the whole program. Sets up and constructs the map, adds the amount of vehicles requested by the 
user and sets up the GUI class instance.
"""


def main():
    x = 150
    y = 100
    i = 0
    e = 0
    world = Map(x, y)
    world_builder(x, y, world)
    k = 0

    # Every Qt application must have one instance of QApplication.
    # Use global to prevent crashing on exit

    global app
    app = QApplication(sys.argv)
    starting_window = VehicleGenerationWindow()
    starting_window.show()

    app.exec()

    j = int(starting_window.get_how_many())



    while k < j:
        vehicle = Vehicle(world)
        headed = Direction.EAST
        if vehicle.get_start() == 1:
            headed = Direction.EAST
            vehicle.set_facing(headed)
        if vehicle.get_start() == 2:
            headed = Direction.WEST
            vehicle.set_facing(headed)
        if vehicle.get_start() == 3:
            headed = Direction.NORTH
            vehicle.set_facing(headed)
        if vehicle.get_start() == 4:
            headed = Direction.EAST
            vehicle.set_facing(headed)
        start_square = world.get_square(vehicle.start_coordinates)
        if start_square.is_empty():
            world.add_vehicle(vehicle, vehicle.start_coordinates, headed)
        else:
            k -= 1
        k += 1

    print(world.get_number_of_vehicles())

    gui = GUI(world, 8)

    # Start the Qt event loop. (i.e. make it possible to interact with the gui)
    sys.exit(app.exec())

    # Any code below this point will only be executed after the gui is closed.


if __name__ == "__main__":
    main()
