# This is an experiment to make maps and display them for the player with /
# some additional functionality also included.

import copy
# from random import randint

# These are the components all rooms are made of.
# Tab these out if you need to see how they look next to one another.
top_wall = " ---------"
top_wall_open = " ---   ---"
bottom_wall = " ---------"
bottom_wall_open = " ---   ---"
side_wall = "|         |"
side_wall_open_left = "          |"
side_wall_open_both = "           "
side_wall_open_right = "|          "
side_wall_here = "|    X    |"
side_wall_open_left_here = "     X    |"
side_wall_open_both_here = "     X     "
side_wall_open_right_here = "|    X     "
side_wall_foe = "|    !    |"
side_wall_open_left_foe = "     !    |"
side_wall_open_both_foe = "     !     "
side_wall_open_right_foe = "|    !     "
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
    side_wall_here,
    side_wall_open_left_here,
    side_wall_open_right_here,
    side_wall_open_both_here,
    side_wall_foe,
    side_wall_open_left_foe,
    side_wall_open_right_foe,
    side_wall_open_both_foe,
    room_null,
]

# These are lists of the components each type of room is made out of, all /
# needed possibilities are represented here.
# Index item 5 can be used to determine which directions it is possible to go /
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


def example_maps(provided_mode):
    if provided_mode == "developer":
        # As examples of what some of these look like:
        print("'closed' room:")
        for item in closed[:5]:
            print(item)
        print("'open_all' room:")
        for item in open_all[:5]:
            print(item)
        print("'null_room' room:")
        for item in null_room[:5]:
            print(item)
    else:
        return


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
map_05_row_0 = null_room, open_bottom, null_room,
map_05_row_1 = open_right, open_all, open_left,
map_05_row_2 = null_room, open_top, null_room,

map_05_composition = map_05_row_0, map_05_row_1, map_05_row_2,

# Creating dictionaries where multiple bits of data can be accessed later
map_01 = {
    'id': "understruts",
    'composition': map_01_composition,
    'danger': "Low",
    'start_pos': [3, 3],
    'enemies': [],
    'weather': [],
}

map_02 = {
    'id': "hat factory",
    'composition': map_02_composition,
    'danger': "Medium",
    'start_pos': [4, 0],
    'enemies': [],
    'weather': [],
}

map_03 = {
    'id': "snake temple",
    'composition': map_03_composition,
    'start_pos': [4, 0],
    'danger': "High",
    'enemies': [],
    'weather': [],
}

map_04 = {
    'id': "test map",
    'composition': map_04_composition,
    'start_pos': [1, 1],
    'danger': "None",
    'enemies': [],
    'weather': [],
}

