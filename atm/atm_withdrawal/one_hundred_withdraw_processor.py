from .cash_withdrawal_processor import CashWithdrawProcessor

class OneHundredWithdrawProcessor(CashWithdrawProcessor):
    def __init__(self, next_cash_withdraw_processor=None):
        super().__init__(next_cash_withdraw_processor)

    def withdraw(self, atm, remaining_amount):
        required = remaining_amount // 100
        balance = remaining_amount % 100

        if required <= atm.get_no_of_one_hundred_notes():
            atm.deduct_one_hundred_notes(required)
        elif required > atm.get_no_of_one_hundred_notes():
            atm.deduct_one_hundred_notes(atm.get_no_of_one_hundred_notes())
            balance += (required - atm.get_no_of_one_hundred_notes()) * 100

        if balance != 0:
            print("Something went wrong")
