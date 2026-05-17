import unittest
from vehicle import Vehicle
from parking_lot import ParkingLot

class ParkingLotTest(unittest.TestCase):

    def test_new_lot_has_capacity_and_zero_vehicles(self):
        p = ParkingLot(10)
        self.assertEqual(p.capacity, 10)
        self.assertEqual(p.count_vehicles(), 0)
    
    def test_constructor_rejects_invalid_capacity(self):
        with self.assertRaises(ValueError):
            ParkingLot(0)
        with self.assertRaises(ValueError):
            ParkingLot(-1)
    
    def test_enter_adds_vehicle_and_marks_it_parked(self):
        p = ParkingLot(10)
        v = Vehicle("AB123", "car")
        p.enter(v)
        p.count_vehicles()
        self.assertEqual(p.count_vehicles(), 1)
        self.assertTrue(v.is_parked)
            
    def test_enter_with_duplicate_plate_raises(self):
        p = ParkingLot(10)

        v1 = Vehicle("AB123", "car")
        v2 = Vehicle("AB123", "car")

        p.enter(v1)

        with self.assertRaises(RuntimeError):
            p.enter(v2)
        
    def test_enter_when_full_raises(self):
        p = ParkingLot(1)
        v = Vehicle("AB123", "car")
        p.enter(v)
        with self.assertRaises(RuntimeError):
            p.enter(v)
        
    def test_is_full_and_available_spots_track_count(self):
        p = ParkingLot(2)
        v1 = Vehicle("AB123", "car")
        p.enter(v1)
        self.assertFalse(p.is_full())
        self.assertEqual(p.available_spots(), 1)
        v2 = Vehicle("BC123", "car")
        p.enter(v2)
        self.assertTrue(p.is_full())
        self.assertEqual(p.available_spots(), 0)
    
    def test_has_vehicle_returns_true_for_present_false_for_absent(self):
        p = ParkingLot(1)
        v1 = Vehicle("AB123", "car")
        p.enter(v1)
        self.assertTrue(p.has_vehicle("AB123"))
        self.assertFalse(p.has_vehicle("ZZ999"))