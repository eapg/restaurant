# structure for the chef controller

class ChefController:

    def __init__(self, chef_repository):
        self.chef_repository = chef_repository

    def get_chef(self, chef_id):
        return self.chef_repository.get_by_id(chef_id)

    def get_chefs(self):
        return self.chef_repository.get_all()

    def insert_chef(self, chef):
        self.chef_repository.add(chef)

    def update_chef_by_id(self, chef_id, new_chef):
        self.chef_repository.update_by_id(chef_id, new_chef)

    def delete_chef_by_id(self, chef_id):
        self.chef_repository.delete_by_id(chef_id)

