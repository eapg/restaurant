# test for the inventory product structure

from src.main.python.core import *
from src.main.python.entities import *

ioc_instance = ioc.Ioc()
inventory_product_controller = ioc_instance.get_instance('inventory_product_controller')

inventory_1 = inventory.Inventory()
inventory_product_1 = inventory_product.InventoryProduct()
inventory_product_2 = inventory_product.InventoryProduct()
inventory_product_3 = inventory_product.InventoryProduct()
inventory_product_4 = inventory_product.InventoryProduct()

product_1 = product.Product()
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
product_4.price = 180

inventory_product_1.inventory = inventory_1
inventory_product_1.product = product_1
inventory_product_1.product_quantity = 25

inventory_product_2.inventory = inventory_1
inventory_product_2.product = product_2
inventory_product_2.product_quantity = 100

inventory_product_3.inventory = inventory_1
inventory_product_3.product = product_3
inventory_product_3.product_quantity = 50

inventory_product_4.inventory = inventory_1
inventory_product_4.product = product_4
inventory_product_4.product_quantity = 250

print('--------------------------------------------------------------------------------------------------------------')
print('------------------------------------Testing inventory product structure---------------------------------------')
print('----------------------------------Testing inventary_product_controller.add()----------------------------------')
print('Adding pizza to inventory product id:1')
inventory_product_controller.insert_product(inventory_product_1)
print('Adding hamburger to inventory product id:2')
inventory_product_controller.insert_product(inventory_product_2)
print('Adding pasta to inventory product  id:3')
inventory_product_controller.insert_product(inventory_product_3)

print('--------------------------------------------------------------------------------------------------------------')
print('----------------------Testing get_products structure from inventory product controller------------------------')
print('Testing product controller method get_all()')
inventory_product_list = inventory_product_controller.get_products()
print(inventory_product_list[1].__dict__)
print(inventory_product_list[2].__dict__)
print(inventory_product_list[3].__dict__)

print('--------------------------------------------------------------------------------------------------------------')
print('-----------------------------------Testing get_product by id structure [id:1] --------------------------------')
print(inventory_product_controller.get_product(1).__dict__)

print('--------------------------------------------------------------------------------------------------------------')
print('---------------------------Testing delete_inventory_product by id structure [id:4]----------------------------')

print('before executing delete_product_by_id: we execute get_product_by_id id:4')
print(inventory_product_controller.get_product(2).__dict__)
inventory_product_controller.delete_product_by_id(2)
print('after deleting product: id:4')
try:
    inventory_product_controller.get_product(2)

except Exception:
    print('product no found in the repository')

print('--------------------------------------------------------------------------------------------------------------')
print('------------------------------Testing update_inventory_product by id structure--------------------------------')
print('-----------------------------Showing inventory product at id:1 before updating--------------------------------')
print(inventory_product_controller.get_product(3).__dict__)
print('---------updating product in id:3 before updating we have pasta and after updating we have a smoothie---------')
inventory_product_controller.update_product_by_id(3, inventory_product_4)
print(inventory_product_controller.get_product(3).__dict__)
