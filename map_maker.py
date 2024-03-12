# This is an experiment to make maps and display them for the player, later /
# more functionality would be added so that the room the player is in means /
# something.

# These are the components all rooms are made of, they are not very readable /
# yet but this could be improved in the future.
# Tab these out if you need to see how they look next to one another.
top_wall = " ---------"
top_wall_open = " ---   ---"
bottom_wall = " ---------"
bottom_wall_open = " ---   ---"
side_wall = "|         |"
side_wall_open_left = "          |"
side_wall_open_both = "           "
side_wall_open_right = "|          "
room_null = "          "

# A list of the room components that could be imported etc.
room_components = [
    top_wall,
    top_wall_open,
    bottom_wall,
    bottom_wall_open,
    side_wall,
    side_wall_open_left,
    side_wall_open_both,
    side_wall_open_right,
    room_null,
]

# These are lists of the components each type of room is made out of, all /
# needed possibilities are represented here.
# Index item 6 can be used to determine which directions it is possible to go /
# in while in any specific room.
closed = [
    top_wall,
    side_wall,
    side_wall,
    side_wall,
    bottom_wall,
    [],
]

open_top = [
    top_wall_open,
    side_wall,
    side_wall,
    side_wall,
    bottom_wall,
    ['up', ],
]

open_left = [
    top_wall,
    side_wall,
    side_wall_open_left,
    side_wall,
    bottom_wall,
    ['left', ],
]

open_right = [
    top_wall,
    side_wall,
    side_wall_open_right,
    side_wall,
    bottom_wall,
    ['right', ],
]

open_bottom = [
    top_wall,
    side_wall,
    side_wall,
    side_wall,
    bottom_wall_open,
    ['down', ],
]

open_top_left = [
    top_wall_open,
    side_wall,
    side_wall_open_left,
    side_wall,
    bottom_wall,
    ['up', 'left', ],
]

open_top_right = [
    top_wall_open,
    side_wall,
    side_wall_open_right,
    side_wall,
    bottom_wall,
    ['up', 'right', ],
]

open_top_bottom = [
    top_wall_open,
    side_wall,
    side_wall,
    side_wall,
    bottom_wall_open,
    ['up', 'down', ],
]

open_top_left_right = [
    top_wall_open,
    side_wall,
    side_wall_open_both,
    side_wall,
    bottom_wall,
    ['up', 'left', 'right', ],
]

open_top_left_bottom = [
    top_wall_open,
    side_wall,
    side_wall_open_left,
    side_wall,
    bottom_wall_open,
    ['up', 'left', 'down', ],
]

open_top_right_bottom = [
    top_wall_open,
    side_wall,
    side_wall_open_right,
    side_wall,
    bottom_wall_open,
    ['up', 'right', 'down', ],
]

open_left_right = [
    top_wall,
    side_wall,
    side_wall_open_both,
    side_wall,
    bottom_wall,
    ['left', 'right', ],
]

open_left_bottom = [
    top_wall,
    side_wall,
    side_wall_open_left,
    side_wall,
    bottom_wall_open,
    ['left', 'down', ],
]

open_left_right_bottom = [
    top_wall,
    side_wall,
    side_wall_open_both,
    side_wall,
    bottom_wall_open,
    ['left', 'right', 'down', ],
]

open_right_bottom = [
    top_wall,
    side_wall,
    side_wall_open_right,
    side_wall,
    bottom_wall_open,
    ['right', 'down', ],
]

open_all = [
    top_wall_open,
    side_wall,
    side_wall_open_both,
    side_wall,
    bottom_wall_open,
    ['up', 'left', 'right', 'down', ],
]

null_room = [
    room_null,
    room_null,
    room_null,
    room_null,
    room_null,
    [],
]

# As examples of what some of these look like:
print("'closed' room:")
for item in closed[0:5]:
    print(item)
print("'open_all' room:")
for item in open_all[0:5]:
    print(item)
print("'null_room' room:")
for item in null_room[0:5]:
    print(item)

# A list of all available room types that could be imported etc.
available_rooms = [
    closed,
    open_top,
    open_left,
    open_right,
    open_bottom,
    open_top_left,
    open_top_right,
    open_top_bottom,
    open_top_left_right,
    open_top_left_bottom,
    open_top_right_bottom,
    open_left_right,
    open_left_bottom,
    open_left_right_bottom,
    open_right_bottom,
    open_all,
    null_room,
]

