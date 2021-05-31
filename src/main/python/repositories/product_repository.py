# This file has the product repository

from src.main.python.repositories.generic_repository import GeneralRepository


class ProductRepository(GeneralRepository):

    def __init__(self):
        self.products = {}
        self.next_id = 1

    def add(self, product):
        product.id = self.next_id
        self.products[self.next_id] = product
        self.next_id += 1
        return product

    def get_by_id(self, product_id):
        return self.products[product_id]

    def get_all(self):
        return self.products

    def delete_by_id(self, product_id):
        return self.products.pop(product_id)

    def update_by_id(self, product_id, new_product):
        self.products[product_id] = new_product




