# The core code for the game 'Murder Mansion'.

import copy
from random import random, randint
from murder_mansion_maps import *


# Displays story and instructions to the player at game start.
def how_to_play():
    print("\nSTORY:")
    print("The city has been rocked by a series of high-profile killings over "
          "the last month.\nNo-one has caught the mysterious killer, but you, "
          "a famous detective, have just got your lucky break.\nThe famous "
          "Carivelli family have ended up as the killer's latest victims and "
          "you are first on the scene.\nThere is just one problem, no-one has "
          "seen the killer leave!")
    input(">>>: ")
    print("\nEnter the Carivelli mansion, gather the 3 pieces of evidence you "
          "need to put the mysterious killer away, but don't get caught!\n"
          "You have chased this mysterious killer across the entire city, and "
          "now it looks like they will be your foe here as well.\n")
    print("Can you survive the...")
    input(">>>: ")
    art_printer(
        game_art,
    )
    input(">>>: ")
    print("CONTROLS:")
    print("The following controls are available:\n"
          "'u/up'       - Go up if possible.\n"
          "'l/left'     - Go left if possible.\n"
          "'r/right'    - Go right if possible.\n"
          "'d/down'     - Go down if possible.\n"
          "'m/map'      - Displays the map.\n"
          "'w/wait'     - Don't move for one turn.\n"
          "'e/evidence' - Displays your collected evidence.\n"
          "'l/list'     - Re-displays your evidence in the evidence menu.\n"
          "'1/2/3/4'    - Displays the chosen piece of evidence in the evidence"
          " menu.\n"
          "'x/exit'     - Exits the evidence menu.\n"
          "'q/quit'     - Quits the game.")
    input(">>>:")
    print("\nYou enter the mansion...")
    input(">>>: ")


# Allows the user to specify game mode, with "player" doing nothing, /
# "developer" printing diagnostics, and "mapper" which allows the player to /
# choose the game map. "developer" also activates choice of maps.
def developer_mode():
    while True:
        set_mode = "player"
        print("Would you like to run in developer mode? Y/ N")
        print("1. Start in normal mode.\n"
              "2. Start in developer mode.\n"
              "3. Start with map choices.\n")
        choice = input(">>>: ")
        if choice == "1":
            set_mode = "player"
            break
        elif choice == "2":
            set_mode = "developer"
            break
        elif choice == "3":
            set_mode = "mapper"
            break
        else:
            print("That is not a valid choice, please enter again.\n")
            continue
    return set_mode


