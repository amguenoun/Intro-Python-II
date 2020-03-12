# Write a class to hold player information, e.g. what room they are in
# currently.
from item import LightSource


class Player:
    def __init__(self, name, current_room, inventory=None):
        self.name = name
        self.current_room = current_room
        self.inventory = inventory
        self.score = 0
        self.sight = True
        if self.inventory is None:
            self.inventory = []

    def take_item(self, target):
        if self.sight:
            x = 1
            for item in self.current_room.item_list:
                if target == item.name:
                    self.inventory.append(item)
                    self.current_room.remove_item(item)
                    item.on_take(self.name)
                    self.score += 10
                    x = 0
            if x:
                print(f'No {target} to pick up.')
        else:
            print("Good luck trying to pick things up in the dark!")

    def drop_item(self, target):
        if self.inventory:
            x = 1
            for item in self.inventory:
                if target == item.name:
                    self.inventory.remove(item)
                    self.current_room.add_item(item)
                    item.on_drop(self.name)
                    self.score -= 10
                    x = 0
            if x:
                print(f'No {target} to drop.')
        else:
            print('Inventory is empty. Nothing to drop')

    def print_inventory(self):
        if len(self.inventory) == 0:
            print('Inventory is empty')
        else:
            print(f'{self.name} opens their inventory:')
            for item in self.inventory:
                print(item)
            print()

    def travel(self, direction):
        if self.current_room.get_room(direction):
            self.current_room = self.current_room.get_room(direction)
            self.score += 1
            self.print_player_location()
        else:
            print("There is nothing in that direction")

    def print_player_location(self):
        if self.current_room.is_light or [True for item in self.inventory if isinstance(item, LightSource)] or [True for item in self.current_room.item_list if isinstance(item, LightSource)]:
            self.sight = True
            print(f"{self.name} {self.current_room}")
            self.current_room.print_room_items()
        else:
            self.sight = False
            print(f"{self.name} cannot see in the dark. It is pitch black!")
