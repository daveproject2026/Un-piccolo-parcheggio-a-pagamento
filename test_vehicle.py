import unittest
from vehicle import Vehicle


class VehicleTest(unittest.TestCase):

    def test_new_vehicle_has_correct_attributes(self):
        v = Vehicle("AB123", "car")
        self.assertEqual(v.plate, "AB123")
        self.assertEqual(v.vehicle_type, "car")

    def test_new_vehicle_is_not_parked(self):
        v = Vehicle("AB123", "car")
        self.assertFalse(v.is_parked)

    def test_constructor_normalizes_plate_to_uppercase(self):
        v = Vehicle("ab123", "car")
        self.assertEqual(v.plate, "AB123")

    def test_constructor_strips_whitespace(self):
        v = Vehicle("  ab123  ", " car ")
        self.assertEqual(v.plate, "AB123")
        self.assertEqual(v.vehicle_type, "car")

    def test_constructor_rejects_empty_plate(self):
        with self.assertRaises(ValueError):
            Vehicle("   ", "car")

    def test_constructor_rejects_empty_vehicle_type(self):
        with self.assertRaises(ValueError):
            Vehicle("AB123", "   ")

    def test_constructor_rejects_unknown_vehicle_type(self):
        with self.assertRaises(ValueError):
            Vehicle("AB123", "bicycle")