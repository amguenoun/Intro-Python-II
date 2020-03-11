# Write a class to hold player information, e.g. what room they are in
# currently.


class Player:
    def __init__(self, name, current_room, inventory=None):
        self.name = name
        self.current_room = current_room
        self.inventory = inventory
        if self.inventory is None:
            self.inventory = []

    def add_item(self, item):
        self.inventory.append(item)
