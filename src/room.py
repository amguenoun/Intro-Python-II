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

    def add_item(self, item):
        self.item_list.append(item)
