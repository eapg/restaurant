# structure for the order detail controller


class OrderDetailController:

    def __init__(self, order_detail_repository):
        self.order_detail_repository = order_detail_repository

    def get_order_detail(self, order_detail_id):
        self.order_detail_repository.get_by_id(order_detail_id)

    def get_orders_detail(self):
        self.order_detail_repository.get_all()

    def insert_order_detail(self, order_detail):
        self.order_detail_repository.add(order_detail)

    def update_order_detail_by_id(self, order_detail_id):
        self.order_detail_repository.update_by_id(order_detail_id)

    def delete_order_detail_by_id(self, order_detail_id):
        self.order_detail_repository.delete_by_id(order_detail_id)


