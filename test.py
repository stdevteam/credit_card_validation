import unittest
from main import CreditCard


class TestCreditCard(unittest.TestCase):

    def setUp(self):
        self.valid_inputs = ("4253625879615786", "5123-4567-8912-3456", "4123356789123456")
        self.invalid_inputs = ("61234-567-8912-3456", "5133-3367-8912-3456", "5123 - 3567 - 8912 - 3456")

    def test_valid_card_numbers(self):
        for valid_input in self.valid_inputs:
            credit_card = CreditCard(valid_input)
            self.assertTrue(credit_card.is_valid())
            print("Valid:", credit_card.is_valid(), credit_card.card_number)

    def test_invalid_card_numbers(self):
        for invalid_input in self.invalid_inputs:
            credit_card = CreditCard(invalid_input)
            self.assertFalse(credit_card.is_valid())
            print("Invalid:", credit_card.is_valid(), credit_card.card_number)

if __name__ == '__main__':
    unittest.main()
