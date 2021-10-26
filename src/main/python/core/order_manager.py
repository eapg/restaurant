# order manager mechanism

from queue import Queue


class OrderManager:

    def __init__(self):

        self.__order_storage = {}
        self.order_id_count = 1

    def init_order_storage(self, order_status):

        for status in order_status:

            self.__order_storage[status] = Queue(maxsize=0)

    def add_to_order_storage(self, order, order_status):

        order.id = self.order_id_count
        self.order_id_count += 1
        self.__order_storage[order_status].put(order)

    def get_from_order_storage(self, order_status):

        return self.__order_storage[order_status].get()

    def get_queue_size(self, order_status):

        return self.__order_storage[order_status].qsize()

    def get_queue_status(self, order_status):

        return self.__order_storage[order_status].empty()

