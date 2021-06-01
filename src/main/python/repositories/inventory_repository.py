# This file has the inventory repository

from src.main.python.repositories.generic_repository import GeneralRepository


class InventoryRepository(GeneralRepository):

    def __init__(self):
        self.inventories = {}
        self.next_id = 1

    def add(self, inventory):
        inventory.id = self.next_id
        self.inventories[self.next_id] = inventory
        self.next_id += 1
        return inventory

    def get_by_id(self, inventory_id):
        return self.inventories[inventory_id]

    def get_all(self):
        return self.inventories

    def delete_by_id(self, inventory_id):
        return self.inventories.pop(inventory_id)

    def update_by_id(self, inventory_id, new_inventory):
        self.inventories[inventory_id] = new_inventory
