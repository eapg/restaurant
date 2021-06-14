# This file has the inventory product repository

from src.main.python.repositories.generic_repository import GeneralRepository


class InventoryProductRepository(GeneralRepository):

    def __init__(self):
        self.inventory_products = {}
        self.next_id = 1

    def add(self, inventory_product):
        inventory_product.id = self.next_id
        self.inventory_products[self.next_id] = inventory_product
        self.next_id += 1
        return inventory_product

    def get_by_id(self, inventory_product_id):
        return self.inventory_products[inventory_product_id]

    def get_all(self):
        return self.inventory_products

    def delete_by_id(self, inventory_product_id):
        return self.inventory_products.pop(inventory_product_id)

    def update_by_id(self, inventory_product_id, new_inventory_product):
        self.inventory_products[inventory_product_id] = new_inventory_product
