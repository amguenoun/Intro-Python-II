class Item:
    def __init__(self, name, description):
        self.name = name
        self.description = description

    def __str__(self):
        return f"{self.name.upper()}: {self.description}"

    def on_take(self, p_name):
        print(f'{p_name} picks up {self.name}\n')

    def on_drop(self, p_name):
        print(f'{p_name} drops {self.name}\n')


class LightSource(Item):
    def __init__(self, name, description):
        super().__init__(name, description)


class Weapon(Item):
    def __init__(self, name, description, attack):
        super().__init__(name, description)
        self.attack = attack
