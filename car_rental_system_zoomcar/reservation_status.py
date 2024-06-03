from enum import Enum

class ReservationStatus(Enum):
    SCHEDULED = 'Scheduled'
    IN_PROGRESS = 'In Progress'
    COMPLETED = 'Completed'
    CANCELED = 'Canceled'

# Example usage
if __name__ == "__main__":
    # Accessing enum values
    print(ReservationStatus.SCHEDULED)
    print(ReservationStatus.IN_PROGRESS)
    print(ReservationStatus.COMPLETED)
    print(ReservationStatus.CANCELED)
