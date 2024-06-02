from .atm_state import ATMState
from .has_card_state import HasCardState  # Assuming HasCardState is defined in a separate module
from abc import ABC, abstractmethod

class IdleState(ATMState):
    @abstractmethod
    def insert_card(self, atm, card):
        print("Card is inserted")
        atm.set_current_atm_state(HasCardState())
