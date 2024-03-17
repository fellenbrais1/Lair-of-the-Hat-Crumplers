# This is an experiment to make maps and display them for the player with /
# some additional functionality also included.

# Functions have been ordered in the loose order they are called by the program.
# import copy

from game_maps_test import *


# TODO: Uncomment this later for use in the 'foe_system'.
# from random import randint


# Allowing the user to specify "developer" mode or not, which displays /
# diagnostic information.
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


# TODO: Add the option to choose a game type on each map when this is ready.
# Allowing the user to choose what map/ game type they want to play.
def choose_game(provided_map_list):
    print("Which map would you like to play on?\n")
    i = 1
    choices = []
    for item in provided_map_list:
        item_name = item['id']
        item_name = item_name.title()
        print(i, ". ", item_name, sep="")
        choices.append(i)
        i += 1
    while True:
        print("\nPlease enter your choice by typing that number. "
              "Or, type 'D' to redisplay the choices or 'X' to quit.")
        choice = input(">>>: ")
        try:
            if int(choice) in choices:
                choice = int(choice)
                chosen_map = map_list[choice - 1]
                break
            else:
                print("Please enter a choice from the list of available maps "
                      "by typing the number of the one you want to play on.")
        except ValueError:
            if choice.casefold() == "d":
                choices = []
                for item in provided_map_list:
                    item_name = item['id']
                    item_name = item_name.title()
                    print(i, ". ", item_name, sep="")
                    choices.append(i)
                    i += 1
            if choice.casefold() == "x":
                print("Okay, see you some other time!")
                exit()

    return chosen_map


# Sets up the map and starting co-ordinates when the game starts.
def initialize_map(provided_current_map):
    initial_y = provided_current_map["start_pos"][0]
    initial_x = provided_current_map["start_pos"][1]
    initial_room = provided_current_map["composition"][initial_y][initial_x]
    return initial_room, initial_y, initial_x


# Displays some examples of what rooms should look like in "developer" mode.
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


# Shows all or some of the maps in 'map_list' when in "developer" mode.
def iterate_maps(
        provided_mode,
        provided_map_list,
):
    # Iterate through all items from 'map_list' if you need to, this would /
    # probably be done only for debugging, and so never be done in the game.
    if provided_mode == "developer":
        for item in provided_map_list:
            map_printer(
                item['composition'],
                item['id'],
                item['danger'],
                current_y,
                current_x,
            )

        # Or call 'map_printer()' with the specified map you want:
        map_printer(
            map_01['composition'],
            map_01['id'],
            map_01['danger'],
            current_y,
            current_x,
        )
        map_printer(
            map_02['composition'],
            map_02['id'],
            map_02['danger'],
            current_y,
            current_x,
        )
        map_printer(
            map_03['composition'],
            map_03['id'],
            map_03['danger'],
            current_y,
            current_x,
        )
        map_printer(
            map_04['composition'],
            map_04['id'],
            map_04['danger'],
            current_y,
            current_x,
        )
        map_printer(
            map_05['composition'],
            map_05['id'],
            map_05['danger'],
            current_y,
            current_x,
        )


# TODO: Add win, lose, exit conditions to allow an end to the game.
# Allows the game to run until a win, lose, or exit condition has been met.
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
    # Main list, some of these have "developer" mode diagnostics.
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


# Allows the player to move around between the rooms of a map.
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
            map_printer(
                provided_map['composition'],
                provided_map['id'],
                provided_map['danger'],
                provided_y,
                provided_x,
            )
            new_room = provided_map["composition"][provided_y][provided_x]
            continue
        else:
            print("That is not a valid direction.")
    return new_room, provided_y, provided_x


# Displays available directions you can take from a room.
def display_available(
        provided_room,
):
    print("The following directions are available:")
    # TODO: Fix the last comma appearing with the '.join' method
    for direction in provided_room[5]:
        print(direction, end=", ")


# This function streamlines the display_position as seen before and can also /
# be used to display the enemy position as well (in theory).
# EDIT: Jesus Christ this was a pain to do.
def position_check(
        provided_y,
        provided_x,
        working_y,
        working_x,
):
    if provided_y == working_y and provided_x == working_x:
        middle_room_object = "X"
    # elif provided_foe_room == provided_map[provided_y][provided_x]:
    #     provided_wall_object = "!"
    else:
        middle_room_object = " "
    return middle_room_object


# 'map_printer()' looks at the map provided to it and generates a string to /
# print for each line of all the rooms in a row. Then it prints this and moves /
# on until all parts of the rooms in a row are printed, then it will move on /
# to the next row until finished.
def map_printer(
        provided_map,
        provided_map_id,
        provided_danger_level,
        provided_y,
        provided_x,
):
    print("\nYou take a look at your map...")
    print("-----------------------------------------------------------------")
    print("You are in the", provided_map_id.title())
    print("The danger level is:", provided_danger_level, "\n")
    for index, row in enumerate(provided_map):
        room_print = ""
        working_y = index
        for i in range(5):
            if i <= 1:
                for room_object in row:
                    room_print += room_object[i] + '\t'
            elif i == 2:
                for room_index, room_object in enumerate(row):
                    working_x = room_index
                    middle_object \
                        = position_check(
                            provided_y,
                            provided_x,
                            working_y,
                            working_x,
                        )
                    new_room_object = room_object[i][:5] + middle_object \
                        + room_object[i][5:]
                    room_print += new_room_object + '\t'
            elif i >= 3:
                for room_object in row:
                    room_print += room_object[i] + '\t'
            if i <= 3:
                room_print = room_print + "\n"
            # print(game_maps_test.wall_object)
        else:
            # print(game_maps_test.wall_object)
            print(room_print)
    print("-----------------------------------------------------------------")
    return current_y, current_x

# TODO: Make and implement the 'foe_system'
# TODO: foe_system
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


# TODO: foe_system
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


# TODO: foe_system
# def caught():
#     if current_room == foe_room:
#         print("The mysterious foe catches up to you!")


# TODO: Add a 'turns_taken' function to determine when the foe will appear and /
# TODO: other things like how fast it will move etc.


# RTP, this code calls the functions to set up the game and get it going.
mode = developer_mode()
current_map = choose_game(map_list)
current_room, current_y, current_x = initialize_map(current_map)
main_loop(
    current_room,
    current_y,
    current_x,
    mode,
    map_list,
)
