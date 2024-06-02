from .atm_state import ATMState
from .idle_state import IdleState
from ..atm_withdrawal.two_thousand_withdraw_processor import TwoThousandWithdrawProcessor
from ..atm_withdrawal.five_hundred_withdraw_processor import FiveHundredWithdrawProcessor
from ..atm_withdrawal.one_hundred_withdraw_processor import OneHundredWithdrawProcessor

class CashWithdrawalState(ATMState):
    def __init__(self):
        print("Please enter the Withdrawal Amount")

    def cash_withdrawal(self, atm_object, card, withdrawal_amount_request):
        if atm_object.get_atm_balance() < withdrawal_amount_request:
            print("Insufficient fund in the ATM Machine")
            self.exit(atm_object)
        elif card.get_bank_balance() < withdrawal_amount_request:
            print("Insufficient fund in the your Bank Account")
            self.exit(atm_object)
        else:
            card.deduct_bank_balance(withdrawal_amount_request)
            atm_object.deduct_atm_balance(withdrawal_amount_request)

            # using chain of responsibility for this logic, how many 2k Rs notes, how many 500 Rs notes etc, has to be withdrawal
            withdraw_processor = TwoThousandWithdrawProcessor(
                FiveHundredWithdrawProcessor(
                    OneHundredWithdrawProcessor(None)
                )
            )

            withdraw_processor.withdraw(atm_object, withdrawal_amount_request)
            self.exit(atm_object)

    def exit(self, atm_object):
        self.return_card()
        atm_object.set_current_atm_state(IdleState())
        print("Exit happens")

    def return_card(self):
        print("Please collect your card")
