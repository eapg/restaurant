# This file has the menu repository

from src.main.python.repositories.generic_repository import GeneralRepository


class MenuRepository(GeneralRepository):

    def __init__(self):
        self.menus = {}

    def add(self, menu):
        self.menus[menu.id] = menu
        return menu

    def get_by_id(self, menu_id):
        return self.menus[menu_id]

    def get_all(self):
        return self.menus

    def delete_by_id(self, menu_id):
        return self.menus.pop(menu_id)

    def update_by_id(self, menu_id, new_menu):
        new_menu.id = menu_id
        self.menus[menu_id] = new_menu
