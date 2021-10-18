# This file has the inventory repository

from src.main.python.repositories.generic_repository import GeneralRepository


class InventoryRepository(GeneralRepository):

    def __init__(self):
        self.inventories = {}

    def add(self, inventory):
        self.inventories[inventory.id] = inventory
        return inventory

    def get_by_id(self, inventory_id):
        return self.inventories[inventory_id]

    def get_all(self):
        return self.inventories

    def delete_by_id(self, inventory_id):
        return self.inventories.pop(inventory_id)

    def update_by_id(self, inventory_id, new_inventory):
        new_inventory.id = inventory_id
        self.inventories[inventory_id] = new_inventory
