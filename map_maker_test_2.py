# This is a system to make maps and display them for the player with /
# the ability to move around the map and track the player's position.

# Functions have been ordered in the loose order they are called by the program.
import copy
from random import random, randint
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
          "'quit' - exits the game.")
    input(">>>:")
    print("\n")


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
        provided_map_list,
):
    print("\nWhich map would you like to play on?\n")
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
        provided_current_map,
):
    initial_y = provided_current_map["start_pos"][0]
    initial_x = provided_current_map["start_pos"][1]
    initial_room = provided_current_map["composition"][initial_y][initial_x]
    initial_foe_appear = provided_current_map["foe_appear"]
    initial_d_map = provided_current_map["discoverable"]
    return initial_room, initial_y, initial_x, initial_foe_appear, \
        initial_d_map


# Displays some examples of what rooms should look like in "developer" mode.
def example_maps(
        provided_mode,
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
        provided_turn_count,
        provided_foe_appear,
        provided_d_map,
        provided_foe_status,
):
    if provided_mode == "developer":
        for item in provided_map_list:
            map_printer(
                item['id'],
                item['danger'],
                current_y,
                current_x,
                provided_foe_y,
                provided_foe_x,
                provided_turn_count,
                provided_foe_appear,
                provided_d_map,
                provided_foe_status,
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
        provided_turn_count,
        provided_foe_appear,
        provided_d_map,
        provided_last_move,
        provided_foe_status,
        provided_reappear_count,
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
        provided_turn_count,
        provided_foe_appear,
        provided_d_map,
        provided_foe_status,
    )
    # Main list, some of these have "developer" mode diagnostics.
    # 'caught()' is run both after the player's turn and the foe's turn to /
    # cover all possible situations where they inhabit the same room.
    while True:
        provided_room, provided_y, provided_x, \
            = choose_direction(
                provided_room,
                current_map,
                provided_y,
                provided_x,
                provided_foe_y,
                provided_foe_x,
                provided_turn_count,
                provided_foe_appear,
                provided_d_map,
                provided_foe_status,
            )
        provided_d_map = map_discover(
            current_map,
            provided_d_map,
            provided_y,
            provided_x,
        )
        if provided_turn_count >= provided_foe_appear:
            provided_room, provided_y, provided_x, caught_flag = caught(
                provided_y,
                provided_x,
                provided_foe_y,
                provided_foe_x,
                current_map,
                provided_d_map,
                provided_foe_status,
            )
            provided_foe_y, provided_foe_x, provided_last_move, \
                provided_foe_status, provided_reappear_count \
                = foe_behave(
                    current_map,
                    provided_foe_y,
                    provided_foe_x,
                    mode,
                    provided_last_move,
                    caught_flag,
                    provided_turn_count,
                    provided_foe_status,
                    provided_y,
                    provided_x,
                    provided_reappear_count,
                )
            provided_room, provided_y, provided_x, caught_flag = caught(
                provided_y,
                provided_x,
                provided_foe_y,
                provided_foe_x,
                current_map,
                provided_d_map,
                provided_foe_status,
            )
        else:
            pass
        # Turn count updater.
        provided_d_map = map_discover(
            current_map,
            provided_d_map,
            provided_y,
            provided_x,
        )
        provided_turn_count = turn_counter(
            provided_turn_count,
        )
        foe_appearance(
            provided_turn_count,
            provided_foe_appear,
        )
        if provided_mode == "developer":
            print(current_room)
            print("Current_y is:", provided_y)
            print("Current_x is:", provided_x)
        else:
            continue


