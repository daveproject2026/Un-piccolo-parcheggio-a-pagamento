import unittest
from vehicle import Vehicle

class TestVehicle(unittest.TestCase):
    
    def test_create_vehicle(self):
        v = Vehicle("AB123", "car")
        self.assertEqual("AB123", v.plate)
        self.assertEqual("car", v.vehicle_type)
        