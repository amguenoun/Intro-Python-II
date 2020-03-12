from room import Room
from player import Player
from item import Item, LightSource
# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons", True),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),
}


# Link rooms together

room['outside'].connect_room(room['foyer'], 'n')
room['foyer'].connect_room(room['overlook'], 'n')
room['foyer'].connect_room(room['narrow'], 'e')
room['narrow'].connect_room(room['treasure'], 'n')

# Add Items to Rooms

room['outside'].add_item(Item('leaf', 'It is a dazzling emerald color.'))
room['outside'].add_item(
    LightSource('lamp', 'The light from the lamp brightens your spirit in this dark world.'))
room['foyer'].add_item(
    Item('candle', 'It is currently out. The wax is warm to the touch.'))
room['overlook'].add_item(
    Item('rock', 'It is a round brown rock. Nothing special.'))
room['treasure'].add_item(
    Item('gold', 'The golden color inspires visions of wealth.'))
room['treasure'].add_item(
    Item('ruby', 'It is a starling red gem. It might be worth something.'))

#
# Main
#

# Make a new player object that is currently in the 'outside' room.
player = Player(input('Enter Player Name: '), room['outside'])
print(
    f"\n{player.name} current Location: {player.current_room.name}.\n{player.current_room.description}\n")
player.current_room.print_room_items()
# Write a loop that:
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.

valid_directions = ("n", "s", "e", "w")
valid_verbs = ('get', 'take', 'drop')


def accept_input(action):
    print('----------')
    if len(action) == 1:
        if action[0] == 'q':
            print('Goodbye!')
            exit(0)
        elif action[0] in valid_directions:
            player.travel(action[0])
        elif action[0] == 'help':
            print(
                'Directions: n, s, e, w. Quit: q, Items: get/take/drop [item], Inventory:  i/inventory')
        elif action[0] == 'i' or action[0] == 'inventory':
            player.print_inventory()
        else:
            print('\nCommand not recognized. Type help for command list.')
    elif len(action) == 2:
        if action[0] in valid_verbs:
            if action[0] in ('get', 'take'):
                player.take_item(action[1])
                player.print_player_location()
            elif action[0] == 'drop':
                player.drop_item(action[1])
                player.print_player_location()
        else:
            print('\nCommand not recognized. Type help for command list.')


while True:
    action = input(f'What does {player.name} do? --> ').lower().split(" ")
    accept_input(action)