# TODO: Create a condition to allow an exit room for use at game end.
# Allows the player to move around between the rooms of a map.
def choose_direction(
        provided_room,
        provided_map,
        provided_y,
        provided_x,
        provided_foe_y,
        provided_foe_x,
        provided_turn_count,
        provided_foe_appear,
        provided_d_map,
        provided_foe_status,
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
        # Converting single letter strings into valid choices for processing.
        if chosen_direction == "u":
            chosen_direction = "up"
        if chosen_direction == "l":
            chosen_direction = "left"
        if chosen_direction == "r":
            chosen_direction = "right"
        if chosen_direction == "d":
            chosen_direction = "down"
        if chosen_direction == "m":
            chosen_direction = "map"
        if chosen_direction == "w":
            chosen_direction = "wait"
        if chosen_direction == "q":
            chosen_direction = "quit"
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
                provided_map['id'],
                provided_map['danger'],
                provided_y,
                provided_x,
                provided_foe_y,
                provided_foe_x,
                provided_turn_count,
                provided_foe_appear,
                provided_d_map,
                provided_foe_status,
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
        provided_turn_count,
        provided_foe_appear,
        provided_foe_status,
):
    if provided_y == working_y and provided_x == working_x:
        middle_room_object = "X"
    elif provided_foe_y == working_y and provided_foe_x == working_x:
        if provided_turn_count >= provided_foe_appear:
            if provided_foe_status == 'gone':
                middle_room_object = " "
            else:
                middle_room_object = "!"
        else:
            middle_room_object = " "
    else:
        middle_room_object = " "
    return middle_room_object


# Prints a map by adding rows of room elements to a print string for each row /
# of rooms in the current map.
def map_printer(
        provided_map_id,
        provided_danger_level,
        provided_y,
        provided_x,
        provided_foe_y,
        provided_foe_x,
        provided_turn_count,
        provided_foe_appear,
        provided_d_map,
        provided_foe_status,
):
    if provided_turn_count == 0:
        print("Welcome to the ", provided_map_id.title(), sep="")
        print("---------------------------------------------------------------"
              "--------------------")
        print("The danger level is:", provided_danger_level, "\n")
    else:
        print("\nYou take a look at your map...")
        print("---------------------------------------------------------------"
              "--------------------")
        print("You are in the", provided_map_id.title())
        print("The danger level is:", provided_danger_level, "\n")
    for index, row in enumerate(provided_d_map):
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
                            provided_turn_count,
                            provided_foe_appear,
                            provided_foe_status,
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
    print("-------------------------------------------------------------------"
          "----------------")
    return provided_y, provided_x


# TODO: Add a second late game foe to the 'foe_system' triggered by all clues.


# Provides co-ordinates for where the foe start the game on each map.
def initialize_foe_position(
        provided_map,
):
    initial_foe_y = provided_map['foe_start'][0]
    initial_foe_x = provided_map['foe_start'][1]
    return initial_foe_y, initial_foe_x


# Allows the foe to appear in the game with a message to the player.
def foe_appearance(
        provided_turn_count,
        provided_foe_appear,
):
    if provided_turn_count < provided_foe_appear:
        return
    elif provided_turn_count == provided_foe_appear:
        print("\nYour mysterious foe returns to the crime scene!")
        print("Don't let them catch up to you!")
        input(">>>:")
        return
    else:
        return


# TODO: Add features to make the foe more intelligent.
# Determines the direction the foe takes each turn and ensures it is a valid /
# direction, the foe does not move directly after a player escape.
def foe_behave(
        provided_map,
        provided_foe_y,
        provided_foe_x,
        provided_mode,
        provided_last_move,
        caught_flag,
        provided_turn_count,
        provided_foe_status,
        provided_y,
        provided_x,
        provided_reappear_count,
):
    opposites = {
        'up': 'down',
        'left': 'right',
        'right': 'left',
        'down': 'up',
    }
    if provided_last_move == '':
        provided_last_move = 'up'
    choice_made = provided_last_move
    while True:
        foe_room = provided_map["composition"][provided_foe_y][provided_foe_x]
        provided_foe_status, provided_reappear_count \
            = foe_disappear(
                provided_turn_count,
                provided_foe_status,
                provided_reappear_count,
                provided_mode,
            )
        if provided_mode == 'developer':
            print(provided_foe_y)
            print(provided_foe_x)
            print(provided_foe_status)
        provided_foe_y, provided_foe_x, provided_foe_status = foe_reappear(
            provided_turn_count,
            provided_reappear_count,
            provided_map,
            provided_y,
            provided_x,
            provided_foe_y,
            provided_foe_x,
            provided_foe_status,
            provided_mode,
        )
        if provided_foe_status == "gone":
            print("There is no sign of the mysterious foe!")
            return provided_foe_y, provided_foe_x, provided_last_move, \
                provided_foe_status, provided_reappear_count
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

                # An attempt to mitigate the foe alternating too much between /
                # opposite directions which results in poor map coverage.
                opposite = opposites['{0}'.format(choice_made)]
                if opposite == provided_last_move:
                    go_opposite = random().__round__()
                    if go_opposite == 1:
                        continue
                    else:
                        pass

                print("The mysterious foe decides to go ", choice_made, "!",
                      sep="")
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
        provided_last_move = choice_made
        return provided_foe_y, provided_foe_x, provided_last_move, \
            provided_foe_status, provided_reappear_count


