class Monster:
    def __init__(self, name, description, room, health, attack, skill):
        self.name = name
        self.description = description
        self.room = room
        self.health = health
        self.skill = skill

    def on_death(self):
        print(f'{self.name} has died!')

    def on_damage(self, dmg):
        if health - dmg <= 0:
            self.on_death
        else:
            health -= dmg
