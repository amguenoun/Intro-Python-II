from room import Room
from player import Player
from item import Item
# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons"),

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

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']

# Add Items to Rooms

room['outside'].add_item(Item('leaf', 'It is a dazzling emerald color.'))
room['foyer'].add_item(
    Item('candle', 'It is currently out. The wax is warm to the touch.'))
room['overlook'].add_item(
    Item('rock', 'It is a round brown rock. Nothing special.'))
room['treasure'].add_item(
    Item('gold coin', 'The golden color inspires visions of wealth.'))
room['treasure'].add_item(
    Item('ruby', 'It is a starling red gem. It might be worth something.'))

#
# Main
#

# Make a new player object that is currently in the 'outside' room.

player = Player("Player 1", room['outside'])

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

print('Welcome to Adventure Game!')
print('type n to move north, s for south, e and w for east and west respectively')
print('q is to quit the game')


def direction_error(direction):
    print(f"\nThere's nothing {direction}, please pick another direction")


def accept_input(action):
    if action == 'q':
        print('Goodbye!')
        exit(0)
    elif action == 'n':
        if player.current_room.n_to == None:
            direction_error("north")
        else:
            player.current_room = player.current_room.n_to
    elif action == 's':
        if player.current_room.s_to == None:
            direction_error("south")
        else:
            player.current_room = player.current_room.s_to
    elif action == 'e':
        if player.current_room.e_to == None:
            direction_error("east")
        else:
            player.current_room = player.current_room.e_to
    elif action == 'w':
        if player.current_room.w_to == None:
            direction_error("west")
        else:
            player.current_room = player.current_room.w_to
    elif action == 'help':
        print('\nn North, s South, e East, w West, q quit')
    else:
        print('\nCommand not recognized. Type help for command list.')


while True:
    print(
        f"\n{player.name} is currently {player.current_room.name}. {player.current_room.description}")

    if len(player.current_room.item_list) == 0:
        print(f'There are no items in this room.')
    else:
        for item in player.current_room.item_list:
            print(f'{player.name} sees a {item.name}. {item.description}')

    action = input(f'What does {player.name} do? --> ')

    accept_input(action)
