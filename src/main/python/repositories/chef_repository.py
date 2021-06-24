# This file has the chef repository

from src.main.python.repositories.generic_repository import GeneralRepository


class ChefRepository(GeneralRepository):

    def __init__(self):
        self.chefs = {}
        self.next_id = 1

    def add(self, chef):
        chef.id = self.next_id
        self.chefs[self.next_id] = chef
        self.next_id += 1
        return chef

    def get_by_id(self, chef_id):
        return self.chefs[chef_id]

    def get_all(self):
        return self.chefs

    def delete_by_id(self, chef_id):
        return self.chefs.pop(chef_id)

    def update_by_id(self, chef_id, new_chef):
        new_chef.id = chef_id
        self.chefs[chef_id] = new_chef

