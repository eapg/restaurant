# structure for the product controller


class ProductController:

    def __init__(self, product_repository):
        self.product_repository = product_repository

    def get_product(self, product_id):
        self.product_repository.get_by_id(product_id)

    def get_products(self):
        self.product_repository.get_all()

    def insert_product(self, product):
        self.product_repository.add(product)

    def update_product_by_id(self, product_id):
        self.product_repository.update_by_id(product_id)

    def delete_product_by_id(self, product_id):
        self.product_repository.delete_by_id(product_id)



