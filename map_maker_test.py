# This is a system to make maps and display them for the player with /
# the ability to move around the map and track the player's position.

# Functions have been ordered in the loose order they are called by the program.
from random import random
from game_maps_test import *


# Displays instructions to the player at game start.
def how_to_play():
    print("\nHOW TO PLAY:")
    print("In this game you are investigating a series of grizzly murders in"
          " several high-profile locations.")
    print("Find the evidence, without being discovered by the mysterious "
          "killer!")
    print("The following controls are available:\n"
          "'map' - displays the map.\n"
          "'wait' - don't move for one turn.\n"
          "'up' - go up if possible.\n"
          "'left' - go left if possible.\n"
          "'right' - go right if possible.\n"
          "'down' - go down if possible.\n"
          "'quit' - exits the game.\n")


# Allows the user to specify "developer" mode or not, which displays /
# diagnostic information in some functions.
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
# Allows the user to choose what map/ game type they want to play.
def choose_game(
        provided_map_list
):
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
def initialize_map(
        provided_current_map
):
    initial_y = provided_current_map["start_pos"][0]
    initial_x = provided_current_map["start_pos"][1]
    initial_room = provided_current_map["composition"][initial_y][initial_x]
    return initial_room, initial_y, initial_x


# Displays some examples of what rooms should look like in "developer" mode.
def example_maps(
        provided_mode
):
    if provided_mode == "developer":
        print("Some examples of what some of the rooms look like:")
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
        provided_foe_y,
        provided_foe_x,
):
    if provided_mode == "developer":
        for item in provided_map_list:
            map_printer(
                item['composition'],
                item['id'],
                item['danger'],
                current_y,
                current_x,
                provided_foe_y,
                provided_foe_x,
            )


# TODO: Add a win condition to allow an end to the game.
# Allows the game to run until a win, lose, or exit condition has been met.
def main_loop(
        provided_room,
        provided_y,
        provided_x,
        provided_mode,
        provided_map_list,
        provided_foe_y,
        provided_foe_x,
):
    # The following functions only produce output in "developer" mode.
    example_maps(
        provided_mode,
    )
    iterate_maps(
        provided_mode,
        provided_map_list,
        provided_foe_y,
        provided_foe_x,
    )
    # Main list, some of these have "developer" mode diagnostics.
    # 'caught()' is run both after the player's turn and the foe's turn to /
    # cover all possible situations where they inhabit the same room.
    while True:
        provided_room, provided_y, provided_x \
            = choose_direction(
                provided_room,
                current_map,
                provided_y,
                provided_x,
                provided_foe_y,
                provided_foe_x,
            )
        provided_y, provided_x, caught_flag = caught(
            provided_y,
            provided_x,
            provided_foe_y,
            provided_foe_x,
            current_map,
        )
        provided_foe_y, provided_foe_x = foe_behave(
            current_map,
            provided_foe_y,
            provided_foe_x,
            mode,
            caught_flag,
        )
        provided_y, provided_x, caught_flag = caught(
            provided_y,
            provided_x,
            provided_foe_y,
            provided_foe_x,
            current_map,
        )
        if provided_mode == "developer":
            print(current_room)
            print("Current_y is:", provided_y)
            print("Current_x is:", provided_x)
        else:
            continue


# TODO: Make this work with the first letter of each direction as well
# Allows the player to move around between the rooms of a map.
def choose_direction(
        provided_room,
        provided_map,
        provided_y,
        provided_x,
        provided_foe_y,
        provided_foe_x,
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
                provided_foe_y,
                provided_foe_x,
            )
        elif chosen_direction == "wait":
            new_room = provided_map["composition"][provided_y][provided_x]
            print("You decide to hide in this room and wait a while...")
            break
        elif chosen_direction == "quit":
            print("See you soon!")
            exit()
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


# Streamlines 'display_position()' in previous builds and can also be used to /
# display the enemy position as well.
def position_check(
        provided_y,
        provided_x,
        working_y,
        working_x,
        provided_foe_y,
        provided_foe_x,
):
    if provided_y == working_y and provided_x == working_x:
        middle_room_object = "X"
    elif provided_foe_y == working_y and provided_foe_x == working_x:
        middle_room_object = "!"
    else:
        middle_room_object = " "
    return middle_room_object


