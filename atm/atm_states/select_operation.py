from .atm_state import ATMState
from .cash_withdrawal_state import CashWithdrawalState
from .check_balance_state import CheckBalanceState
from ..transaction_type import TransactionType  # Assuming TransactionType is defined in a separate module
from .cash_withdrawal_state import CashWithdrawalState
from .check_balance_state import CheckBalanceState

class SelectOperationState(ATMState):
    def __init__(self):
        self.show_operations()

    def select_operation(self, atm_object, card, txn_type):
        if txn_type == TransactionType.CASH_WITHDRAWAL:
            atm_object.set_current_atm_state(CashWithdrawalState())
        elif txn_type == TransactionType.BALANCE_CHECK:
            atm_object.set_current_atm_state(CheckBalanceState())
        else:
            print("Invalid Option")
            self.exit(atm_object)

    def exit(self, atm_object):
        self.return_card()
        atm_object.set_current_atm_state(IdleState())
        print("Exit happens")

    def return_card(self):
        print("Please collect your card")

    def show_operations(self):
        print("Please select the Operation")
        TransactionType.show_all_transaction_types()
