    def test_park_marks_vehicle_as_parked(self):
        v = Vehicle("AB123", "car")
        v.park()
        self.assertTrue(v.is_parked)

    def test_park_already_parked_raises(self):
        v = Vehicle("AB123", "car")
        v.park()
        with self.assertRaises(RuntimeError):
            v.park()

    def test_leave_marks_vehicle_as_not_parked(self):
        v = Vehicle("AB123", "car")
        v.park()
        v.leave()
        self.assertFalse(v.is_parked)

    def test_leave_when_not_parked_raises(self):
        v = Vehicle("AB123", "car")
        with self.assertRaises(RuntimeError):
            v.leave()

    def test_park_and_leave_cycle(self):
        v = Vehicle("AB123", "car")
        v.park()
        v.leave()
        v.park()
        self.assertTrue(v.is_parked)