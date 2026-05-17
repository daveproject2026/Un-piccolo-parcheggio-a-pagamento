class Vehicle:
    def __init__(self, plate, vehicle_type):
        plate = plate.strip().upper()
        vehicle_type = vehicle_type.strip()

        if not plate:
            raise ValueError

        if not vehicle_type:
            raise ValueError
        
        if vehicle_type not in ("car", "motorcycle", "truck"):
            raise ValueError
        
        
        self.plate = plate
        self.vehicle_type = vehicle_type
        self.is_parked = False
        
    def park(self):
        if self.is_parked:
            raise RuntimeError
        self.is_parked = True
        
        
    
    def leave(self):
        if not self.is_parked:
            raise RuntimeError
        self.is_parked = False
        
        
        
            