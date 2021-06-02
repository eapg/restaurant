# This file has the order repository

from src.main.python.repositories.generic_repository import GeneralRepository


class OrderRepository(GeneralRepository):

    def __init__(self):
        self.orders = {}
        self.next_id = 1

    def add(self, order):
        order.id = self.next_id
        self.orders[self.next_id] = order
        self.next_id += 1
        return order

    def get_by_id(self, order_id):
        return self.orders[order_id]

    def get_all(self):
        return self.orders

    def delete_by_id(self, order_id):
        return self.orders.pop(order_id)

    def update_by_id(self, order_id, new_order):
        self.orders[order_id] = new_order
