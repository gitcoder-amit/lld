from abc import ABC, abstractmethod

class ATMState(ABC):
    @abstractmethod
    def insert_card(self, atm, card):
        pass

    @abstractmethod
    def authenticate_pin(self, atm, card, pin):
        pass

    @abstractmethod
    def select_operation(self, atm, card, txn_type):
        pass

    @abstractmethod
    def cash_withdrawal(self, atm, card, withdraw_amount):
        pass

    @abstractmethod
    def display_balance(self, atm, card):
        pass

    @abstractmethod
    def return_card(self):
        pass

    @abstractmethod
    def exit(self, atm):
        pass