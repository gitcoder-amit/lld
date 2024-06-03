from datetime import datetime
from enum import Enum
from user import User
from products.vehicle import Vehicle
from location import Location
from reservation_status import ReservationStatus
from reservation_type import ReservationType

class Reservation:
    def __init__(self):
        self.reservation_id = None
        self.user = None
        self.vehicle = None
        self.booking_date = None
        self.date_booked_from = None
        self.date_booked_to = None
        self.from_time_stamp = None
        self.to_time_stamp = None
        self.pickup_location = None
        self.drop_location = None
        self.reservation_type = None
        self.reservation_status = None

    def create_reserve(self, user: User, vehicle: Vehicle) -> int:
        # Generate new id
        self.reservation_id = 12232
        self.user = user
        self.vehicle = vehicle
        self.reservation_type = ReservationType.DAILY
        self.reservation_status = ReservationStatus.SCHEDULED

        return self.reservation_id

# Example usage
if __name__ == "__main__":
    from user import User
    from products.vehicle import Vehicle
    from location import Location

    # Create sample user and vehicle
    user = User(user_id=1, name="John Doe", email="johndoe@example.com")
    vehicle = Vehicle(vehicle_id=1, vehicle_number=12345, company_name="Toyota", model_name="Camry")
    
    # Create a reservation
    reservation = Reservation()
    reservation_id = reservation.create_reserve(user, vehicle)
    
    print(f"Reservation ID: {reservation_id}")