# Allows the user to choose what map/ game type they want to play.
def choose_game(
        provided_map_list,
        provided_mode,
):
    if provided_mode == "developer" or provided_mode == "mapper":
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
                  "Or, 'l/list' to redisplay the choices or 'q/quit' to quit.")
            choice = input(">>>: ")
            try:
                if int(choice) in choices:
                    choice = int(choice)
                    chosen_map = map_list[choice - 1]
                    break
                else:
                    print("Please enter a choice from the list of available "
                          "maps by typing a number.")
            except ValueError:
                choice = choice.casefold()
                if choice == "l":
                    choice = "list"
                if choice == "q":
                    choice = "quit"
                if choice.casefold() == "list":
                    choices = []
                    for item in provided_map_list:
                        item_name = item['id']
                        item_name = item_name.title()
                        print(i, ". ", item_name, sep="")
                        choices.append(i)
                        i += 1
                if choice.casefold() == "quit":
                    print("Okay, see you some other time!")
                    exit()
        while True:
            # Peaceful mode has no enemies that appear.
            print("\nPlease choose a game mode:\n"
                  "1. Normal\n"
                  "2. Peaceful\n")
            choice = input(">>>: ")
            if choice == "1":
                break
            if choice == "2":
                altered_map = copy.deepcopy(chosen_map)
                new_foe_appear = 999999999999999
                altered_map['foe_appear'] = new_foe_appear
                return altered_map
            else:
                print("\nThat is not valid input, please type again.")
        return chosen_map
    else:
        chosen_map = map_list[4]
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
        print("\nDEVELOPER DIAGNOSTICS 'example_maps()'")
        print("Some examples of what some of the rooms look like:")
        print("'closed' room:")
        print("'closed' room does not display row 2 correctly as it is missing "
              "a blank 'middle_row' object in this version.")
        for item in closed[:5]:
            print(item)
        print("'open_all' room:")
        for item in open_all[:5]:
            print(item)
        print("'null_room' room:")
        for item in null_room[:5]:
            print(item)
        for item in mansion_entry[:5]:
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
        provided_foe_two_y,
        provided_foe_two_x,
        provided_foe_two_flag,
        provided_foe_two_status,
):
    if provided_mode == "developer":
        print("\nDEVELOPER DIAGNOSTICS 'iterate_maps()'")
        print("All maps will be printed:")
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
                provided_foe_two_y,
                provided_foe_two_x,
                provided_foe_two_flag,
                provided_foe_two_status,
            )
        print("\n")


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
        provided_evidence_list,
        provided_found_list,
        provided_foe_two_flag,
        provided_foe_two_y,
        provided_foe_two_x,
        provided_foe_two_status,
        provided_win_condition,
        provided_all_evidence_turn_count,
        provided_reappear_two_count,
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
        provided_foe_two_y,
        provided_foe_two_x,
        provided_foe_two_flag,
        provided_foe_two_status,
    )
    # Main list, some of these have "developer" mode diagnostics.
    # 'caught()' is run both after the player's turn and the foe's turn to /
    # cover all possible situations where they inhabit the same room.
    while True:
        provided_room, provided_y, provided_x, provided_win_condition, \
            provided_all_evidence_turn_count \
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
                provided_found_list,
                provided_mode,
                provided_foe_two_flag,
                provided_foe_two_y,
                provided_foe_two_x,
                provided_foe_two_status,
                provided_win_condition,
                provided_all_evidence_turn_count,
            )
        provided_d_map = map_discover(
            current_map,
            provided_d_map,
            provided_y,
            provided_x,
        )
        provided_evidence_list, provided_found_list = find_evidence(
            provided_y,
            provided_x,
            provided_evidence_list,
            provided_found_list,
        )
        if provided_mode == "developer":
            print("'win_condition' =", provided_win_condition)
            print("'provided_foe_two_flag' =", provided_foe_two_flag)
        if provided_turn_count >= provided_foe_appear:
            # To test if the second foe should appear yet.
            provided_foe_two_flag, provided_foe_two_status = foe_two_entry(
                provided_win_condition,
                provided_turn_count,
                provided_all_evidence_turn_count,
                provided_foe_two_flag,
                provided_foe_two_status,
                provided_mode,
            )
            provided_room, provided_y, provided_x, caught_flag \
                = caught(
                    provided_y,
                    provided_x,
                    provided_foe_y,
                    provided_foe_x,
                    current_map,
                    provided_d_map,
                    provided_foe_status,
                    provided_name="foe",
                )
            if provided_foe_two_flag == 1:
                # Setting up the entry point for foe_two.
                provided_foe_two_y, provided_foe_two_x, provided_foe_two_flag \
                    = initialize_foe_two_position(
                        current_map,
                        provided_mode,
                        provided_y,
                        provided_x,
                    )
            if provided_foe_two_flag == 2:
                # Checking to see if foe_two has 'caught' the player.
                provided_room, provided_y, provided_x, caught_flag \
                    = caught(
                        provided_y,
                        provided_x,
                        provided_foe_two_y,
                        provided_foe_two_x,
                        current_map,
                        provided_d_map,
                        provided_foe_two_status,
                        provided_name="accomplice",
                    )
            provided_foe_y, provided_foe_x, provided_last_move, \
                provided_foe_status, provided_reappear_count \
                = foe_behave(
                    current_map,
                    provided_foe_y,
                    provided_foe_x,
                    mode,
                    provided_last_move,
                    provided_turn_count,
                    provided_foe_status,
                    provided_y,
                    provided_x,
                    provided_reappear_count,
                    provided_name="foe",
                )
            provided_room, provided_y, provided_x, caught_flag \
                = caught(
                    provided_y,
                    provided_x,
                    provided_foe_y,
                    provided_foe_x,
                    current_map,
                    provided_d_map,
                    provided_foe_status,
                    provided_name="foe",
                )
            if provided_foe_two_flag == 2:
                # Allowing foe_two behaviour.
                provided_foe_two_y, provided_foe_two_x, provided_last_move, \
                    provided_foe_two_status, provided_reappear_two_count \
                    = foe_behave(
                        current_map,
                        provided_foe_two_y,
                        provided_foe_two_x,
                        mode,
                        provided_last_move,
                        provided_turn_count,
                        provided_foe_two_status,
                        provided_y,
                        provided_x,
                        provided_reappear_two_count,
                        provided_name="accomplice",
                    )
                # Checking to again see if foe_two has 'caught' the player.
                provided_room, provided_y, provided_x, caught_flag \
                    = caught(
                        provided_y,
                        provided_x,
                        provided_foe_two_y,
                        provided_foe_two_x,
                        current_map,
                        provided_d_map,
                        provided_foe_status,
                        provided_name="accomplice",
                    )
        else:
            pass
        provided_d_map = map_discover(
            current_map,
            provided_d_map,
            provided_y,
            provided_x,
        )
        provided_evidence_list, provided_found_list = find_evidence(
            provided_y,
            provided_x,
            provided_evidence_list,
            provided_found_list,
        )
        provided_turn_count = turn_counter(
            provided_turn_count,
        )
        provided_foe_status = foe_appearance(
            provided_turn_count,
            provided_foe_appear,
            provided_foe_status,
        )
        if provided_mode == "developer":
            print("\nDEVELOPER DIAGNOSTICS 'main_loop()'")
            print(current_room)
            print("'current_y' =", provided_y)
            print("'current_x' =:", provided_x)
            print("\n")
        else:
            continue


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
        provided_found_list,
        provided_mode,
        provided_foe_two_flag,
        provided_foe_two_y,
        provided_foe_two_x,
        provided_foe_two_status,
        provided_win_condition,
        provided_all_evidence_turn_count,
):
    foe_close(
        provided_foe_y,
        provided_foe_x,
        provided_y,
        provided_x,
        provided_foe_status,
        provided_name="foe",
    )
    if provided_foe_two_flag == 2:
        foe_close(
            provided_foe_two_y,
            provided_foe_two_x,
            provided_y,
            provided_x,
            provided_foe_two_status,
            provided_name="accomplice",
        )
    directions = "up", "left", "right", "down", "outside",
    provided_win_condition, provided_all_evidence_turn_count \
        = evidence_count(
            provided_found_list,
            provided_turn_count,
            provided_win_condition,
            provided_all_evidence_turn_count,
        )
    if provided_win_condition == 1:
        print("\nYou have collected enough evidence!\n"
              "Get to the exit at the bottom of the map!")
    while True:
        display_available(
            provided_room,
        )
        print("\nWhich direction would you like to go in?\n"
              "'u/up', 'l/left', 'r/right', 'd/down', 'o/outside', 'm/map', "
              "'e/evidence', 'q/quit''")
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
        if chosen_direction == "o":
            chosen_direction = "outside"
        if chosen_direction == "m":
            chosen_direction = "map"
        if chosen_direction == "w":
            chosen_direction = "wait"
        if chosen_direction == "q":
            chosen_direction = "quit"
        if chosen_direction == "e":
            chosen_direction = "evidence"
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
                elif chosen_direction == "outside":
                    if provided_win_condition == 1:
                        you_win(provided_found_list)
                    else:
                        print("\nYou can't leave yet, you haven't gathered "
                              "enough evidence!")
                        new_room = \
                            provided_map["composition"][provided_y][provided_x]
                        continue
            else:
                print("You decide to go ", chosen_direction, ".", sep="")
                print("\nA solid wall blocks your progress in that direction!")
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
                provided_foe_two_y,
                provided_foe_two_x,
                provided_foe_two_flag,
                provided_foe_two_status,
            )
        elif chosen_direction == "wait":
            new_room = provided_map["composition"][provided_y][provided_x]
            print("You decide to hide in this room and wait a while...")
            break
        elif chosen_direction == "evidence":
            evidence_inspect(
                provided_found_list,
                provided_mode
            )
        elif chosen_direction == "quit":
            print("\nAre you sure you want to quit? 'y/yes', 'n/no'")
            quit_choice = input(">>>: ")
            quit_choice = quit_choice.casefold()
            if quit_choice == 'y':
                quit_choice = 'yes'
            if quit_choice == 'yes':
                print("\nExiting game, see you next time!")
                exit()
            else:
                print("\nI didn't think you would quit so easily!")
                pass
        else:
            print("That is not a valid direction.")
    return new_room, provided_y, provided_x, provided_win_condition, \
        provided_all_evidence_turn_count


