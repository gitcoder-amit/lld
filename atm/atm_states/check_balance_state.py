from .atm_state import ATMState
from .idle_state import IdleState  # Assuming IdleState is defined in a separate module

class CheckBalanceState(ATMState):
    def __init__(self):
        pass

    def display_balance(self, atm, card):
        print("Your Balance is:", card.get_bank_balance())
        self.exit(atm)

    def exit(self, atm_object):
        self.return_card()
        atm_object.set_current_atm_state(IdleState())
        print("Exit happens")

    def return_card(self):
        print("Please collect your card")
