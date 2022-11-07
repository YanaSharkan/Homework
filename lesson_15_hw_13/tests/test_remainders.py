import unittest
from unittest.mock import MagicMock
import sys
sys.path.append('..')

from shop import Shop  # noqa: E402
from storage import Storage  # noqa: E402
from input_output import InputOutput  # noqa: E402


class RemaindersTestCase(unittest.TestCase):

    def test_get_remainders(self):
        products = [
            {"product_number": 1, "name": "Hotwheels track",
             "price": 20, "amount": 5},
            {"product_number": 2, "name": "Hotwheels basic car",
             "price": 2, "amount": 35}
        ]
        storage = Storage()
        storage.read = MagicMock(return_value=products)
        InputOutput.output_remainder = MagicMock()
        shop = Shop(storage)
        shop.choose_operations = MagicMock()
        shop.perform_operation('1')
        InputOutput.output_remainder.assert_any_call(products[0])
        InputOutput.output_remainder.assert_any_call(products[1])
        shop.choose_operations.assert_called()
