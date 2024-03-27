from square import Square
from gui import GUI


class Map:

    def __init__ (self, width, height):

        self.x = width
        self.y = height

        self.gui = None

        self.squares = [None] * width
        for x in range(self.get_width()):      # stepper
            self.squares[x] = [None] * height
            for y in range(self.get_height()):    # stepper
                self.squares[x][y] = Square()    # fixed value
        self.vehicles = []                        # container
        self.turn = 0
        self.end = 0

    def set_gui(self, gui):
        self.gui = gui

    def end_simulation(self):
        self.end = 1

    def get_width(self):
        """
        Returns width of the world in squares: int
        """
        return len(self.squares)


    def get_height(self):
        """
        Returns the height of the world in squares: int
        """
        return len(self.squares[0])


    def add_vehicle(self, vehicle, location, facing):

        if vehicle.set_world(self, location, facing):
            self.vehicles.append(vehicle)
            self.get_square(location).set_vehicle(vehicle)
            return True
        else:
            return False


    def add_wall(self, location):

        return self.get_square(location).set_wall()


    def get_square(self, coordinates):

        if self.contains(coordinates):
            return self.squares[coordinates.get_x()][coordinates.get_y()]
        else:
            return Square(True)


    def get_number_of_vehicles(self):

        return len(self.vehicles)


    def get_vehicle(self, turn_number):

        if 0 <= turn_number < self.get_number_of_vehicles():
            return self.vehicles[turn_number]
        else:
            return None


    def get_next_vehicle(self):

        if self.get_number_of_vehicles() < 1:
            return None
        else:
            return self.vehicles[self.turn]


    def next_vehicle_turn(self):

        current = self.get_next_vehicle()
        if current is not None:
            self.turn = (self.turn + 1) % self.get_number_of_vehicles()
            if not current.is_finished():
                current.take_turn()
            else:
                current.did_not_move()

    def next_full_turn(self):

        e = 0
        k = 0
        for i in self.vehicles:
            if not i.did_move_last_turn():
                k += 1
            e += 1
        if k == e:
            self.gui.exit_program()

        for count in range(self.get_number_of_vehicles()):
            self.next_vehicle_turn()


    def contains(self, coordinates):

        x_coordinate = coordinates.get_x()
        y_coordinate = coordinates.get_y()
        return 0 <= x_coordinate < self.get_width() and 0 <= y_coordinate < self.get_height()


    def get_vehicles(self):

        return self.vehicles[:]
