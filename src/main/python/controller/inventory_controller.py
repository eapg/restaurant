# structure for the inventory controller


class InventoryController:

    def __init__(self, inventory_repository):
        self.inventory_repository = inventory_repository

    def get_inventory(self, inventory_id):
        self.inventory_repository.get_by_id(inventory_id)

    def get_inventories(self):
        self.inventory_repository.get_all()

    def insert_inventory(self, inventory):
        self.inventory_repository.add(inventory)

    def update_inventory_by_id(self, inventory_id):
        self.inventory_repository.update_by_id(inventory_id)

    def delete_inventory_by_id(self, inventory_id):
        self.inventory_repository.delete_by_id(inventory_id)

