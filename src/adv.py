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

room['outside'].items = [
    Item("Goldfish", "A chonky, floppy fishy babe. You think it's a calico oranda.")]
room['foyer'].items = [
    Item("Cat", "A fluffy cat with a squishy face. It mrows and chirps gently.")]
room['overlook'].items = [Item(
    "Turtle", "A serene looking semi-aquatic turtle. Probably a yellow-bellied slider.")]
room['narrow'].items = [
    Item("Sword", "An iron sword orange with rust... or blood?")]
room['treasure'].items = ["Eyeball", "A gooey eyeball."]
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
Jamie = Player("Jamie", room["outside"])
current_location = None
Jamie.backpack = []

print('Choose a direction (n,s,e, or w), look around (l), pick up an item you find (p), drop an item (d), or quit the game by pressing q!\n')
playing = True
while playing:
    for key, value in room.items():
        # print(value.name)
        if value.name == Jamie.location.name:
            print(value)
            current_location = value
    move = input(f"\nWhich direction should we head, {Jamie.name}?\n")
    if move == "n":
        if Jamie.location.n_to == None:
            print("\nWe can't go there!")
        else:
            Jamie.location = Jamie.location.n_to
    if move == "s":
        if Jamie.location.s_to == None:
            print("\nWe can't go there!")
        else:
            Jamie.location = Jamie.location.s_to
            print
    if move == "e":
        if Jamie.location.e_to == None:
            print("\nWe can't go there!")
        else:
            Jamie.location = Jamie.location.e_to
    if move == "w":
        if Jamie.location.w_to == None:
            print("\nWe can't go there!")
        else:
            Jamie.location = Jamie.location.w_to
    if move == "q":
        print(
            f"\n Hark Triton, hark! Bellow, bid our father the Sea King rise from the depths full fowl in his fury! Black waves teeming with salt foam to smother this young mouth with pungent slime. To choke ye, engorging your organs til’ ye turn blue and bloated with bilge and brine and can scream no more only when he, crowned in cockle shells with slitherin’ tentacle tail and steaming beard take up his fell befitted arm, his coral tyne trident screeches banshee-like in the tempest and plunges right through yer gullet bursting ye -- a bulging blacker no more, but a blasted bloody film now and nothing for the harpies and the souls of dead sailors to peck and claw and feed upon only to be lapped up and swallowed by the infinite waters of the Dread Emperor himself. Forgotten to any man, to any time, forgotten to any god or devil, forgotten even to the sea, for any stuff for part of {Jamie.name}, even any scantling of your soul is {Jamie.name} no more, but is now itself the sea!")
        playing = False
    if move == "l":
        print("\nYou look around for anything useful!\n",
              Jamie.location.items)
    if move == "p":
        if len(Jamie.location.items) > 0:
            selectable = []
            for item in Jamie.location.items:
                selectable.append(item)
            selection = input("\nPick up an item to add to your backpack!\n")
            if selection:
                for item in selectable:
                    if selection == item.name:
                        Jamie.get_item(item)
                        Jamie.location.drop_item(item)
                        print(
                            f"\nYou deposit the {selection} into your backpack for safekeeping\n")
        else:
            print("\nThere's nothing useful here!\n")
    if move == "d":
        if len(Jamie.backpack) > 0:
            print("\nHere's what's in your backpack: \n", Jamie.backpack)
            selectable = []
            for item in Jamie.backpack:
                selectable.append(item)
            selection = input("\nChoose an item to drop!")
            if selection:
                for item in selectable:
                    if selection == item.name:
                        Jamie.drop_item(item)
                        Jamie.location.get_item(item)
                        print(
                            f"\nYou remove the {selection} from your backpack and toss it aside!\n")
        else:
            print("\n There's nothing in your backpack!\n")
