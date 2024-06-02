from enum import Enum

class TransactionType(Enum):
    CASH_WITHDRAWAL = "Cash Withdrawal"
    BALANCE_CHECK = "Balance Check"

    @staticmethod
    def show_all_transaction_types():
        for transaction_type in TransactionType:
            print(transaction_type.value)
