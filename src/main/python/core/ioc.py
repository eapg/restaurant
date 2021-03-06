# structure for the ioc to have just one instance

from src.main.python.core.singleton_decorator import singleton
from src.main.python.repositories import *
from src.main.python.controller import *


@singleton
class Ioc:

    __instance_ioc = {}

    def __init__(self):

        self.__init_repositories()
        self.__init_controllers()

    def __init_repositories(self):
        self.__instance_ioc['product_repository'] = product_repository.ProductRepository()
        self.__instance_ioc['inventory_repository'] = inventory_repository.InventoryRepository()
        self.__instance_ioc['inventory_product_repository'] = inventory_product_repository.InventoryProductRepository()
        self.__instance_ioc['menu_repository'] = menu_repository.MenuRepository()
        self.__instance_ioc['order_repository'] = order_repository.OrderRepository()
        self.__instance_ioc['order_amount_repository'] = order_amount_repository.OrderAmountRepository()
        self.__instance_ioc['order_detail_repository'] = order_detail_repository.OrderDetailRepository()
        self.__instance_ioc['order_status_repository'] = order_status_repository.OrderStatusRepository()
        self.__instance_ioc['chef_repository'] = chef_repository.ChefRepository()

    def __init_controllers(self):
        self.__instance_ioc['product_controller'] = product_controller.ProductController(
            self.__instance_ioc['product_repository'])
        self.__instance_ioc['inventory_controller'] = inventory_controller.InventoryController(
            self.__instance_ioc['inventory_repository'])
        self.__instance_ioc['inventory_product_controller'] = inventory_product_controller.InventoryProductController(
            self.__instance_ioc['inventory_product_repository'])
        self.__instance_ioc['menu_controller'] = menu_controller.MenuController(
            self.__instance_ioc['menu_repository'])
        self.__instance_ioc['order_controller'] = order_controller.OrderController(
            self.__instance_ioc['order_repository'])
        self.__instance_ioc['order_amount_controller'] = order_amount_controller.OrderAmountController(
            self.__instance_ioc['order_amount_repository'])
        self.__instance_ioc['order_detail_controller'] = order_detail_controller.OrderDetailController(
            self.__instance_ioc['order_detail_repository'])
        self.__instance_ioc['order_status_controller'] = order_status_controller.OrderStatusController(
            self.__instance_ioc['order_status_repository'])
        self.__instance_ioc['chef_controller'] = chef_controller.ChefController(
            self.__instance_ioc['chef_repository'])

    def put_instance(self, instance, instance_id):
        self.__instance_ioc[instance_id] = instance

    def get_instance(self, instance_id):
        return self.__instance_ioc[instance_id]