# Displays available directions you can take from a room.
def display_available(
        provided_room,
):
    print_string = ""
    print("\nThe following directions are available:")
    for direction in provided_room[5]:
        print_string += direction + ", "
    print_string = print_string[:-2]
    print(print_string)


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
        provided_foe_two_y,
        provided_foe_two_x,
        provided_foe_two_flag,
        provided_foe_two_status,
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
    elif provided_foe_two_y == working_y and provided_foe_two_x == working_x:
        if provided_foe_two_flag == 2:
            if provided_foe_two_status == 'gone':
                middle_room_object = " "
            else:
                middle_room_object = "?"
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
        provided_foe_two_y,
        provided_foe_two_x,
        provided_foe_two_flag,
        provided_foe_two_status,
):
    if provided_turn_count == 0:
        print("\nWelcome to the ", provided_map_id.title(), sep="")
        print("---------------------------------------------------------------"
              "--------------------")
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
                            provided_foe_two_y,
                            provided_foe_two_x,
                            provided_foe_two_flag,
                            provided_foe_two_status,
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


# Provides co-ordinates for where the foe start the game on each map.
def initialize_foe_position(
        provided_map,
):
    initial_foe_y = provided_map['foe_start'][0]
    initial_foe_x = provided_map['foe_start'][1]
    return initial_foe_y, initial_foe_x


