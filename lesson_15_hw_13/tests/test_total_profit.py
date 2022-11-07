import unittest
from unittest.mock import MagicMock
import sys
sys.path.append('..')

from shop import Shop  # noqa: E402
from storage import Storage  # noqa: E402
from input_output import InputOutput  # noqa: E402


class TotalProfitTestCase(unittest.TestCase):

    def test_total_profit(self):
        storage = Storage()
        storage.read = MagicMock(return_value=[
            {'product_number': 1, 'quantity': 5, 'price': 20},
            {'product_number': 2, 'quantity': 15, 'price': 2}
        ])
        InputOutput.output_total_profit = MagicMock()
        shop = Shop(storage)
        shop.choose_operations = MagicMock()
        shop.perform_operation('3')
        InputOutput.output_total_profit.assert_called_with(130)
        shop.choose_operations.assert_called()
