from PyQt6 import QtWidgets, QtCore, QtGui
from coordinates import Coordinates
from vehicle_gui import VehicleGraphicsItem
from starting_window import VehicleGenerationWindow


class GUI(QtWidgets.QMainWindow):

    def __init__(self, map, square_size):
        super().__init__()

        self.setCentralWidget(QtWidgets.QWidget()) # QMainWindow must have a centralWidget to be able to add layouts
        self.horizontal = QtWidgets.QHBoxLayout() # Horizontal main layout
        self.centralWidget().setLayout(self.horizontal)
        self.world = map
        self.square_size = square_size
        self.map = map

        self.map.set_gui(self)

        self.added_vehicles = []
        self.init_window()
        self.init_buttons()

        self.add_SquareGraphicsItems()
        self.add_VehicleGraphicsItems()
        self.update_vehicles()

        # Set a timer to call the update function periodically
        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.update_vehicles)
        self.timer.start(100) # Milliseconds

        self.timer_move = QtCore.QTimer()


    def get_vehicleItems(self):

        items = []
        for item in self.scene.items():
            if type(item) is VehicleGraphicsItem:
                items.append(item)
        return items

    def init_buttons(self):
        """
        Adds buttons to the window and connects them to their respective functions
        See: QPushButton at https://doc.qt.io/qtforpython-5/PySide2/QtWidgets/QPushButton.html
        """

        start_button = QtWidgets.QPushButton("start simulation")
        start_button.clicked.connect(self.start_timer)
        self.horizontal.addWidget(start_button)

        exit_button = QtWidgets.QPushButton("exit simulation")
        exit_button.clicked.connect(self.exit_program)
        self.horizontal.addWidget(exit_button)


    def start_timer(self):

        self.timer.timeout.connect(self.world.next_full_turn)
        self.timer_move.setInterval(100000)
        self.timer_move.start()

    def pause_timer(self):
        self.timer_move.stop()

    def exit_program(self):
        self.close()

    def update_vehicles(self):
        """
        Iterates over all robot items and updates their position to match
        their physical representations in the robot world.
        """
        for vehicle_item in self.get_vehicleItems():
            vehicle_item.updateAll()


    def init_window(self):
        """
        Sets up the window.
        """
        self.setGeometry(600, 100, 1800, 1200)
        self.setWindowTitle('Traffic_Simulation')
        self.show()

        # Add a scene for drawing 2d objects
        self.scene = QtWidgets.QGraphicsScene()
        self.scene.setSceneRect(0, 0, 1000, 800)

        # Add a view for showing the scene
        self.view = QtWidgets.QGraphicsView(self.scene, self)
        self.view.adjustSize()
        self.view.show()
        self.horizontal.addWidget(self.view)

    def add_SquareGraphicsItems(self):

        width = self.map.get_width()
        height = self.map.get_height()
        x = 0
        y = 0
        color1 = QtGui.QColor(20, 20, 20)
        brush1 = QtGui.QBrush(color1)
        pen1 = QtGui.QPen(color1)
        color2 = QtGui.QColor(211, 211, 211)
        brush2 = QtGui.QBrush(color2)
        pen2 = QtGui.QPen(color2)

        while x < width:
            while y < height:
                coordinates = Coordinates(x, y)
                s = self.map.get_square(coordinates)
                square = self.square_size
                square = QtWidgets.QGraphicsRectItem(x * square, y * square, square, square)
                if s.is_wall_square():
                    square.setBrush(brush1)
                    square.setPen(pen1)
                    self.scene.addItem(square)
                else:
                    square.setBrush(brush2)
                    square.setPen(pen2)
                    self.scene.addItem(square)
                y += 1
            y = 0
            x += 1

    def add_VehicleGraphicsItems(self):

        vehicles = self.map.get_vehicles()
        for i in vehicles:
            if i not in self.added_vehicles:
                vehicle = VehicleGraphicsItem(i, self.square_size)
                self.scene.addItem(vehicle)
                self.added_vehicles.append(i)
