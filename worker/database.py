class Store(object):
    def __init__(self, id=None, name=None):
        self.id = id
        self.name = name

    def __repr__(self):
        return str(self)

    def __str__(self):
        return '<Store id={id} name={name} />'.format(
            **self.__dict__
        )

class StoreManager(object):
    def __init__(self):
        self._stores = [
            Store(
                id=1,
                name='us/new york'
            ),
            Store(
                id=2,
                name='se/stockholm',
            ),
        ]

    def get_all(self):
        return self._stores


class Order(object):
    def __init__(self, id=None, store_id=None, reference_id=None, item_skus=None, total_amount=None, currency=None, created_at=None):
        self.id = id
        self.store_id = store_id
        self.reference_id = reference_id
        self.item_skus = item_skus
        self.total_amount = total_amount
        self.currency = currency
        self.created_at = created_at

    def __str__(self):
        return '<Order id={id} store_id={store_id} reference_id={reference_id} item_skus={item_skus} total_amount={total_amount} currency={currency} created_at={created_at} />'.format(
            **self.__dict__
        )

    def __repr__(self):
        return str(self)

class OrderManager(object):
    def __init__(self):
        return

    def save(self, order):
        print('Saving order', order)

    def batch_save(self, orders):
        for order in orders:
            order.save()

class Database(object):
    def __init__(self):
        self.orders = OrderManager()
        self.stores = StoreManager()