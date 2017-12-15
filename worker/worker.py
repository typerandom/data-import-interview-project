from database import Order

"""
Store - model

    id
    name

Order - model

    id - int
    store_id - int
    reference_id - string
    item_skus - string[]
    total_amount - decimal
    currency - string
    created_at - date

Database - data store

    stores

        get_all()

    orders

        save(order)
        batch_save(orders[])
"""

class Worker(object):
    def __init__(self, database):
        self.database = database

    def process(self, filepath):
        print('Processing file', filepath)

        print('Stores', self.database.stores.get_all())

        self.database.orders.save(Order(
            total_amount=123,
        ))