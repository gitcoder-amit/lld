class Card:
    PIN_NUMBER = 112211

    def __init__(self):
        self.card_number = None
        self.cvv = None
        self.expiry_date = None
        self.holder_name = None
        self.bank_account = None

    def is_correct_pin_entered(self, pin):
        return pin == Card.PIN_NUMBER

    def get_bank_balance(self):
        if self.bank_account:
            return self.bank_account.balance
        return 0  # Return 0 if bank account is not set

    def deduct_bank_balance(self, amount):
        if self.bank_account:
            self.bank_account.withdrawal_balance(amount)

    def set_bank_account(self, bank_account):
        self.bank_account = bank_account
