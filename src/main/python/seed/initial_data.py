# initial data to simulate al the entities initialization for the simulator

from src.main.python.core import *
from src.main.python.entities import *


def reduce_from_inventory(product_to_by_reduce):
    pass


ioc_instance = ioc.Ioc()
product_controller = ioc_instance.get_instance('product_controller')
inventory_product_controller = ioc_instance.get_instance('inventory_product_controller')
inventory_controller = ioc_instance.get_instance('inventory_controller')

# products
product_pizza = product.Product()
product_pizza.id = 1
product_pizza.description = 'Ham and cheese with bacon'
product_pizza.price = 250
product_pizza.product_complexity = 30

product_controller.insert_product(product_pizza)

inventory_product_pizza = inventory_product.InventoryProduct()
inventory_product_pizza.id = 1
inventory_product_pizza.product = product_controller.get_product(1)
inventory_product_pizza.product_quantity = 50

inventory_product_controller.insert_inventory_product(inventory_product_pizza)

product_hamburger = product.Product()
product_hamburger.id = 2
product_hamburger.description = 'Bacon triple hamburger'
product_hamburger.price = 200
product_hamburger.product_complexity = 25

product_controller.insert_product(product_hamburger)

inventory_product_hamburger = inventory_product.InventoryProduct()
inventory_product_hamburger.id = 2
inventory_product_hamburger.product = product_controller.get_product(2)
inventory_product_hamburger.product_quantity = 30

inventory_product_controller.insert_inventory_product(inventory_product_hamburger)

product_pasta = product.Product()
product_pasta.id = 3
product_pasta.description = 'pesto pasta'
product_pasta.price = 180
product_pasta.product_complexity = 35

product_controller.insert_product(product_pasta)

inventory_product_pasta = inventory_product.InventoryProduct()
inventory_product_pasta.id = 3
inventory_product_pasta.product = product_controller.get_product(3)
inventory_product_pasta.product_quantity = 20

inventory_product_controller.insert_inventory_product(inventory_product_pasta)

product_smoothie = product.Product()
product_smoothie.id = 4
product_smoothie.description = 'strawberry and cream frozen smoothie'
product_smoothie.price = 120
product_smoothie.product_complexity = 15

product_controller.insert_product(product_smoothie)

inventory_product_smoothie = inventory_product.InventoryProduct()
inventory_product_smoothie.id = 4
inventory_product_smoothie.product = product_controller.get_product(4)
inventory_product_smoothie.product_quantity = 10

inventory_product_controller.insert_inventory_product(inventory_product_smoothie)

product_juice = product.Product()
product_juice.id = 5
product_juice.description = 'Fruit punch juice'
product_juice.price = 100
product_juice.product_complexity = 10

product_controller.insert_product(product_juice)

inventory_product_juice = inventory_product.InventoryProduct()
inventory_product_juice.id = 5
inventory_product_juice.product = product_controller.get_product(5)
inventory_product_juice.product_quantity = 5

inventory_product_controller.insert_inventory_product(inventory_product_juice)

inventory_controller.insert_inventory(inventory_product_controller.get_inventory_product(1))
inventory_controller.insert_inventory(inventory_product_controller.get_inventory_product(2))
inventory_controller.insert_inventory(inventory_product_controller.get_inventory_product(3))
inventory_controller.insert_inventory(inventory_product_controller.get_inventory_product(4))
inventory_controller.insert_inventory(inventory_product_controller.get_inventory_product(5))

# create the orders to test kitchen simulator

order_controller = ioc_instance.get_instance('order_controller')

# order #1 - Pizza + Juice
order_1 = order.Order()
order_1.id = 1
order_1.client_name = 'Elido p'

order_detail_1 = order_detail.OrderDetails()
order_detail_1.id = 1
order_detail_1.order_product_list[1] = product_controller.get_product(1)
reduce_from_inventory(product_controller.get_product(1))
order_detail_1.order_product_list[2] = product_controller.get_product(5)
reduce_from_inventory(product_controller.get_product(5))

# add amount of the total order 1

order_1.order_details = order_detail_1
order_controller.insert_order(order_1)

# order #2 - Pasta + Juice
order_2 = order.Order()
order_2.id = 2
order_2.client_name = 'Andres p'

order_detail_2 = order_detail.OrderDetails()
order_detail_2.id = 2
order_detail_2.order_product_list[1] = product_controller.get_product(3)
reduce_from_inventory(product_controller.get_product(3))
order_detail_2.order_product_list[2] = product_controller.get_product(5)
reduce_from_inventory(product_controller.get_product(5))

# add amount of the total order 2

order_2.order_details = order_detail_2
order_controller.insert_order(order_2)

# order #3 - hamburger + Juice
order_3 = order.Order()
order_3.id = 3
order_3.client_name = 'Andreina p'

order_detail_3 = order_detail.OrderDetails()
order_detail_3.id = 3

order_detail_3.order_product_list[1] = product_controller.get_product(2)
reduce_from_inventory(product_controller.get_product(2))
order_detail_3.order_product_list[2] = product_controller.get_product(5)
reduce_from_inventory(product_controller.get_product(5))

# add amount of the total order 3

order_3.order_details = order_detail_3
order_controller.insert_order(order_3)

# order #4 - Hamburger + Pizza + Juice + Smoothie
order_4 = order.Order()
order_4.id = 4
order_4.client_name = 'Lluvia A'

order_detail_4 = order_detail.OrderDetails()
order_detail_4.id = 4

order_detail_4.order_product_list[1] = product_controller.get_product(2)
reduce_from_inventory(product_controller.get_product(2))
order_detail_4.order_product_list[2] = product_controller.get_product(1)
reduce_from_inventory(product_controller.get_product(1))
order_detail_4.order_product_list[3] = product_controller.get_product(5)
reduce_from_inventory(product_controller.get_product(5))
order_detail_4.order_product_list[4] = product_controller.get_product(4)
reduce_from_inventory(product_controller.get_product(4))

# add amount of the total order 4

order_4.order_details = order_detail_4
order_controller.insert_order(order_4)

# order #5 - Juice + Smoothie
order_5 = order.Order()
order_5.id = 5

order_detail_5 = order_detail.OrderDetails()
order_detail_5.id = 5
order_detail_5.client_name = 'Luiggi c'
order_detail_5.order_product_list[1] = product_controller.get_product(5)
reduce_from_inventory(product_controller.get_product(5))
order_detail_5.order_product_list[2] = product_controller.get_product(4)
reduce_from_inventory(product_controller.get_product(4))

# add amount of the total order 5

order_5.order_details = order_detail_5
order_controller.insert_order(order_5)


# creating chefs to be use in the kitchen simulator

chef_controller = ioc_instance.get_instance('chef_controller')

chef_1 = chef.Chef()
chef_1.id = 40255
chef_1.name = 'andres'
chef_1.ability = 10
chef_1.chef_status = 'Available'
chef_1.estimate_order_time = 0
chef_1.star_order_time = 0

chef_2 = chef.Chef()
chef_2.id = 40256
chef_2.name = 'marcos'
chef_2.ability = 10
chef_2.chef_status = 'Available'
chef_2.estimate_order_time = 0
chef_2.star_order_time = 0

chef_3 = chef.Chef()
chef_3.id = 40257
chef_3.name = 'Papotico'
chef_3.ability = 10
chef_3.chef_status = 'Available'
chef_3.estimate_order_time = 0
chef_3.star_order_time = 0

chef_controller.insert_chef(chef_1)
chef_controller.insert_chef(chef_2)
chef_controller.insert_chef(chef_3)
