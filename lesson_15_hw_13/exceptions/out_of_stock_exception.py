class OutOfStockException(Exception):
    """
    Exception raised for errors if the product was not find.
    """
    def __init__(self, message='Product was not find'):
        self.message = message
        super().__init__(self.message)
