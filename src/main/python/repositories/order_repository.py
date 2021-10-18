# This file has the order repository

from src.main.python.repositories.generic_repository import GeneralRepository


class OrderRepository(GeneralRepository):

    def __init__(self):
        self.orders = {}

    def add(self, order):
        self.orders[order.id] = order
        return order

    def get_by_id(self, order_id):
        return self.orders[order_id]

    def get_all(self):
        return self.orders

    def delete_by_id(self, order_id):
        return self.orders.pop(order_id)

    def update_by_id(self, order_id, new_order):
        new_order.id = order_id
        self.orders[order_id] = new_order