# Sets a valid start position for the second foe when joining the game.
def initialize_foe_two_position(provided_map,
                                provided_mode,
                                provided_y,
                                provided_x,
                                ):
    while True:
        new_foe_two_y = randint(0, len(provided_map['composition']) - 1)
        new_foe_two_x \
            = randint(0, len(provided_map['composition'][new_foe_two_y]) - 1)
        if provided_mode == 'developer':
            print("\nDEVELOPER DIAGNOSTICS 'initialize_foe_two_position()'")
            print("'new_foe_two_y' =", new_foe_two_y)
            print("'new_foe_two_x' =", new_foe_two_x)
            print("\n")
        if new_foe_two_y == provided_y and new_foe_two_x == provided_x:
            continue
        elif provided_map['composition'][new_foe_two_y][new_foe_two_x] \
                == null_room:
            continue
        else:
            break
    new_foe_two_flag = 2
    return new_foe_two_y, new_foe_two_x, new_foe_two_flag


# Handles when the second foe will appear in the game.
def foe_two_entry(
        provided_win_condition,
        provided_turn_count,
        provided_all_evidence_turn_count,
        provided_foe_two_flag,
        provided_foe_two_status,
        provided_mode,
):
    if provided_mode == "developer":
        print("\nDEVELOPER DIAGNOSTIC 'foe_two_entry()'")
        print("'evidence_turn_count' =", provided_all_evidence_turn_count)
        print("'turn count' =", provided_turn_count)
    while True:
        if provided_win_condition == 1:
            if provided_turn_count == provided_all_evidence_turn_count:
                print("\nThe foe's accomplice enters the scene!")
                art_printer(killer_art)
                print("Now there are two of them after you!")
                input(">>>: ")
                new_foe_two_status = "present"
                new_foe_two_flag = 1
                return new_foe_two_flag, new_foe_two_status
            elif provided_turn_count > provided_all_evidence_turn_count:
                break
            else:
                break
        else:
            break
    return provided_foe_two_flag, provided_foe_two_status