# The map building process:
# Each row of the map has to be built out of the different rooms.
# Each row has to have the same number of rooms otherwise it stops working /
# correctly, this can be fixed later. For now, pad empty spaces with /
# 'null_room's to make the row lengths of all the rows equal.

# map_01: "understruts"
# Definition of which rooms a row consists of from left to right for 'map_01'.
map_01_row_1 = open_right_bottom, open_left_right, open_left_bottom, \
               null_room,
map_01_row_2 = open_top, null_room, open_top_bottom, open_bottom,
map_01_row_3 = open_right, open_left_right_bottom, open_top_left, \
               open_top_bottom,
map_01_row_4 = null_room, open_top_right, open_left_right, open_top_left,

# A composition of the rows in 'map_01' for 'map_printer()' to use.
map_01_composition = map_01_row_1, map_01_row_2, map_01_row_3, map_01_row_4

# Playing around building other maps, it might be easier to plan out maps on /
# excel or something, so the grid is more easily visible, bit this isn't too /
# difficult so far.

# map_02: "hat factory"
map_02_row_1 = open_bottom, open_bottom, null_room, open_bottom,
map_02_row_2 = open_top_bottom, open_top_bottom, open_bottom, open_top_bottom
map_02_row_3 = open_top_bottom, open_top_bottom, open_top_right, \
               open_top_left_bottom
map_02_row_4 = open_top_bottom, open_top_right, open_left_right, \
               open_top_left_bottom
map_02_row_5 = open_top_right, open_left_right, open_left_right, open_top_left

map_02_composition = map_02_row_1, map_02_row_2, map_02_row_3, map_02_row_4, \
                     map_02_row_5

# map_03: "snake temple"
map_03_row_1 = open_right, open_left_right, open_left_bottom,
map_03_row_2 = null_room, null_room, open_top_bottom,
map_03_row_3 = null_room, open_right_bottom, open_top_left,
map_03_row_4 = open_right_bottom, open_top_left, null_room,
map_03_row_5 = open_top, null_room, null_room,

map_03_composition = map_03_row_1, map_03_row_2, map_03_row_3, map_03_row_4, \
                     map_03_row_5

# Creating dictionaries where multiple bits of data can be accessed later /
# more can be added later like the enemies present etc. as needed, not all of /
# this would be accessed by 'map_printer()' but could be used for other /
# functions later.
map_01 = {
    'id': "understruts",
    'composition': map_01_composition,
    'danger': "Low",
    'enemies': [],
    'weather': [],
}

map_02 = {
    'id': "hat factory",
    'composition': map_02_composition,
    'danger': "Medium",
    'enemies': [],
    'weather': [],
}

map_03 = {
    'id': "snake temple",
    'composition': map_03_composition,
    'danger': "High",
    'enemies': [],
    'weather': [],
}

# A list of maps for reference and for iterating through if needed.
map_list = [
    map_01,
    map_02,
    map_03,
]

# 'map_printer()' looks at the map provided to it and generates a string to /
# print for each line of all the rooms in a row. Then it prints this and moves /
# on until all parts of the rooms in a row are printed, then it will move on /
# to the next row until finished.

# I am not actually sure about the 'i <= 3' condition, but it got me the /
# results I wanted, i.e. not leaving a new line between each row of rooms.


def map_printer(map_provided, map_id_provided, danger_level):
    print("\nYou take a look at your map...")
    print("-----------------------------------------------------------------")
    print("You are in the", map_id_provided.title())
    print("The danger level is:", danger_level, "\n")
    for row in map_provided:
        room_print = ""
        for i in range(5):
            for room_object in row:
                room_print += room_object[i] + '\t'
            else:
                if i <= 3:
                    room_print = room_print + "\n"
                else:
                    continue
        print(room_print)
    print("-----------------------------------------------------------------")


# Iterate through all items from 'map_list' if you need to, this would /
# probably be done only for debugging, and so never be done in the game:
for item in map_list:
    map_printer(item['composition'], item['id'], item['danger'])

# Or call 'map_printer()' with the specified map you want:
map_printer(map_03['composition'], map_03['id'], map_03['danger'])
map_printer(map_01['composition'], map_01['id'], map_01['danger'])
map_printer(map_02['composition'], map_02['id'], map_02['danger'])
