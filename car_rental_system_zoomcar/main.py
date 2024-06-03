from user import User
from location import Location
from store import Store
from vehicle_rental_system import VehicleRentalSystem
# from Payment import Payment
from bill import Bill
from reservation import Reservation
from products.car import Car
from products.vehicle_type import VehicleType

def main():
    # Adding users, vehicles, and stores
    users = add_users()
    vehicles = add_vehicles()
    stores = add_stores(vehicles)

    # Creating a vehicle rental system
    rental_system = VehicleRentalSystem(stores, users)

    # 0. User comes
    user = users[0]

    # 1. User searches store based on location
    location = Location(pincode=403012, city="Bangalore", state="Karnataka", country="India")
    store = rental_system.get_store(location)

    # 2. Get all vehicles the user is interested in
    store_vehicles = store.get_vehicles(VehicleType.CAR)

    # 3. Reserving the particular vehicle
    reservation = store.create_reservation(store_vehicles[0], users[0])

    # 4. Generate the bill
    bill = Bill(reservation)

    # 5. Make payment
    payment = Payment()
    payment.pay_bill(bill)

    # 6. Trip completed, submit the vehicle and close the reservation
    store.complete_reservation(reservation.reservation_id)

def add_vehicles():
    vehicles = []

    vehicle1 = Car()
    vehicle1.vehicle_id = 1
    vehicle1.vehicle_type = VehicleType.CAR

    vehicle2 = Car()
    vehicle2.vehicle_id = 2
    vehicle2.vehicle_type = VehicleType.CAR

    vehicles.append(vehicle1)
    vehicles.append(vehicle2)

    return vehicles

def add_users():
    users = []

    user1 = User()
    user1.user_id = 1

    users.append(user1)

    return users

def add_stores(vehicles):
    stores = []

    store1 = Store()
    store1.store_id = 1
    store1.set_vehicles(vehicles)

    stores.append(store1)

    return stores

if __name__ == "__main__":
    main()