# Allows the foe to appear in the game with a message to the player.
def foe_appearance(
        provided_turn_count,
        provided_foe_appear,
        provided_foe_status,
):
    if provided_turn_count < provided_foe_appear:
        provided_foe_status = "gone"
        return provided_foe_status
    elif provided_turn_count == provided_foe_appear:
        print("\nYour mysterious foe returns to the crime scene!")
        art_printer(killer_art)
        print("Don't let them catch up to you!")
        input(">>>:")
        new_foe_status = 'present'
        return new_foe_status
    else:
        return provided_foe_status


# TODO: Add features to make the foe more intelligent like a 'chase_mode'.
# Determines the direction the foe takes each turn and ensures it is a valid /
# direction, the foe does not move directly after a player escape.
def foe_behave(
        provided_map,
        provided_foe_y,
        provided_foe_x,
        provided_mode,
        provided_last_move,
        provided_turn_count,
        provided_foe_status,
        provided_y,
        provided_x,
        provided_reappear_count,
        provided_name,
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
                provided_name,
            )
        if provided_mode == 'developer':
            print("\nDEVELOPER DIAGNOSTICS 'foe_behave()'")
            print("'provided_foe_y' =", provided_foe_y)
            print("'provided_foe_x' =", provided_foe_x)
            print("'provided_foe_status' =", provided_foe_status)
            print("\n")
        provided_foe_y, provided_foe_x, provided_foe_status, caught_flag, \
            reappear_flag \
            = foe_reappear(
                provided_turn_count,
                provided_reappear_count,
                provided_map,
                provided_y,
                provided_x,
                provided_foe_y,
                provided_foe_x,
                provided_foe_status,
                provided_mode,
                provided_name,
            )
        if provided_foe_status == "gone":
            print("There is no sign of the mysterious ", provided_name, "!",
                  sep="")
            return provided_foe_y, provided_foe_x, provided_last_move, \
                provided_foe_status, provided_reappear_count
        if caught_flag != 1:
            try:
                available_directions = len(foe_room[5])
                if provided_mode == "developer":
                    print("\nDEVELOPER DIAGNOSTICS 'foe_behave()'")
                    random_float = random()
                    foe_choice = int(random_float * available_directions)
                    print("'foe_choice' example randoms:")
                    for i in range(11):
                        random_float = random()
                        foe_choice = int(random_float * available_directions)
                        print(foe_choice)
                    else:
                        print("'available_directions' = ", available_directions)
                        print("'len of foe_room[5]' = ", len(foe_room[5]))
                        print("'foe_room[5]' = ", foe_room[5])
                        print("'foe_choice' = ", foe_choice)
                        choice_made = foe_room[5][foe_choice]
                        print("'choice_made' = ", choice_made)
                        print("\n")
                while True:
                    random_float = random()
                    foe_choice = int(random_float * available_directions)
                    choice_made = foe_room[5][foe_choice]
                    if choice_made == "outside":
                        continue
                    else:
                        break
                # An attempt to mitigate the foe alternating too much between /
                # opposite directions which results in poor map coverage.
                if choice_made != "outside":
                    opposite = opposites['{0}'.format(choice_made)]
                    if opposite == provided_last_move:
                        go_opposite = random().__round__()
                        if go_opposite == 1:
                            continue
                        else:
                            pass
                else:
                    pass

                print("The mysterious ", provided_name, " decides to go ",
                      choice_made, "!", sep="")
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
                print("The mysterious ", provided_name, " bides their time...",
                      sep="")
        else:
            if reappear_flag == 1:
                if provided_mode == "developer":
                    print("\nDEVELOP DIAGNOSTICS 'foe_behave()'")
                    print("Foe reappear condition triggered.")
                    print("\n")
                pass
            else:
                print("The mysterious ", provided_name, " bides their time...",
                      sep="")
        provided_last_move = choice_made
        return provided_foe_y, provided_foe_x, provided_last_move, \
            provided_foe_status, provided_reappear_count


