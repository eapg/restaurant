# This file has the product repository

from src.main.python.repositories.generic_repository import GeneralRepository


class ProductRepository(GeneralRepository):

    def __init__(self):
        self.products = {}

    def add(self, product):
        self.products[product.id] = product
        return product

    def get_by_id(self, product_id):
        return self.products[product_id]

    def get_all(self):
        return self.products

    def delete_by_id(self, product_id):
        return self.products.pop(product_id)

    def update_by_id(self, product_id, new_product):
        new_product.id = product_id
        self.products[product_id] = new_product

