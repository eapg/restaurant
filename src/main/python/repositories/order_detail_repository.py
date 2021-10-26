# This file has the order detail repository

from src.main.python.repositories.generic_repository import GeneralRepository


class OrderDetailRepository(GeneralRepository):

    def __init__(self):
        self.orders_detail = {}

    def add(self, order_detail):
        self.orders_detail[order_detail.id] = order_detail
        return order_detail

    def get_by_id(self, order_detail_id):
        return self.orders_detail[order_detail_id]

    def get_all(self):
        return self.orders_detail

    def delete_by_id(self, order_detail_id):
        return self.orders_detail.pop(order_detail_id)

    def update_by_id(self, order_detail_id, new_order_detail):
        self.orders_detail[order_detail_id] = new_order_detail
