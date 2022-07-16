import unittest
from code.car import Car
from random import randint

from code.elements.type_of_car import TypeOfCar

# Random order for tests runs. (Original is: -1 if x<y, 0 if x==y, 1 if x>y).
unittest.TestLoader.sortTestMethodsUsing = lambda _, x, y: randint(-1, 1)

class TestCar(unittest.TestCase):

    def setUp(self):
        """Method to prepare the test fixture. Run BEFORE the test methods."""
        self.new_car = Car()

    def tearDown(self):
        """Method to tear down the test fixture. Run AFTER the test methods."""
        pass

    def addCleanup(self, function, *args, **kwargs):
        """Function called AFTER tearDown() to clean resources used on test."""
        pass

    def test_drive(self):
        self.assertEqual(self.new_car.drive(), "driving")

    def test_default_type_of_car(self):
        self.assertEqual(self.new_car.type_of_car, TypeOfCar.UNIVERSAL)

if __name__.__contains__("__main__"):
    print(__doc__)
    unittest.main()