from shop import Shop
from storage import Storage
from exceptions.operation_exception import OperationException
from exceptions.out_of_stock_exception import OutOfStockException


def main():
    storage = Storage()
    shop = Shop(storage)
    try:
        shop.choose_operations()
    except (OperationException, OutOfStockException) as err:
        print(err)


if __name__ == '__main__':
    main()