# Prints a map by adding rows of room elements to a print string for each row /
# of rooms in the current map.
def map_printer(
        provided_map,
        provided_map_id,
        provided_danger_level,
        provided_y,
        provided_x,
        provided_foe_y,
        provided_foe_x,
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
                            provided_foe_y,
                            provided_foe_x,
                        )
                    new_room_object = room_object[i][:5] + middle_object \
                        + room_object[i][5:]
                    room_print += new_room_object + '\t'
            elif i >= 3:
                for room_object in row:
                    room_print += room_object[i] + '\t'
            if i <= 3:
                room_print = room_print + "\n"
        else:
            print(room_print)
    print("-----------------------------------------------------------------")
    return current_y, current_x


# TODO: Make and implement the 'foe_system'


# Provides co-ordinates for where the foe start the game on each map.
def initialize_foe_position(
        provided_map
):
    initial_foe_y = provided_map['foe_start'][0]
    initial_foe_x = provided_map['foe_start'][1]
    return initial_foe_y, initial_foe_x


# Determines the direction the foe takes each turn and ensures it is a valid /
# direction, the foe does not move directly after a player escape.
def foe_behave(
        provided_map,
        provided_foe_y,
        provided_foe_x,
        provided_mode,
        caught_flag,
):
    foe_room = provided_map["composition"][provided_foe_y][provided_foe_x]
    if caught_flag != 1:
        try:
            available_directions = len(foe_room[5])
            if provided_mode == "developer":
                random_float = random()
                foe_choice = int(random_float * available_directions)
                for i in range(11):
                    random_float = random()
                    foe_choice = int(random_float * available_directions)
                    print(foe_choice)
                else:
                    print(available_directions)
                    print(len(foe_room[5]))
                    print(foe_room[5])
                    print(foe_choice)
                    choice_made = foe_room[5][foe_choice]
                    print(choice_made)

            random_float = random()
            foe_choice = int(random_float * available_directions)
            choice_made = foe_room[5][foe_choice]

            print("The mysterious foe decides to go ", choice_made, "!", sep="")
            while True:
                if choice_made == "up":
                    provided_foe_y -= 1
                    break
                elif choice_made == "left":
                    provided_foe_x -= 1
                    break
                elif choice_made == "right":
                    provided_foe_x += 1
                    break
                elif choice_made == "down":
                    provided_foe_y += 1
                    break
        except IndexError:
            print("The mysterious foe bides their time...")
    else:
        print("The mysterious foe bides their time...")
    return provided_foe_y, provided_foe_x


# Handles situations where the player and foe end up in the same place, the /
# player either dies or gets away from the foe.
def caught(
        provided_y,
        provided_x,
        provided_foe_y,
        provided_foe_x,
        provided_map,
):
    caught_flag = 0
    if provided_y == provided_foe_y and provided_x == provided_foe_x:
        print("The mysterious foe catches up to you!")
        input(">>>:")
        print("They reach out their hands...")
        input(">>>:")
        caught_chance = random().__round__()
        if caught_chance == 1:
            print("But you manage to slip away!")
            provided_y, provided_x \
                = forced_move(provided_map, provided_y, provided_x)
            caught_flag = 1
        else:
            print("You cannot get away!")
            print("The mysterious foe chokes the life out of you!\n")
            input(">>>:")
            print("GAME OVER!")
            exit()
    return provided_y, provided_x, caught_flag


# Forcibly moves the player by one valid space if they manage to get away from /
# the foe, the foe does not move again that turn in this case.
def forced_move(
        provided_map,
        provided_y,
        provided_x,
):
    danger_room = provided_map["composition"][provided_y][provided_x]
    available_directions = len(danger_room[5])
    random_float = random()
    panic_choice = int(random_float * available_directions)
    choice_made = danger_room[5][panic_choice]

    print("You manage to run ", choice_made, "!", sep="")
    while True:
        if choice_made == "up":
            provided_y -= 1
            break
        elif choice_made == "left":
            provided_x -= 1
            break
        elif choice_made == "right":
            provided_x += 1
            break
        elif choice_made == "down":
            provided_y += 1
            break
    return provided_y, provided_x


# TODO: Add a 'turns_taken' function to determine things about foe behavior.


# RTP, this code calls the functions to set up the game and get it going.
mode = developer_mode()
current_map = choose_game(
    map_list
)
current_room, current_y, current_x = initialize_map(
    current_map
)
foe_y, foe_x = initialize_foe_position(
    current_map
)
how_to_play()
map_printer(
    current_map['composition'],
    current_map['id'],
    current_map['danger'],
    current_y,
    current_x,
    foe_y,
    foe_x,
)
main_loop(
    current_room,
    current_y,
    current_x,
    mode,
    map_list,
    foe_y,
    foe_x,
)