map_05 = {
    'id': "murder mansion",
    'composition': map_05_composition,
    'start_pos': [1, 1],
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


# TODO: FIX this, it is assigning all similar rooms as changed rooms
def display_position(provided_map, provided_y, provided_x, provided_mode):
    altered_map = copy.deepcopy(provided_map)
    if provided_mode == "developer":
        print("altered:", altered_map)
        print("provided:", provided_map)
    position = copy.deepcopy(altered_map["composition"][provided_y][provided_x])
    position_object = copy.deepcopy(position[2])
    if position_object == side_wall:
        position_object = side_wall_here
    elif position_object == side_wall_open_left:
        position_object = side_wall_open_left_here
    elif position_object == side_wall_open_right:
        position_object = side_wall_open_right_here
    else:
        position_object = side_wall_open_both_here

    # This is an experiment using 'altered_room', doesn't work yet.
    altered_room = [
        altered_map["composition"][provided_y][provided_x][0],
        altered_map["composition"][provided_y][provided_x][1],
        position_object,
        altered_map["composition"][provided_y][provided_x][3],
        altered_map["composition"][provided_y][provided_x][4],
        altered_map["composition"][provided_y][provided_x][5],
    ]

    altered_map["composition"][provided_y][provided_x] = altered_room

    # This is the code that kind of worked.
    # altered_map["composition"][provided_y][provided_x][2] = position_object
    return altered_map


# TODO: Foe system
# To be run with the altered map from 'display_position()' later
# def display_foes_position(provided_map, provided_foe_y, provided_foe_x):
#     altered_map = provided_map
#     # print("altered:", altered_map)
#     # print("provided:", provided_map)
#     position = altered_map["composition"][provided_foe_y][provided_foe_x]
#     position_object = position[2]
#     if position_object == side_wall:
#         position_object = side_wall_foe_here
#     elif position_object == side_wall_open_left:
#         position_object = side_wall_open_left_foe_here
#     elif position_object == side_wall_open_right:
#         position_object = side_wall_open_right_foe_here
#     else:
#         position_object = side_wall_open_both_foe_here
#
#     altered_map["composition"][provided_foe_y][provided_foe_x][2] \
#         = position_object
#     return altered_map


# TODO: Foe system
# def foe_behave(provided_map, foe_y, foe_x):
#     foe_room = provided_map["composition"][foe_y][foe_x]
#     available_directions = len(foe_room[5])
#     foe_choice = randint(0, available_directions)
#     print("The mysterious foe decides to go, ", foe_choice, "!", sep="")
#     while True:
#         if foe_choice == "up":
#             foe_y -= 1
#             new_foe_room = \
#                 provided_map["composition"][foe_y][foe_x]
#             break
#         elif foe_choice == "left":
#             foe_x -= 1
#             new_foe_room = \
#                 provided_map["composition"][foe_y][foe_x]
#             break
#         elif foe_choice == "right":
#             foe_x += 1
#             new_foe_room = \
#                 provided_map["composition"][foe_y][foe_x]
#             break
#         elif foe_choice == "down":
#             foe_y += 1
#             new_foe_room = \
#                 provided_map["composition"][foe_y][foe_x]
#             break
#     return new_foe_room


# TODO: Foe System
# def caught():
#     if current_room == foe_room:
#         print("The mysterious foe catches up to you!")


# 'map_printer()' looks at the map provided to it and generates a string to /
# print for each line of all the rooms in a row. Then it prints this and moves /
# on until all parts of the rooms in a row are printed, then it will move on /
# to the next row until finished.


def map_printer(
        map_provided,
        map_id_provided,
        danger_level,
):
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


# Will only run in "developer" mode.
def iterate_maps(
        provided_mode,
        provided_map_list,
):
    # Iterate through all items from 'map_list' if you need to, this would /
    # probably be done only for debugging, and so never be done in the game:
    if provided_mode == "developer":
        for item in provided_map_list:
            map_printer(item['composition'], item['id'], item['danger'])

        # Or call 'map_printer()' with the specified map you want:
        map_printer(map_01['composition'], map_01['id'], map_01['danger'])
        map_printer(map_02['composition'], map_02['id'], map_02['danger'])
        map_printer(map_03['composition'], map_03['id'], map_03['danger'])
        map_printer(map_04['composition'], map_04['id'], map_04['danger'])
        map_printer(map_05['composition'], map_05['id'], map_05['danger'])
    else:
        return


def display_available(
        provided_room,
):
    print("The following directions are available:")
    # TODO: Fix the last comma appearing with the '.join' method
    for direction in provided_room[5]:
        print(direction, end=", ")


def choose_direction(
        provided_room,
        provided_map,
        provided_y,
        provided_x,
):
    directions = "up", "left", "right", "down",
    while True:
        display_available(
            provided_room,
        )
        print("\nWhich direction would you like to go in?\n"
              "Or, type 'map' to see the map.")
        chosen_direction = input(">>>: ")
        chosen_direction = chosen_direction.casefold()
        if chosen_direction in directions:
            if chosen_direction in provided_room[5]:
                print("You decide to go ", chosen_direction, ".", sep="")
                if chosen_direction == "up":
                    provided_y -= 1
                    new_room = \
                        provided_map["composition"][provided_y][provided_x]
                    break
                elif chosen_direction == "left":
                    provided_x -= 1
                    new_room = \
                        provided_map["composition"][provided_y][provided_x]
                    break
                elif chosen_direction == "right":
                    provided_x += 1
                    new_room = \
                        provided_map["composition"][provided_y][provided_x]
                    break
                elif chosen_direction == "down":
                    provided_y += 1
                    new_room = \
                        provided_map["composition"][provided_y][provided_x]
                    break
            else:
                print("A solid wall blocks your progress in that direction!")
        elif chosen_direction == "map":
            altered_map = display_position(
                provided_map,
                provided_y,
                provided_x,
                mode,
            )
            map_printer(
                altered_map['composition'],
                provided_map['id'],
                provided_map['danger'],
            )
            new_room = provided_map["composition"][provided_y][provided_x]
            continue
        else:
            print("That is not a valid direction.")
    return new_room, provided_y, provided_x


def main_loop(
        provided_room,
        provided_y,
        provided_x,
        provided_mode,
        provided_map_list,
):
    # The following functions only run in "developer" mode.
    example_maps(
        provided_mode,
    )
    iterate_maps(
        provided_mode,
        provided_map_list,
    )
    # Main list, some of these have "developer' mode diagnostics.
    while True:
        provided_room, provided_y, provided_x \
            = choose_direction(
                provided_room,
                current_map,
                provided_y,
                provided_x,
            )
        if provided_mode == "developer":
            print(current_room)
            print("Current_y is:", provided_y)
            print("Current_x is:", provided_x)
        else:
            continue


# Allowing the user to specify "developer" mode or not.
def developer_mode():
    while True:
        print("Would you like to run in developer mode? Y/ N")
        choice = input(">>>: ")
        choice = choice.casefold()
        if choice == "y":
            set_mode = "developer"
            break
        elif choice == "n":
            set_mode = "player"
            break
        else:
            print("That is not a valid choice, please enter again.")
    return set_mode


# Initializing map data and starting position.
current_map = map_01
current_y = current_map["start_pos"][0]
current_x = current_map["start_pos"][1]
current_room = current_map["composition"][current_y][current_x]


# RTP
mode = developer_mode()
main_loop(
    current_room,
    current_y,
    current_x,
    mode,
    map_list,
)
