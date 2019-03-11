import re
from itertools import groupby

pattern = re.compile(r'^[4,5,6]\d{3}(\d{4}|-\d{4}){3}')


class CreditCard:
    def __init__(self, card_number):
        self.card_number = card_number

    def count_consecutive(self, card_number):
        """
        max consecutive of each number
        :param card_number: 
        :return: max_consecutive
        """
        return max(len(list(g)) for _, g in groupby(card_number))

    def is_valid(self):
        """
        checks is the pattern match with number and max_consecutive < 4 
        :return: bool 
        """
        if pattern.fullmatch(self.card_number) and self.count_consecutive(self.card_number.replace('-', '')) < 4:
            return True
        else:
            return False
