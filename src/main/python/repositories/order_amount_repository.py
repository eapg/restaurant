# This file has the order amount repository

from src.main.python.repositories.generic_repository import GeneralRepository


class OrderAmountRepository(GeneralRepository):

    def __init__(self):
        self.order_amounts = {}

    def add(self, order_amount):
        self.order_amounts[order_amount.id] = order_amount
        return order_amount

    def get_by_id(self, order_amount_id):
        return self.order_amounts[order_amount_id]

    def get_all(self):
        return self.order_amounts

    def delete_by_id(self, order_amount_id):
        return self.order_amounts.pop(order_amount_id)

    def update_by_id(self, order_amount_id, new_order_amount):
        self.order_amounts[order_amount_id] = new_order_amount
