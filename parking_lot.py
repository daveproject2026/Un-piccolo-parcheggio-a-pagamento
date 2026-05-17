class ParkingLot:
    def __init__(self, capacity):
        if capacity <= 0:
            raise ValueError

        self.capacity = capacity
        self._vehicles = {}

    def count_vehicles(self):
        return len(self._vehicles)

    def enter(self, vehicle):

        if len(self._vehicles) >= self.capacity:
            raise RuntimeError

        if vehicle.plate in self._vehicles:
            raise RuntimeError

        vehicle.park()
        self._vehicles[vehicle.plate] = vehicle
        
        
    def is_full(self):
        return self.count_vehicles() == self.capacity
            
    def available_spots(self):
        return self.capacity - self.count_vehicles()
    
    def has_vehicle(self, plate):
         return plate.strip().upper() in self._vehicles
            