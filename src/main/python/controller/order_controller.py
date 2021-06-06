# structure for the order controller


class OrderController:

    def __init__(self, order_repository):
        self.order_repository = order_repository

    def get_order(self, order_id):
        self.order_repository.get_by_id(order_id)

    def get_orders(self):
        self.order_repository.get_all()

    def insert_order(self, order):
        self.order_repository.add(order)

    def update_order_by_id(self, order_id):
        self.order_repository.update_by_id(order_id)

    def delete_order_by_id(self, order_id):
        self.order_repository.delete_by_id(order_id)