# Allows the foe to randomly disappear and surprise the player around the map.
def foe_disappear(
        provided_turn_count,
        provided_foe_status,
        provided_reappear_count,
        provided_mode,
):
    if provided_foe_status == 'present':
        disappear_chance = randint(1, 6)
        if disappear_chance == 6:
            print("The mysterious foe vanishes from sight and hearing!")
            provided_foe_status = 'gone'
            reappear_count = provided_turn_count + randint(1, 3)
            if provided_mode == 'developer':
                print(reappear_count)
        else:
            provided_foe_status = 'present'
            reappear_count = provided_reappear_count
        return provided_foe_status, reappear_count
    else:
        return provided_foe_status, provided_reappear_count


# Determines the new room assignment for when the foe reappears in the game.
def foe_reappear(
        provided_turn_count,
        provided_reappear_count,
        provided_map,
        provided_y,
        provided_x,
        provided_foe_y,
        provided_foe_x,
        provided_foe_status,
        provided_mode,
):
    if provided_mode == 'developer':
        print(provided_turn_count)
        print(provided_reappear_count)
    if provided_turn_count == provided_reappear_count:
        print("The mysterious foe reappears all of a sudden!")
        while True:
            new_foe_y = randint(0, len(provided_map['composition']) - 1)
            new_foe_x \
                = randint(0, len(provided_map['composition'][new_foe_y]) - 1)
            if provided_mode == 'developer':
                print(new_foe_y)
                print(new_foe_x)
            if new_foe_y == provided_y and new_foe_x == provided_x:
                continue
            elif provided_map['composition'][new_foe_y][new_foe_x] == null_room:
                continue
            else:
                break
        new_foe_status = 'present'
        return new_foe_y, new_foe_x, new_foe_status
    else:
        new_foe_y = provided_foe_y
        new_foe_x = provided_foe_x
        new_foe_status = provided_foe_status
        return new_foe_y, new_foe_x, new_foe_status


# Handles situations where the player and foe end up in the same place, the /
# player either dies or gets away from the foe.
def caught(
        provided_y,
        provided_x,
        provided_foe_y,
        provided_foe_x,
        provided_map,
        provided_d_map,
        provided_foe_status,
):
    if provided_foe_status == 'gone':
        new_room = provided_map["composition"][provided_y][provided_x]
        caught_flag = 0
        return new_room, provided_y, provided_x, caught_flag
    new_room = provided_map["composition"][provided_y][provided_x]
    caught_flag = 0
    if provided_y == provided_foe_y and provided_x == provided_foe_x:
        print("The mysterious foe catches up to you!")
        input(">>>:")
        print("They reach out their hands...")
        input(">>>:")
        caught_chance = random().__round__()
        if caught_chance == 1:
            print("But you manage to slip away!")
            new_room, provided_y, provided_x, provided_d_map \
                = forced_move(
                    provided_map,
                    provided_d_map,
                    provided_y,
                    provided_x,
                )
            caught_flag = 1
        else:
            print("You cannot get away!")
            print("The mysterious foe chokes the life out of you!\n")
            input(">>>:")
            art_printer(game_over_art)
            exit()
    return new_room, provided_y, provided_x, caught_flag