# Allows the foe to randomly disappear and surprise the player around the map.
def foe_disappear(
        provided_turn_count,
        provided_foe_status,
        provided_reappear_count,
        provided_mode,
        provided_name,
):
    if provided_foe_status == 'present':
        disappear_chance = randint(1, 6)
        if disappear_chance == 6:
            print("\nYou lose track of the mysterious ", provided_name, "!",
                  sep="")
            art_printer(foe_disappear_art)
            print(">>>: ")
            provided_foe_status = 'gone'
            reappear_count = provided_turn_count + randint(1, 3)
            if provided_mode == 'developer':
                print("\nDEVELOPER DIAGNOSTICS 'foe_disappear()'")
                print("'reappear_count' =", reappear_count)
                print("\n")
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
        provided_name,
):
    if provided_mode == 'developer':
        print("\nDEVELOPER DIAGNOSTICS foe_reappear()'")
        print("'provided_turn_count' =", provided_turn_count)
        print("'provided_reappear_count' =", provided_reappear_count)
        print("\n")
    if provided_turn_count == provided_reappear_count:
        print("\nThe mysterious ", provided_name, " reappears all of a sudden!"
                                                  "\n", sep="")
        art_printer(foe_return_art)
        print(">>>: ")
        while True:
            new_foe_y = randint(0, len(provided_map['composition']) - 1)
            new_foe_x \
                = randint(0, len(provided_map['composition'][new_foe_y]) - 1)
            if provided_mode == 'developer':
                print("\nDEVELOPER DIAGNOSTICS 'foe_reappear()'")
                print("'new_foe_y' =", new_foe_y)
                print("'new_foe_x' =", new_foe_x)
                print("\n")
            if new_foe_y == provided_y and new_foe_x == provided_x:
                continue
            elif provided_map['composition'][new_foe_y][new_foe_x] == null_room:
                continue
            else:
                break
        new_foe_status = 'present'
        caught_flag = 1
        reappear_flag = 1
        return new_foe_y, new_foe_x, new_foe_status, caught_flag, reappear_flag
    else:
        new_foe_y = provided_foe_y
        new_foe_x = provided_foe_x
        new_foe_status = provided_foe_status
        caught_flag = 0
        reappear_flag = 0
        return new_foe_y, new_foe_x, new_foe_status, caught_flag, reappear_flag


# Determines whether the foe is close to the player when present and prints a /
# warning for the player.
def foe_close(
        provided_foe_y,
        provided_foe_x,
        provided_y,
        provided_x,
        provided_foe_status,
        provided_name,
):
    if provided_foe_status == 'present':
        y_difference = abs(provided_foe_y - provided_y)
        if y_difference <= 1:
            x_difference = abs(provided_foe_x - provided_x)
            if x_difference <= 1:
                print("\nThe mysterious ", provided_name, " is close!"
                                                          "\nLook out!", sep="")


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
        provided_name,
):
    if provided_foe_status == 'gone':
        new_room = provided_map["composition"][provided_y][provided_x]
        caught_flag = 0
        return new_room, provided_y, provided_x, caught_flag
    new_room = provided_map["composition"][provided_y][provided_x]
    caught_flag = 0
    if provided_y == provided_foe_y and provided_x == provided_foe_x:
        print("The mysterious ", provided_name, " catches up to you!", sep="")
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
            print("The mysterious ", provided_name, " chokes the life out of "
                                                    "you!\n", sep="")
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


