# Test for the menu structure
import menu

from src.main.python.core import *
from src.main.python.entities import *

ioc_instance = ioc.Ioc()
menu_controller = ioc_instance.get_instance('menu_controller')

menu_1 = menu.Menu()
menu_2 = menu.Menu()

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

menu_1.id = 1
menu_1.category = 'Main course'
menu_1.menu_product_list[1] = product_1
menu_1.menu_product_list[2] = product_2

menu_2.id = 2
menu_2.category = 'Beverage'
menu_2.menu_product_list[1] = product_3
menu_2.menu_product_list[2] = product_4

print('--------------------------------------------------------------------------------------------------------------')
print('----------------------------------------Testing menu structure------------------------------------------------')
print('-------------------------------------Testing menu_controller.add()--------------------------------------------')

print('Adding menus to the menu repository through the controller')
menu_controller.insert_menu(menu_1)
menu_controller.insert_menu(menu_2)

print('--------------------------------------------------------------------------------------------------------------')
print('------------------------------Testing get_menus structure from menu controller--------------------------------')
print('Testing menu controller method get_all()')
menu_list = menu_controller.get_menus()
print(menu_list[1].category)
print(menu_list[1].menu_product_list[1].__dict__)
print(menu_list[1].menu_product_list[2].__dict__)

print(menu_list[2].category)
print(menu_list[2].menu_product_list[1].__dict__)
print(menu_list[2].menu_product_list[2].__dict__)

print('--------------------------------------------------------------------------------------------------------------')
print('-----------------------------------Testing get_menu by id structure [id:1] -----------------------------------')
print(menu_controller.get_menu(1).__dict__)

print('--------------------------------------------------------------------------------------------------------------')
print('------------------------------Testing delete_menu by id structure [id:2]--------------------------------------')

print('before executing delete_menu_by_id: we execute get_menu_by_id id:2')
print(menu_controller.get_menu(2).__dict__)
menu_controller.delete_menu_by_id(2)
print('after deleting menu: id:2')
try:
    menu_controller.get_menu(2)

except Exception:
    print('menu no found in the repository')

print('--------------------------------------------------------------------------------------------------------------')
print('-----------------------------------Testing update_menu by id structure----------------------------------------')
print('----------------------------------Showing menu at id:1 before updating----------------------------------------')

print(menu_controller.get_menu(1).__dict__)

print('updating Menu id:1 with the menu id:2 data, now we have beverage at menu id:1')

menu_controller.update_menu_by_id(1, menu_2)

print(menu_controller.get_menu(1).__dict__)

