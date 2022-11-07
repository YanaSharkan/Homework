from exceptions.operation_exception import OperationException
from exceptions.out_of_stock_exception import OutOfStockException
from input_output import InputOutput


class Shop:
    def __init__(self, storage):
        self._storage = storage
        self._operations = {
            '1': 'Show how many products left.',
            '2': 'Show seller\'s current profit for each product.',
            '3': 'Show total seller\'s profit.',
            '4': 'Order product.'
        }

    def _get_remainders(self):
        data = self._storage.read('products')
        for product in data:
            InputOutput.output_remainder(product)

    def _get_profit_per_products(self):
        orders = self._storage.read('orders')
        products = self._storage.read('products')
        for product in products:
            total = 0
            for order in orders:
                if order['product_number'] == product['product_number']:
                    total += order['price'] * order['quantity']

            InputOutput.output_profit_for_product(product['name'], total)

    def _total_profit(self):
        orders = self._storage.read('orders')
        total = 0
        for order in orders:
            total += order['price'] * order['quantity']

        InputOutput.output_total_profit(total)

    def _order_product(self):
        self._get_remainders()
        product_number, quantity = InputOutput.input_order_params()
        products = self._storage.read('products')
        product_to_order = None
        for product in products:
            if product['product_number'] == product_number:
                product_to_order = product

        if product_to_order and product_to_order['amount'] >= quantity:
            order = {
                'product_number': product_to_order['product_number'],
                'quantity': quantity,
                'price': product_to_order['price']
            }
            self._storage.add_record('orders', order)
            product_to_order['amount'] -= quantity
            self._storage.write('products', products)
            InputOutput.output_order_created()
        else:
            raise OutOfStockException()

    def choose_operations(self):
        print('-------------------------------------------------')
        for number in self._operations:
            print(f'{number}. {self._operations[number]}')

        operation = InputOutput.input_operation()
        self.perform_operation(operation)

    def perform_operation(self, operation):
        if operation == '1':
            self._get_remainders()
        elif operation == '2':
            self._get_profit_per_products()
        elif operation == '3':
            self._total_profit()
        elif operation == '4':
            self._order_product()
        else:
            raise OperationException()
        self.choose_operations()
