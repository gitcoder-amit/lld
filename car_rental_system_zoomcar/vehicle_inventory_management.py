from typing import List
from products.vehicle import Vehicle

class VehicleInventoryManagement:
    def __init__(self, vehicles: List[Vehicle]):
        self._vehicles = vehicles

    @property
    def vehicles(self) -> List[Vehicle]:
        # Implement filtering logic if needed
        return self._vehicles

    @vehicles.setter
    def vehicles(self, vehicles: List[Vehicle]):
        self._vehicles = vehicles