# Write a class to hold player information, e.g. what room they are in
# currently.


class Player:
    def __init__(self, name, current_room, inventory=None):
        self.name = name
        self.current_room = current_room
        self.inventory = inventory
        if self.inventory is None:
            self.inventory = []

    def take_item(self, target):
        for item in self.current_room.item_list:
            if target.lower() == item.name:
                self.inventory.append(item)
                self.current_room.remove_item(item)
                print(f'{self.name} picks up {item.name}\n')
            else:
                print(f'No {item.name} to pick up.')

    def print_inventory(self):
        if len(self.inventory) == 0:
            print('\nInventory is empty')
        else:
            print(f'\n{self.name} opens their inventory:')
            for item in self.inventory:
                print(item)
            print()

    def travel(self, direction):
        if self.current_room.get_room(direction):
            self.current_room = self.current_room.get_room(direction)
            self.print_player_location()
        else:
            print("There is nothing in that direction")

    def print_player_location(self):
        print(f"{self.name} {self.current_room}")
