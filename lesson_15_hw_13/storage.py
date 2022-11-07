import json


class Storage:
    def __init__(self):
        self._paths = {'orders': 'storage/orders.json',
                       'products': 'storage/products.json'
                       }

    def _open_storage(self, storage_name, mode='w'):
        path = self._paths[storage_name]
        return open(path, mode)

    def _close_storage(self, storage):
        storage.close()

    def write(self, storage_name, data):
        storage = self._open_storage(storage_name)
        json.dump(data, storage)
        self._close_storage(storage)

    def read(self, storage_name):
        storage = self._open_storage(storage_name, 'r')
        data = json.load(storage)
        self._close_storage(storage)
        return data

    def add_record(self, storage_name, data):
        records = self.read(storage_name)
        records.append(data)
        self.write(storage_name, records)
