from reservation import Reservation

class Bill:
    def __init__(self, reservation: Reservation):
        self.reservation = reservation
        self.total_bill_amount = self.compute_bill_amount()
        self.is_bill_paid = False

    def compute_bill_amount(self) -> float:
        return 100.0

# Example usage
if __name__ == "__main__":
    from reservation import Reservation

    # Creating a sample reservation
    reservation = Reservation()

    # Creating a bill for the reservation
    bill = Bill(reservation)
    print(f"Total Bill Amount: {bill.total_bill_amount}")
