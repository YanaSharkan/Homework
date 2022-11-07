class InputOutput:

    @staticmethod
    def input_operation():
        return input('Which operation you want to choose? ')

    @staticmethod
    def input_order_params():
        product_number = int(
            input('Enter number of product you would like to buy: ')
        )
        quantity = int(input('Enter quantity of product: '))
        return product_number, quantity

    @staticmethod
    def output_order_created():
        print('Order created!')

    @staticmethod
    def output_total_profit(total):
        print(f'{total} is total profit.')

    @staticmethod
    def output_profit_for_product(product_name, total):
        print(
            'Total profit for product {0} is {1}'.format(product_name, total)
        )

    @staticmethod
    def output_remainder(product):
        print('{0}. {1} - {2}.'.format(
            product['product_number'],
            product['name'],
            product['amount']))
