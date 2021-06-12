# this file have the product test. we test the controller and its methods

from src.main.python.core import *
from src.main.python.entities import *

ioc_instance = ioc.Ioc()
product_controller = ioc_instance.get_instance('product_controller')

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

print('--------------------------------------------------------------------------------------------------------------')
print('----------------------------------------Testing product structure---------------------------------------------')
print('-------------------------------------Testing product_controller.add()-----------------------------------------')
print('Adding a product(pizza) id:1')
product_controller.insert_product(product_1)
print('Adding a second product(hamburger) id:2')
product_controller.insert_product(product_2)
print('Adding a third product(pasta) id:3')
product_controller.insert_product(product_3)
print('Adding a four product(smoothie) id:4')
product_controller.insert_product(product_4)

print('--------------------------------------------------------------------------------------------------------------')
print('--------------------------------------Testing get_products structure------------------------------------------')
print('Testing product controller method get_all()')
product_list = product_controller.get_products()
print(product_list[1].__dict__)
print(product_list[2].__dict__)
print(product_list[3].__dict__)
print(product_list[4].__dict__)

print('--------------------------------------------------------------------------------------------------------------')
print('-----------------------------------Testing get_product by id structure [id:1] --------------------------------')
print(product_controller.get_product(1).__dict__)

print('--------------------------------------------------------------------------------------------------------------')
print('-----------------------------------Testing delete_product by id structure [id:4]------------------------------')

print('before executing delete_product_by_id: we execute get_product_by_id id:4')
print(product_controller.get_product(4).__dict__)
product_controller.delete_product_by_id(4)
print('after deleting product: id:4')
try:
    product_controller.get_product(4)

except Exception:
    print('product no found in the repository')

print('--------------------------------------------------------------------------------------------------------------')
print('-----------------------------------Testing update_product by id structure-------------------------------------')
print('----------------------------------Showing product at id:1 before updating-------------------------------------')
print(product_controller.get_product(1).__dict__)
print('---------updating product in id:1 before updating we have pizza and after updating we have a smoothie---------')
product_controller.update_product_by_id(1, product_4)
print(product_controller.get_product(1).__dict__)

print('---------------------------------------------------------------------------------------------------------------')
print('-------------------------Second instance to test that the instance is singleton--------------------------------')

ioc_2nd_instance = ioc.Ioc()
product_controller2 = ioc_2nd_instance.get_instance('product_controller')
product_list2 = product_controller2.get_products()
print(product_list2[1].__dict__)
print(product_list2[2].__dict__)
print(product_list2[3].__dict__)

