# structure for the menu controller


class MenuController:

    def __init__(self, menu_repository):
        self.menu_repository = menu_repository

    def get_menu(self, menu_id):
        return self.menu_repository.get_by_id(menu_id)

    def get_menus(self):
        return self.menu_repository.get_all()

    def insert_menu(self, menu):
        self.menu_repository.add(menu)

    def update_menu_by_id(self, menu_id, new_menu):
        self.menu_repository.update_by_id(menu_id, new_menu)

    def delete_menu_by_id(self, menu_id):
        self.menu_repository.delete_by_id(menu_id)

