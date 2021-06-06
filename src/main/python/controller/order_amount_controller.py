# structure for the order amount controller


class OrderAmountController:

    def __init__(self, order_amount_repository):
        self.order_amount_repository = order_amount_repository

    def get_order_amount(self, order_amount_id):
        self.order_amount_repository.get_by_id(order_amount_id)

    def get_orders_amount(self):
        self.order_amount_repository.get_all()

    def insert_order_amount(self, order_amount):
        self.order_amount_repository.add(order_amount)

    def update_order_amount_by_id(self, order_amount_id):
        self.order_amount_repository.update_by_id(order_amount_id)

    def delete_order_amount_by_id(self, order_amount_id):
        self.order_amount_repository.delete_by_id(order_amount_id)


