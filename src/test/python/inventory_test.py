# # test for the inventory structure

from src.main.python.core import *
from src.main.python.entities import *

ioc_instance = ioc.Ioc()
inventory_controller = ioc_instance.get_instance('inventory_controller')

inventory_1 = inventory.Inventory()
inventory_2 = inventory.Inventory()
inventory_product_1 = inventory_product.InventoryProduct()
inventory_product_2 = inventory_product.InventoryProduct()
inventory_product_3 = inventory_product.InventoryProduct()

product_1 = product.Product()
product_1.id = 1
product_1.name = 'pizza'
product_1.description = 'ham and cheese with bacon'
product_1.price = 250

product_2 = product.Product()
product_2.name = 'hamburger'
product_2.description = 'bacon triple hamburger'
product_2.price = 200

product_3 = product.Product()
product_3.name = 'pasta'
product_3.description = 'Carbonara pasta with bread'
product_3.price = 180

product_4 = product.Product()
product_4.name = 'smoothie'
product_4.description = 'strawberry and cream frozen smoothie'
product_4.price = 200

inventory_product_1.id = 1
inventory_product_1.product = product_1
inventory_product_1.product_quantity = 25

inventory_product_2.id = 2
inventory_product_2.product = product_2
inventory_product_2.product_quantity = 100

inventory_product_3.id = 3
inventory_product_3.product = product_3
inventory_product_3.product_quantity = 50

inventory_1.inventory_list = inventory_product_1
inventory_1.inventory_list = inventory_product_2
inventory_1.inventory_list = inventory_product_3

# creating a 2nd inventory to test delete method

inventory_2.inventory_product_list = inventory_product_1
inventory_2.inventory_product_list = inventory_product_2
inventory_2.inventory_product_list = inventory_product_3

print('--------------------------------------------------------------------------------------------------------------')
print('----------------------------------------Testing inventory  structure------------------------------------------')
print('-------------------------------------Testing inventary_controller.add()---------------------------------------')

print('Adding inventory to the repository')
inventory_controller.insert_inventory(inventory_1)
inventory_controller.insert_inventory(inventory_2)
print('--------------------------------------------------------------------------------------------------------------')
print('-------------------------Testing get_inventories structure from inventory  controller-------------------------')
print('Testing product controller method get_all()')
inventory_list = inventory_controller.get_inventories()
print(inventory_list[1].__dict__)
print(inventory_list[2].__dict__)

print('--------------------------------------------------------------------------------------------------------------')
print('-----------------------------------Testing get_inventory by id structure [id:1] --------------------------------')
print(inventory_controller.get_inventory(1).__dict__)

print('--------------------------------------------------------------------------------------------------------------')
print('------------------------------Testing delete_inventory by id structure [id:1]---------------------------------')

print('before executing delete_product_by_id: we execute get_product_by_id id:2')
print(inventory_controller.get_inventory(2).__dict__)
inventory_controller.delete_inventory_by_id(2)
print('after deleting product: id:2')
try:
    inventory_controller.get_inventory(2)

except Exception:
    print('product no found in the repository')

print('--------------------------------------------------------------------------------------------------------------')
print('------------------------------Testing update_inventory_product by id structure--------------------------------')
print('-----------------------------Showing inventory product at id:1 before updating--------------------------------')

print(inventory_controller.get_inventory(1).inventory_list.product.__dict__)

inventory_product_1.product = product_4
inventory_product_1.product_quantity = 150

inventory_1.inventory_product_list = inventory_product_1

print('updating product in id:1 inside the inventory,')
inventory_controller.update_inventory_by_id(1, inventory_1)
print(inventory_controller.get_inventory(1).inventory_list.product.__dict__)
