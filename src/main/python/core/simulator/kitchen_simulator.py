# code for the kitchen simulator

from threading import Thread
from src.main.python.seed import *
from src.main.python.core import *
import time


def init_order_manager_simulator():
    order_manager_simulator.init_order_storage(['order placed', 'in process', 'completed'])


def add_order_to_order_placed_queue(order_id):
    order_manager_simulator.add_to_order_storage(initial_data.order_controller.get_order(order_id), 'order placed')
    print(f'Order {order_id} successfully added')


def add_order_to_order_complete(order):
    order_manager_simulator.add_to_order_storage(order, 'completed')
    print(f'Order {order.id} ready. waiting to be served.')


class KitchenSimulator:

    def __init__(self, chefs):
        self.chefs = chefs

    @staticmethod
    def chef_process_to_prepare_the_order(chef, time_counter):

        order_time = 0
        chef.order_start_time = time_counter
        print(f'time in the moment: {time_counter}')
        chef.chef_status = 'busy'
        print(f'Chef {chef.id} take the order number: {chef.order_to_work.id}')
        chef.order_to_work.status = 'In process'
        print(f'Order {chef.order_to_work.id} in process....')
        order_len = len(chef.order_to_work.order_details.order_product_list)

        for i in range(1, order_len):
            order_time = order_time + chef.order_to_work.order_details.order_product_list[i].product_complexity

        time_order = int((order_time / 10) * chef.ability)
        print(f'estimation time for the order {time_order} minutes')
        chef.estimate_order_time = time_order

    def chefs_in_kitchen(self):

        time_counter = 0

        while True:

            for chef in self.chefs:

                if chef.chef_status == 'Available' and not order_manager_simulator.get_queue_status('order placed'):

                    chef.order_to_work = order_manager_simulator.get_from_order_storage('order placed')
                    self.chef_process_to_prepare_the_order(chef, time_counter)

                else:

                    if chef.estimate_order_time == (time_counter - chef.order_start_time):
                        print(f'order {chef.order_to_work.id} complete')
                        chef.order_to_work.order_status = 'Complete'
                        add_order_to_order_complete(chef.order_to_work)
                        chef.chef_status = 'Available'

            time.sleep(1)
            time_counter += 1

    def adding_new_chef_to_kitchen(self, chef):
        self.chefs.append(chef)


if __name__ == "__main__":

    order_manager_simulator = order_manager.OrderManager()
    init_order_manager_simulator()

    add_order_to_order_placed_queue(1)
    add_order_to_order_placed_queue(2)
    add_order_to_order_placed_queue(3)
    add_order_to_order_placed_queue(4)
    add_order_to_order_placed_queue(5)

    kitchen_simulator = KitchenSimulator(([initial_data.chef_1, initial_data.chef_2, initial_data.chef_3]))

    t_k = Thread(target=kitchen_simulator.chefs_in_kitchen)
    t_k.start()
    time.sleep(10)
    add_order_to_order_placed_queue(1)
