import unittest
from unittest.mock import MagicMock
import sys
sys.path.append('..')

from shop import Shop  # noqa: E402
from storage import Storage  # noqa: E402
from input_output import InputOutput  # noqa: E402


class ProfitPerProductTestCase(unittest.TestCase):
    _products = [
        {"product_number": 1, "name": "Hotwheels track",
         "price": 20, "amount": 5},
        {"product_number": 2, "name": "Hotwheels basic car",
         "price": 2, "amount": 35},
        {"product_number": 3, "name": "Hotwheels car's set",
         "price": 8, "amount": 10}
    ]
    _orders = [
        {'product_number': 1, 'quantity': 5, 'price': 20},
        {'product_number': 2, 'quantity': 15, 'price': 2}
    ]

    def _storage_return_value(self, storage_name):
        if storage_name == 'products':
            return self._products
        else:
            return self._orders

    def test_profit_per_product(self):
        storage = Storage()
        storage.read = MagicMock()
        storage.read.side_effect = self._storage_return_value
        InputOutput.output_profit_for_product = MagicMock()
        shop = Shop(storage)
        shop.choose_operations = MagicMock()
        shop.perform_operation('2')
        InputOutput.output_profit_for_product.assert_any_call(
            self._products[0]['name'], 100)
        InputOutput.output_profit_for_product.assert_any_call(
            self._products[1]['name'], 30)
        InputOutput.output_profit_for_product.assert_any_call(
            self._products[2]['name'], 0)
        shop.choose_operations.assert_called()
