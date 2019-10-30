from room import Room
from player import Player

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

#
# Main
#

# Make a new player object that is currently in the 'outside' room.


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
Jamie = Player("Jamie", "outside")


def map():
    for key, value in room.items():
        # print(value)
        if key == Jamie.location:
            print(value)
        # if r[0]==Jamie.location:
        #   current_room.append(r)


map()

while True:
    start = input(
        f"Hark Triton, hark! Bellow, bid our father the Sea King rise from the depths full fowl in his fury! Black waves teeming with salt foam to smother this young mouth with pungent slime. To choke ye, engorging your organs til’ ye turn blue and bloated with bilge and brine and can scream no more only when he, crowned in cockle shells with slitherin’ tentacle tail and steaming beard take up his fell befitted arm, his coral tyne trident screeches banshee-like in the tempest and plunges right through yer gullet bursting ye -- a bulging blacker no more, but a blasted bloody film now and nothing for the harpies and the souls of dead sailors to peck and claw and feed upon only to be lapped up and swallowed by the infinite waters of the Dread Emperor himself. Forgotten to any man, to any time, forgotten to any god or devil, forgotten even to the sea, for any stuff for part of {Jamie.name}, even any scantling of your soul is {Jamie.name} no more, but is now itself the sea! \n ...Anyway, you see a cave mount in a northernly direction! Do you check it out?")
