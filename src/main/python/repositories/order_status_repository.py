# This file has the order status repository

from src.main.python.repositories.generic_repository import GeneralRepository


class OrderStatusRepository(GeneralRepository):

    def __init__(self):
        self.orders_status = {}
        self.next_id = 1

    def add(self, order_status):
        order_status.id = self.next_id
        self.orders_status[self.next_id] = order_status
        self.next_id += 1
        return order_status

    def get_by_id(self, order_status_id):
        return self.orders_status[order_status_id]

    def get_all(self):
        return self.orders_status

    def delete_by_id(self, order_status_id):
        return self.orders_status.pop(order_status_id)

    def update_by_id(self, order_status_id, new_order_status):
        self.orders_status[order_status_id] = new_order_status
