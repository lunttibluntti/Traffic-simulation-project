from PyQt6 import QtWidgets, QtGui, QtCore
from direction import Direction


class VehicleGraphicsItem(QtWidgets.QGraphicsPolygonItem):
    """
    The class RobotGraphicsItem extends QGraphicsPolygonItem to link it together to the physical
    representation of a Robot. The QGraphicsPolygonItem handles the drawing, while the
    Robot knows its own location and status.
    """

    def __init__(self, vehicle, square_size):
        # Call init of the parent object
        super(VehicleGraphicsItem, self).__init__()

        # Do other stuff
        self.vehicle = vehicle
        self.square_size = square_size
        brush = QtGui.QBrush(1) # 1 for even fill
        self.setBrush(brush)
        self.constructVehicles()
        self.updateAll()


    def constructVehicles(self):
        """
        This method sets the shape of this item into a triangle.

        The QGraphicsPolygonItem can be in the shape of any polygon.
        We use triangles to represent robots, as it makes it easy to
        show the current facing of the robot.
        """
        # Create a new QPolygon object
        rectangle = QtGui.QPolygonF()

        rectangle.append(QtCore.QPointF(self.square_size / 4, 0))
        rectangle.append(QtCore.QPointF(self.square_size * 3 / 4, 0))
        rectangle.append(QtCore.QPointF(self.square_size * 3 / 4, self.square_size))
        rectangle.append(QtCore.QPointF(self.square_size / 4, self.square_size))




        # Set this newly created polygon as this Item's polygon.
        self.setPolygon(rectangle)

        # Set the origin of transformations to the center of the triangle.
        # This makes it easier to rotate this Item.
        self.setTransformOriginPoint(self.square_size/2, self.square_size/2)


    def updateAll(self):
        """
        Updates the visual representation to correctly resemble the current
        location, direction and status of the parent robot.
        """
        self.updatePosition()
        self.updateRotation()
        self.updateColor()


    def updatePosition(self):
        """
        Implement me!

        Update the coordinates of this item to match the attached robot.
        Remember to take in to account the size of the squares.

        A robot in the first (0, 0) square should be drawn at (0, 0).

        See: For setting the position of this GraphicsItem, see
        QGraphicsPolygonItem at https://doc.qt.io/qtforpython-5/PySide2/QtWidgets/QGraphicsPolygonItem.html
        and its parent class QGraphicsItem at https://doc.qt.io/qtforpython-5/PySide2/QtWidgets/QGraphicsItem.html

        For getting the location of the parent robot, look at the Robot-class
        in vehicle.py.
        """
        coordinates = self.vehicle.get_location()
        x = coordinates.x*self.square_size
        y = coordinates.y*self.square_size
        self.setPos(x, y)


    def updateRotation(self):
        """
        Implement me!

        Rotates this item to match the rotation of parent robot.
        A method for rotating can be found from QGraphicsItem at https://doc.qt.io/qtforpython-5/PySide2/QtWidgets/QGraphicsItem.html

        """
        facing = self.vehicle.get_facing()
        rotation = Direction.get_degrees(facing)
        self.setRotation(rotation)


    def updateColor(self):
        """
        Implement me!

        Draw broken robots in red, stuck robots in yellow and working robots in green.

        The rgb values of the colors must be the following:
        - red: (255, 0, 0)
        - yellow: (255, 255, 0)
        - green: (0, 255, 0)

        See: setBrush() at https://doc.qt.io/qtforpython-5/PySide2/QtWidgets/QAbstractGraphicsShapeItem.html
        and QBrush at https://doc.qt.io/qtforpython-5/PySide2/QtGui/QBrush.html
        and QColor at https://doc.qt.io/qtforpython-5/PySide2/QtGui/QColor.html

        Look at vehicle.py for checking the status of the robot.
        """
        blue = QtGui.QColor(0, 190, 255)
        brush1 = QtGui.QBrush(blue)
        red = QtGui.QColor(255, 0, 0)
        brush2 = QtGui.QBrush(red)
        self.setBrush(brush1)


