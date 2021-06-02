# This file has the order amount repository

from src.main.python.repositories.generic_repository import GeneralRepository


class OrderAmountRepository(GeneralRepository):

    def __init__(self):
        self.order_amounts = {}
        self.next_id = 1

    def add(self, order_amount):
        order_amount.id = self.next_id
        self.order_amounts[self.next_id] = order_amount
        self.next_id += 1
        return order_amount

    def get_by_id(self, order_amount_id):
        return self.order_amounts[order_amount_id]

    def get_all(self):
        return self.order_amounts

    def delete_by_id(self, order_amount_id):
        return self.order_amounts.pop(order_amount_id)

    def update_by_id(self, order_amount_id, new_order_amount):
        self.order_amounts[order_amount_id] = new_order_amount
