from enum import Enum

class ReservationType(Enum):
    HOURLY = 'Hourly'
    DAILY = 'Daily'

# Example usage
if __name__ == "__main__":
    # Accessing enum values
    print(ReservationType.HOURLY)
    print(ReservationType.DAILY)