# Forcibly moves the player by one valid space if they manage to get away from /
# the foe, the foe does not move again that turn in this case.
def forced_move(
        provided_map,
        provided_d_map,
        provided_y,
        provided_x,
):
    danger_room = provided_map["composition"][provided_y][provided_x]
    new_room = danger_room
    available_directions = len(danger_room[5])
    random_float = random()
    panic_choice = int(random_float * available_directions)
    choice_made = danger_room[5][panic_choice]

    print("You run ", choice_made, "!", sep="")
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
        new_room = \
            provided_map["composition"][provided_y][provided_x]
        provided_d_map = map_discover(
            provided_map,
            provided_d_map,
            provided_y,
            provided_x,
        )
    return new_room, provided_y, provided_x, provided_d_map


# Provides an integer for the turn the game is on.
def turn_counter(
        provided_turn_count,
):
    provided_turn_count += 1
    return provided_turn_count


# Allows the map of the level to be discovered room by room upon visit.
def map_discover(
        provided_map,
        provided_d_map,
        provided_y,
        provided_x,
):
    altered_d_map = copy.deepcopy(provided_d_map)
    altered_discoverable = list(altered_d_map)
    altered_discoverable[provided_y] = list(altered_discoverable[provided_y])
    altered_discoverable[provided_y][provided_x] \
        = list(altered_discoverable[provided_y][provided_x])
    room_object \
        = copy.deepcopy(provided_map['composition'][provided_y][provided_x])
    altered_discoverable[provided_y][provided_x] = room_object
    altered_discoverable[provided_y] = tuple(altered_discoverable[provided_y])
    altered_d_map = tuple(altered_discoverable)
    return altered_d_map


# TODO: Add the rest of the clues_system to the game.
# - Assign clues to random rooms avoiding player start and null rooms.
# - Add a condition to check if a room is a clue room and change its status.
# - Add a function that adds clues to your list and removes from 'remaining'.
# - Add function to be able to display collected clues and inspect.
# - Add function to check if all clues are gathered and trigger end conditions.


# TODO: Fit this with the rest of the program to create a win condition.
# Initialize the clues to be used in the game from 'game_maps_test.py'.
def initialize_clues():
    game_clues = clues_list
    game_remaining_clues = clues_to_collect_list
    return game_clues, game_remaining_clues


def art_printer(provided_art):
    print(provided_art)
    input(">>>: ")


# Initializes data for use in the game, to unclutter the RTP.
def game_initialize():
    i_mode = developer_mode()
    i_current_map = choose_game(
        map_list,
    )
    i_current_room, i_current_y, i_current_x, i_foe_appear, i_d_map \
        = initialize_map(
            i_current_map,
        )
    i_foe_y, i_foe_x = initialize_foe_position(
        i_current_map,
    )
    art_printer(game_art)
    how_to_play()
    i_turn_count = 0
    i_initial_last_move = ''
    i_foe_status = "present"
    map_printer(
        i_current_map['id'],
        i_current_map['danger'],
        i_current_y,
        i_current_x,
        i_foe_y,
        i_foe_x,
        i_turn_count,
        i_foe_appear,
        i_d_map,
        i_foe_status,
    )
    i_reappear_count = 999999999999999
    return i_mode, i_current_map, i_current_room, i_current_y, i_current_x, \
        i_foe_appear, i_d_map, i_foe_y, i_foe_x, i_turn_count, \
        i_initial_last_move, i_foe_status, i_reappear_count


# RTP, this code calls the functions to set up the game and get it going.
mode, current_map, current_room, current_y, current_x, foe_appear, \
        d_map, foe_y, foe_x, turn_count, initial_last_move, foe_status, \
        initial_reappear_count \
        = game_initialize()
main_loop(
    current_room,
    current_y,
    current_x,
    mode,
    map_list,
    foe_y,
    foe_x,
    turn_count,
    foe_appear,
    d_map,
    initial_last_move,
    foe_status,
    initial_reappear_count,
)
