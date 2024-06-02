class ATMRoom:
    def __init__(self):
        self.atm = None
        self.user = None

    def initialize(self):
        self.atm = ATM.get_atm_object()
        self.atm.set_atm_balance(3500, 1, 2, 5)
        self.user = self.create_user()

    def create_user(self):
        user = User()
        return user

    def main(self):
        self.initialize()
        self.atm.print_current_atm_status()
        self.atm.get_current_atm_state().insert_card(self.atm, self.user.card)
        self.atm.get_current_atm_state().authenticate_pin(self.atm, self.user.card, 112211)
        self.atm.get_current_atm_state().select_operation(self.atm, self.user.card, TransactionType.CASH_WITHDRAWAL)
        self.atm.get_current_atm_state().cash_withdrawal(self.atm, self.user.card, 2700)
        self.atm.print_current_atm_status()

if __name__ == "__main__":
    atm_room = ATMRoom()
    atm_room.main()