import fire
from utils import CreditCard


class BankCards:
    def __init__(self):
        self._input_lins_count = None
        self.card_numbers = []

    def input_cards_count(self, count):
        self._input_lins_count = count
        for i in range(count):
            print("You must enter {} card numbers".format(count-i))
            self.card_number(input())
        self.validate_inputs()

    def card_number(self, num):
        self.card_numbers.append(num)

    def validate_inputs(self):
        for card_num in self.card_numbers:
            credit_card = CreditCard(card_num)
            msg = "The credit card number {} is {}"
            if credit_card.is_valid():
                print(msg.format(credit_card.card_number, "valid"))
            else:
                print(msg.format(credit_card.card_number, "invalid"))

    def check_card_number(self, num):
        self._input_lins_count = 1
        self.card_numbers.append(num)
        self.validate_inputs()

if __name__ == '__main__':
    fire.Fire(BankCards)