# Assigns evidence to three non-starting or null rooms in the map and stores /
# the co-ordinates to the list of lists 'evidence_yx'.
def assign_evidence(
        provided_evidence_list,
        provided_map,
        provided_mode,
):
    initial_evidence_yx = []
    if provided_mode == 'developer':
        print("\nDEVELOPER DIAGNOSTICS 'assign_evidence()'")
        for item in provided_evidence_list:
            print("'item' in 'provided_evidence_list' =", item['name'])
        for item in provided_evidence_list:
            print("'item[yx]' in 'provided_evidence_list' =", item['yx'])
    while True:
        for item in provided_evidence_list:
            while True:
                item['yx'] = []
                evidence_y = randint(0, len(provided_map['composition']) - 1)
                evidence_x \
                    = randint(0, len(provided_map['composition'][evidence_y])
                              - 1)
                item['yx'].append(evidence_y)
                item['yx'].append(evidence_x)
                working_y = item['yx'][0]
                working_x = item['yx'][1]
                if item['yx'] == provided_map['start_pos']:
                    continue
                if item['yx'] in initial_evidence_yx:
                    continue
                if provided_map['composition'][working_y][working_x] \
                        == null_room:
                    continue
                if provided_mode == 'developer':
                    print("\nDEVELOPER DIAGNOSTICS 'assign_evidence()'")
                    print("'item[name]'/ 'item[yx]' =", item['name'],
                          item['yx'])
                initial_evidence_yx.append(item['yx'])
                break
        else:
            break
    if provided_mode == 'developer':
        print("\nDEVELOPER DIAGNOSTICS 'assign_evidence()'")
        print("'initial_evidence_yx' =", initial_evidence_yx)
        for item in provided_evidence_list:
            print("'item[yx]' =", item['yx'])
    return provided_evidence_list


# This function should show you the evidence when you enter the same room as /
# it, and delete that piece of evidence from the 'provided_evidence_list' so /
# that it cannot be 'found' again.
def find_evidence(
        provided_y,
        provided_x,
        provided_evidence_list,
        provided_found_list,
):
    working_yx = [provided_y, provided_x]
    for item in provided_evidence_list:
        target_yx = item['yx']
        if working_yx == target_yx:
            print("\nYou find something in the room, a {0}!"
                  .format(item['name']))
            art_printer(item['picture'])
            input(">>>: ")
            provided_found_list.append(item)
            filtered_evidence_list \
                = delete_by_yx(provided_evidence_list.copy(), target_yx)
            return filtered_evidence_list, provided_found_list
        else:
            continue
    else:
        return provided_evidence_list, provided_found_list


# Called by 'find_evidence()' to delete the evidence found from the findable /
# list by filtering it out by its matching ['yx'] value.
def delete_by_yx(
        provided_evidence_list,
        provided_target_yx
):
    return list(filter(lambda d: d.get('yx')
                != provided_target_yx, provided_evidence_list))


# Initialize the evidence to be used in the game from 'game_maps_test.py'.
def initialize_evidence():
    game_evidence = evidence_list
    initial_collected_evidence = evidence_collected_list
    return game_evidence, initial_collected_evidence


# Allows inspection of player collected evidence items.
def evidence_inspect(provided_found_list, provided_mode):
    while True:
        choice_list = []
        print("\nWhich piece of collected evidence would you like to "
              "inspect?\n")
        for index, item in enumerate(provided_found_list):
            print("{0}. {1}".format(index + 1, item['name']))
            choice_list.append(int(index + 1))
        if provided_mode == "developer":
            print("\nDEVELOP DIAGNOSTICS 'evidence_inspect()'")
            print("'choice_list' =", choice_list)
            print(type("'choice_list type' =", choice_list))
        print("\n'1/2/3/4' inspect the item you want, 'l/list' to display "
              "again or 'x/exit' to exit this menu.\n")
        choice = input(">>>: ")
        try:
            if int(choice) in choice_list:
                choice = int(choice) - 1
                evidence_to_view = provided_found_list[choice]
                print("\n")
                print(evidence_to_view['name'])
                print(evidence_to_view['picture'])
                print(evidence_to_view['description'])
                input(">>>: ")
            else:
                print("That is not a valid choice, please enter again.")
                continue
        except ValueError:
            # Converting to full words instead of letters to allow processing.
            if choice.casefold() == 'l':
                choice = 'list'
            if choice.casefold() == "x":
                choice = 'exit'
            if choice.casefold() == 'list':
                continue
            if choice.casefold() == 'exit':
                break
            print("That is not a valid choice, please enter again.")
            continue


