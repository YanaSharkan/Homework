class OperationException(Exception):
    """
    Exception raised for errors if the operation is not supported.
    """
    def __init__(self, message='Operation is not supported!'):
        self.message = message
        super().__init__(self.message)
