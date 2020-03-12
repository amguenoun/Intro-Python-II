# Implement a class to hold room information. This should have name and
# description attributes.


class Room:
    def __init__(self, name, description, items=None):
        self.name = name
        self.description = description
        self.n_to = None
        self.s_to = None
        self.e_to = None
        self.w_to = None
        self.item_list = items
        if self.item_list is None:
            self.item_list = []

    def __str__(self):
        return f"current location: {self.name}.\n{self.description}\n"

    def add_item(self, item):
        self.item_list.append(item)

    def remove_item(self, item):
        self.item_list.remove(item)

    def get_room(self, direction):
        if direction == 'n':
            return self.n_to
        if direction == 's':
            return self.s_to
        if direction == 'e':
            return self.e_to
        if direction == 'w':
            return self.w_to

    def print_room_items(self):
        if len(self.item_list) == 0:
            print(f'There are no items in this room.')
        else:
            for item in self.item_list:
                print(f'You see a {item.name}. {item.description}')
