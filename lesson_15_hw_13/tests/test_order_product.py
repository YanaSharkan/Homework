import unittest
from unittest.mock import MagicMock
import sys
sys.path.append('..')

from shop import Shop  # noqa: E402
from storage import Storage  # noqa: E402
from input_output import InputOutput  # noqa: E402
from exceptions.out_of_stock_exception import OutOfStockException  # noqa: E402


class OrderProductTestCase(unittest.TestCase):
    _product = [
        {"product_number": 1,
         "name": "Hotwheels track",
         "price": 20, "amount": 5}
    ]

    def test_order_product_success(self):
        order = {"product_number": 1,
                 "quantity": 5,
                 "price": 20}
        storage = Storage()
        storage.read = MagicMock(return_value=self._product)
        InputOutput.input_order_params = MagicMock(return_value=(1, 5))
        InputOutput.output_remainder = MagicMock()
        InputOutput.output_order_created = MagicMock()
        storage.add_record = MagicMock()
        storage.write = MagicMock()
        shop = Shop(storage)
        shop.choose_operations = MagicMock()
        shop.perform_operation('4')
        InputOutput.output_order_created.assert_called()
        shop.choose_operations.assert_called()
        storage.write.assert_called_with('products', self._product)
        storage.add_record.assert_called_with('orders', order)

    def test_order_product_error(self):
        storage = Storage()
        storage.read = MagicMock(return_value=self._product)
        InputOutput.input_order_params = MagicMock(return_value=(2, 5))
        InputOutput.output_remainder = MagicMock()
        InputOutput.output_order_created = MagicMock()
        storage.add_record = MagicMock()
        storage.write = MagicMock()
        shop = Shop(storage)
        shop.choose_operations = MagicMock()
        with self.assertRaises(OutOfStockException) as context:
            shop.perform_operation('4')
        self.assertTrue('Product was not find' == context.exception.message)
        InputOutput.output_order_created.assert_not_called()
        shop.choose_operations.assert_not_called()
        storage.add_record.assert_not_called()
        storage.write.assert_not_called()
