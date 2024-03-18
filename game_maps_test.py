# Maps and map components that can be used for games.

wall_object = " "

top_wall = " ---------"
top_wall_open = " ---   ---"
bottom_wall = " ---------"
bottom_wall_open = " ---   ---"
side_wall = "|         |"
side_wall_both_closed = "|        |"
side_wall_open_left = "         |"
side_wall_open_both = "         "
side_wall_open_right = "|         "
room_null = "        "

# A list of the room components that could be imported etc.
room_components = [
    top_wall,
    top_wall_open,
    bottom_wall,
    bottom_wall_open,
    side_wall,
    side_wall_both_closed,
    side_wall_open_left,
    side_wall_open_both,
    side_wall_open_right,
    room_null,
]

# These are lists of the components each type of room is made out of, all /
# needed possibilities are represented here.
# Index item 5 can be used to determine which directions it is possible to go /
# in while in any specific room.
closed = [
    top_wall,
    side_wall,
    side_wall_both_closed,
    side_wall,
    bottom_wall,
    [],
]

open_top = [
    top_wall_open,
    side_wall,
    side_wall_both_closed,
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
    side_wall_both_closed,
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
    side_wall_both_closed,
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
# Each row has to have the same number of rooms otherwise it stops working.
# Pad empty spaces with 'null_room's to make the row lengths of all the rows /
# equal.

# map_01: "understruts"
# Definition of which rooms a row consists of from left to right for 'map_01'.
map_01_row_0 = open_right_bottom, open_left_right, open_left_bottom, \
               null_room,
map_01_row_1 = open_top, null_room, open_top_bottom, open_bottom,
map_01_row_2 = open_right, open_left_right_bottom, open_top_left, \
               open_top_bottom,
map_01_row_3 = null_room, open_top_right, open_left_right, open_top_left,

# A composition of the rows in 'map_01' for 'map_printer()' to use.
map_01_composition = map_01_row_0, map_01_row_1, map_01_row_2, map_01_row_3

# map_02: "hat factory"
map_02_row_0 = open_bottom, open_bottom, null_room, open_bottom,
map_02_row_1 = open_top_bottom, open_top_bottom, open_bottom, open_top_bottom
map_02_row_2 = open_top_bottom, open_top_bottom, open_top_right, \
               open_top_left_bottom
map_02_row_3 = open_top_bottom, open_top_right, open_left_right, \
               open_top_left_bottom
map_02_row_4 = open_top_right, open_left_right, open_left_right, open_top_left

map_02_composition = map_02_row_0, map_02_row_1, map_02_row_2, map_02_row_3, \
                     map_02_row_4

# map_03: "snake temple"
map_03_row_0 = open_right, open_left_right, open_left_bottom,
map_03_row_1 = null_room, null_room, open_top_bottom,
map_03_row_2 = null_room, open_right_bottom, open_top_left,
map_03_row_3 = open_right_bottom, open_top_left, null_room,
map_03_row_4 = open_top, null_room, null_room,

map_03_composition = map_03_row_0, map_03_row_1, map_03_row_2, map_03_row_3, \
                     map_03_row_4

# map_04: "test map"
map_04_row_0 = null_room, open_bottom, null_room,
map_04_row_1 = open_right, open_all, open_left,
map_04_row_2 = null_room, open_top, null_room,

map_04_composition = map_04_row_0, map_04_row_1, map_04_row_2,

# map_05: 'murder mansion'
map_05_row_0 = open_bottom, null_room, null_room, null_room, \
               open_right_bottom, open_left_right, open_left_bottom,
map_05_row_1 = open_top_bottom, null_room, open_right_bottom, \
               open_left_right_bottom, open_top_left, null_room, open_top_bottom
map_05_row_2 = open_top_right_bottom, open_left_right, open_top_left_right, \
               open_all, open_left, null_room, open_top_bottom
map_05_row_3 = open_top_bottom, null_room, null_room, open_top_bottom, \
               null_room, open_bottom, open_top_bottom
map_05_row_4 = open_top_right_bottom, open_left_right_bottom, \
               open_left_right, open_all, open_left_right_bottom, open_all, \
               open_top_left_bottom
map_05_row_5 = open_top_right, open_top_left, null_room, \
               open_top_right_bottom, open_top_left, open_top_right, \
               open_top_left_bottom
map_05_row_6 = null_room, null_room, null_room, open_top_bottom, null_room, \
               null_room, open_top

map_05_composition = map_05_row_0, map_05_row_1, map_05_row_2, map_05_row_3, \
                     map_05_row_4, map_05_row_5, map_05_row_6

# TODO: Work on this discoverable map system and make it work in 'map_maker.py'
# murder mansion discoverable map
# The intention for this map is to show the player and then update this map \
# with new rooms by updating it from map_05
map_05_row_0_d = null_room, null_room, null_room, null_room, null_room, \
                 null_room, null_room
map_05_row_1_d = null_room, null_room, null_room, null_room, null_room, \
                 null_room, null_room
map_05_row_2_d = null_room, null_room, null_room, null_room, null_room, \
                 null_room, null_room
map_05_row_3_d = null_room, null_room, null_room, null_room, null_room, \
                 null_room, null_room
map_05_row_4_d = null_room, null_room, null_room, null_room, null_room, \
                 null_room, null_room
map_05_row_5_d = null_room, null_room, null_room, null_room, null_room, \
                 null_room, null_room
map_05_row_6_d = null_room, null_room, null_room, open_top_bottom, null_room, \
                 null_room, null_room

map_05_d_composition = map_05_row_0_d, map_05_row_1_d, map_05_row_2_d, \
                       map_05_row_3_d, map_05_row_4_d, map_05_row_5_d, \
                       map_05_row_6_d

# Creating dictionaries where multiple bits of data can be accessed later
map_01 = {
    'id': "understruts",
    'composition': map_01_composition,
    'danger': "Low",
    'start_pos': [3, 3],
    'foe_start': [0, 0],
    'foe_appear': 2,
    'enemies': [],
    'weather': [],
}

map_02 = {
    'id': "hat factory",
    'composition': map_02_composition,
    'danger': "Medium",
    'start_pos': [4, 0],
    'foe_start': [0, 0],
    'foe_appear': 3,
    'enemies': [],
    'weather': [],
}

map_03 = {
    'id': "snake temple",
    'composition': map_03_composition,
    'start_pos': [4, 0],
    'foe_start': [0, 0],
    'foe_appear': 2,
    'danger': "High",
    'enemies': [],
    'weather': [],
}

map_04 = {
    'id': "test map",
    'composition': map_04_composition,
    'start_pos': [1, 1],
    'foe_start': [1, 2],
    'foe_appear': 1,
    'danger': "None",
    'enemies': [],
    'weather': [],
}

map_05 = {
    'id': "murder mansion",
    'composition': map_05_composition,
    'discoverable': map_05_d_composition,
    'start_pos': [6, 3],
    'foe_start': [0, 0],
    'foe_appear': 5,
    'danger': "Impending",
    'enemies': [],
    'weather': [],
}
# A list of maps for reference and for iterating through if needed.
map_list = [
    map_01,
    map_02,
    map_03,
    map_04,
    map_05,
]
