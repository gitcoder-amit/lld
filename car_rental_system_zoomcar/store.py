from typing import List
from products.vehicle import Vehicle
from products.vehicle_type import  VehicleType
from vehicle_inventory_management import VehicleInventoryManagement
from location import Location
from reservation import Reservation
from user import User

class Store:
    def __init__(self, store_id: int, store_location: Location):
        self.store_id = store_id
        self.inventory_management = None
        self.store_location = store_location
        self.reservations = []

    def get_vehicles(self, vehicle_type: VehicleType) -> List[Vehicle]:
        # Filtering logic can be added based on vehicle_type if needed
        return self.inventory_management.vehicles

    def set_vehicles(self, vehicles: List[Vehicle]):
        self.inventory_management = VehicleInventoryManagement(vehicles)

    def create_reservation(self, vehicle: Vehicle, user: User) -> Reservation:
        reservation = Reservation()
        reservation.create_reserve(user, vehicle)
        self.reservations.append(reservation)
        return reservation

    def complete_reservation(self, reservation_id: int) -> bool:
        for reservation in self.reservations:
            if reservation.reservation_id == reservation_id:
                reservation.complete_reserve()
                self.reservations.remove(reservation)
                return True
        return False

    # Additional methods for updating reservations can be added here

