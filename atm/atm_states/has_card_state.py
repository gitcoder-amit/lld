from .atm_state import ATMState
from .select_operation import SelectOperationState  # Assuming SelectOperationState is defined in a separate module
from abc import ABC, abstractmethod
from .idle_state import IdleState


class HasCardState(ATMState):
    def __init__(self):
        print("Enter your card pin number")

    @abstractmethod
    def authenticate_pin(self, atm, card, pin):
        is_correct_pin_entered = card.is_correct_pin_entered(pin)

        if is_correct_pin_entered:
            atm.set_current_atm_state(SelectOperationState())
        else:
            print("Invalid PIN Number")
            self.exit(atm)

    @abstractmethod
    def exit(self, atm):
        self.return_card()
        atm.set_current_atm_state(IdleState())
        print("Exit happens")

    @abstractmethod
    def return_card(self):
        print("Please collect your card")
