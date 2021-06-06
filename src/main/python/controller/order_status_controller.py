# structure for the order status controller


class OrderStatusController:

    def __init__(self, order_status_repository):
        self.order_status_repository = order_status_repository

    def get_order_status(self, order_status_id):
        self.order_status_repository.get_by_id(order_status_id)

    def get_orders_status(self):
        self.order_status_repository.get_all()

    def insert_order_status(self, order_status):
        self.order_status_repository.add(order_status)

    def update_order_status_by_id(self, order_status_id):
        self.order_status_repository.update_by_id(order_status_id)

    def delete_order_status_by_id(self, order_status_id):
        self.order_status_repository.delete_by_id(order_status_id)