# Returns a 'win_condition' value of 1 if the 'found_list' is at len 4.
def evidence_count(
        provided_found_list,
        provided_turn_count,
        provided_win_condition,
        provided_all_evidence_turn_count,
):
    while True:
        if provided_win_condition != 1:
            if len(provided_found_list) == 4:
                new_win_condition = 1
                evidence_turn_count = turn_counter(provided_turn_count)
                evidence_turn_count -= 1
                break
            else:
                new_win_condition = 0
                evidence_turn_count = 999999999999999
                break
        else:
            new_win_condition = provided_win_condition
            evidence_turn_count = provided_all_evidence_turn_count
            break
    return new_win_condition, evidence_turn_count


# Prints art provided to it, art is kept in 'game_maps_test.py'.
def art_printer(provided_art):
    print(provided_art)


# Handles the output in the case of a game win.
def you_win(provided_found_list):
    print("\nYou escaped the mansion with your life and with the evidence!")
    print("The evidence you collected was:")
    for item in provided_found_list[1:]:
        print(item['name'])
    print("\nThat is more than enough to find out the killer's identity and "
          "put them away for good!")
    art_printer(victory_art)
    input(">>>: ")
    print("Thank you for playing!")
    exit()


# Initializes data for use in the game, to unclutter the RTP.
def game_initialize():
    i_mode = developer_mode()
    i_current_map = choose_game(
        map_list,
        i_mode,
    )
    i_current_room, i_current_y, i_current_x, i_foe_appear, i_d_map \
        = initialize_map(
            i_current_map,
        )
    i_foe_y, i_foe_x = initialize_foe_position(
        i_current_map,
    )
    i_game_evidence, i_game_found_evidence = initialize_evidence()
    i_evidence_list = assign_evidence(
        i_game_evidence,
        i_current_map,
        i_mode,
    )
    how_to_play()
    i_turn_count = 0
    i_initial_last_move = ''
    i_foe_status = "gone"
    i_foe_two_status = "gone"
    i_foe_two_flag = 0
    i_foe_two_y = 0
    i_foe_two_x = 0
    i_win_condition = 0
    i_all_evidence_turn_count = 999999999999999
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
        i_foe_two_y,
        i_foe_two_x,
        i_foe_two_flag,
        i_foe_two_status,
    )
    i_reappear_count = 999999999999999
    i_reappear_two_count = 999999999999999

    return i_mode, i_current_map, i_current_room, i_current_y, i_current_x, \
        i_foe_appear, i_d_map, i_foe_y, i_foe_x, i_turn_count, \
        i_initial_last_move, i_foe_status, i_reappear_count, i_evidence_list, \
        i_game_found_evidence, i_foe_two_flag, i_foe_two_y, i_foe_two_x, \
        i_foe_two_status, i_win_condition, i_all_evidence_turn_count, \
        i_reappear_two_count


# RTP, this code calls the functions to set up the game and get it going.
mode, current_map, current_room, current_y, current_x, foe_appear, \
    d_map, foe_y, foe_x, turn_count, initial_last_move, foe_status, \
    initial_reappear_count, game_evidence_list, game_found_evidence, \
    foe_two_flag, foe_two_y, foe_two_x, foe_two_status, win_condition,\
    all_evidence_turn_count, reappear_two_count\
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
    game_evidence_list,
    game_found_evidence,
    foe_two_flag,
    foe_two_y,
    foe_two_x,
    foe_two_status,
    win_condition,
    all_evidence_turn_count,
    reappear_two_count,
)
