# test for the order structure
import order
import order_detail

from src.main.python.core import *
from src.main.python.entities import *

ioc_instance = ioc.Ioc()
order_controller = ioc_instance.get_instance('order_controller')

order_1 = order.Order()
order_1.id = 1
order_detail_1 = order_detail.OrderDetails()

order_2 = order.Order()
order_2.id = 2
order_detail_2 = order_detail.OrderDetails()

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
product_3.name = 'Pina Colada'
product_3.description = 'Frozen Pina Colada'
product_3.price = 100

product_4 = product.Product()
product_4.name = 'smoothie'
product_4.description = 'strawberry and cream frozen smoothie'
product_4.price = 150

# order 1 - Pizza + Smoothie
order_detail_1.id = 1
order_detail_1.order_product_list[1] = product_1
order_detail_1.order_product_list[2] = product_4

amount = 0
for k in order_detail_1.order_product_list:
    amount += order_detail_1.order_product_list[k].price

# order 1 total amount with taxes
amount = amount * 1.28
order_detail_1.order_amount = amount

# order 2 - Hamburger + Pina Colada
order_detail_2.id = 1
order_detail_2.order_product_list[1] = product_2
order_detail_2.order_product_list[2] = product_3

amount = 0
for k in order_detail_2.order_product_list:
    amount += order_detail_2.order_product_list[k].price

# order 2 total amount with taxes
amount = amount * 1.28
order_detail_2.order_amount = amount

order_1.order_details = order_detail_1
order_1.order_status = 'open'

order_2.order_details = order_detail_2
order_2.order_status = 'open'

print('--------------------------------------------------------------------------------------------------------------')
print('----------------------------------------Testing order structure------------------------------------------------')
print('-------------------------------------Testing order_controller.add()--------------------------------------------')

print('Adding orders to the order repository through the controller')
order_controller.insert_order(order_1)
order_controller.insert_order(order_2)

print('--------------------------------------------------------------------------------------------------------------')
print('------------------------------Testing get_orders structure from order controller--------------------------------')
print('Testing order controller method get_all()')
order_list = order_controller.get_orders()
print('Showing order #1')
print('products:')
print(order_list[1].order_details.order_product_list[1].__dict__)
print(order_list[1].order_details.order_product_list[2].__dict__)
print('Total Amount:')
print(order_list[1].order_details.order_amount)

print('Showing order #2')
print('products:')
print(order_list[2].order_details.order_product_list[1].__dict__)
print(order_list[2].order_details.order_product_list[2].__dict__)
print('Total Amount:')
print(order_list[2].order_details.order_amount)

print('--------------------------------------------------------------------------------------------------------------')
print('-----------------------------------Testing get_order by id structure [id:1] -----------------------------------')
print(order_controller.get_order(1).__dict__)

print('--------------------------------------------------------------------------------------------------------------')
print('------------------------------Testing delete_order by id structure [id:2]--------------------------------------')

order_controller.delete_order_by_id(2)
try:
    order_controller.get_order(2)

except Exception:
    print('order #2 complete')

print('---------------------------------------------------------------------------------------------------------------')
print('-----------------------------------Testing update_order by id structure----------------------------------------')
print('----------------------------Showing order at id:1 before client changed ---------------------------------------')

order_a = order_controller.get_order(1)
print('Showing order #1')
print('products:')
print(order_a.order_details.order_product_list[1].__dict__)
print(order_a.order_details.order_product_list[2].__dict__)
print('Total Amount:')
print(order_a.order_details.order_amount)

print('----------------------------Showing order at id:1 after client changed ----------------------------------------')

order_controller.update_order_by_id(1, order_2)
order_a = order_controller.get_order(1)
print('Showing order #1')
print('products:')
print(order_a.order_details.order_product_list[1].__dict__)
print(order_a.order_details.order_product_list[2].__dict__)
print('Total Amount:')
print(order_a.order_details.order_amount)
