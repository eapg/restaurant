# structure for the inventory product controller


class InventoryProductController:

    def __init__(self, inventory_product_repository):
        self.inventory_product_repository = inventory_product_repository

    def get_inventory_product(self, inventory_product_id):
        return self.inventory_product_repository.get_by_id(inventory_product_id)

    def get_inventories_product(self):
        return self.inventory_product_repository.get_all()

    def insert_inventory_product(self, inventory_product):
        self.inventory_product_repository.add(inventory_product)

    def update_inventory_product_by_id(self, inventory_product_id):
        self.inventory_product_repository.update_by_id(inventory_product_id)

    def delete_inventory_product_by_id(self, inventory_product_id):
        self.inventory_product_repository.delete_by_id(inventory_product_id)

