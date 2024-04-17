# This is a system to make maps and display them for the player with \
# the ability to move around the map and track the player's position.

# Functions have been ordered in the loose order they are called by the program.
import copy
from random import random, randint
from game_maps_test import *


# Displays instructions to the player at game start.
def how_to_play(provided_art: str) -> None:
    """
    Prints a list of instructions for the player.

    The instructions contain the story of the game and controls.
    Also calls 'art_printer()' to print game title art.

    :param provided_art: The art that will be printed by 'art_printer()'
    """
    print("\nSTORY:")
    print("The city has been rocked by a series of high-profile killings over "
          "the last month.\nNo-one has caught the mysterious killer, but you, a"
          " famous detective just got your lucky break.\nThe famous Carivelli "
          "family have ended up as the killer's latest victims and you are "
          "first on the scene.\nThere is just one major problem, no-one has "
          "seen the killer leave!\n")
    print("Enter the Carivelli mansion, gather the 3 pieces of evidence you "
          "need to put the mysterious killer away, but don't get caught!\n")
    print("Can you survive the... ")
    input(">>>: ")
    art_printer(provided_art)
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
          "'1/2/3/4'    - Displays the chosen piece of evidence.\n"
          "'x/exit'     - Exits the evidence menu.\n"
          "'q/quit'     - Quits the game.")
    input(">>>:")
    print("\n")


# Allows the user to specify "developer" mode or not, which displays \
# diagnostic information in some functions.
def developer_mode() -> str:
    """
    Allows functions to print diagnostic data if 'develop mode' is enabled.

    Modes are 'player' (normal), and 'developer' (prints diagnostics).

    :return: 'set_mode' which influences behaviour of other functions.
    """
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
def choose_game(provided_map_list: list) -> dict:
    """
    Allows the user to choose which map to play on for the game.

    Based on the inputted choice, the required map will be called up and used
    for the game's code.

    :param provided_map_list: A list of maps to choose from for the game.
    :return: 'chosen_map' returned to be used by the game.
    """
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
def initialize_map(provided_current_map: dict) -> tuple:
    """
    Allows the player's starting room and yx co-ordinate to be generated.

    Data is mined from the 'provided_current_map' for use here.

    :param provided_current_map: The current game map.
    :return: 'initial_room', 'initial_y', initial_x', initial_foe_appear',
    'initial_d_map' forming the player's starting room and yx co-ordinates and
    the foe's starting room and turn to appear in game.
    """
    initial_y = provided_current_map["start_pos"][0]
    initial_x = provided_current_map["start_pos"][1]
    initial_room = provided_current_map["composition"][initial_y][initial_x]
    initial_foe_appear = provided_current_map["foe_appear"]
    initial_d_map = provided_current_map["discoverable"]
    return initial_room, initial_y, initial_x, initial_foe_appear, \
        initial_d_map


# Displays some examples of what rooms should look like in "developer" mode.
def example_maps(provided_mode: str) -> None:
    """
    Prints example maps while in 'developer mode'.

    Code does not do anything in 'player mode'.

    :param provided_mode: Mode provided by 'developer_mode()'.
    """
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
        provided_mode: str,
        provided_map_list: list,
        provided_foe_y: int,
        provided_foe_x: int,
        provided_turn_count: int,
        provided_foe_appear: int,
        provided_d_map: tuple,
        provided_foe_status: str
) -> None:
    """
    Prints all maps in the game files in developer mode.

    Prints all maps in the games files using the 'map_printer()'.
    This code does nothing in 'player' mode.

    :param provided_mode: The mode generated by 'developer_mode()'.
    :param provided_map_list: The list of game maps.
    :param provided_foe_y: Current y co-ordinate.
    :param provided_foe_x: Current x co-ordinate.
    :param provided_turn_count: Current turn count.
    :param provided_foe_appear: The turn where the foe will appear in the game.
    :param provided_d_map: The discoverable map for use in the game.
    :param provided_foe_status: Whether the foe is present or has disappeared.
    """
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
                provided_foe_status
            )
        print("\n")


# Allows the game to run until a win, lose, or exit condition has been met.
def main_loop(
        provided_room: tuple,
        provided_y: int,
        provided_x: int,
        provided_mode: str,
        provided_map_list: list,
        provided_foe_y: int,
        provided_foe_x: int,
        provided_turn_count: int,
        provided_foe_appear: int,
        provided_d_map: tuple,
        provided_last_move: str,
        provided_foe_status: str,
        provided_reappear_count: int,
        provided_evidence_list: list,
        provided_found_list: list
) -> None:
    """
    The main loop of the program that enables the game to progress.

    This function calls 'choose_direction()' next which will then eventually
    feed back to call this function again.
    In developer mode diagnostics are printed.
    Player and foe co-ordinates are passed here to be passed to
    'choose_direction()' later.

    :param provided_room: The current room.
    :param provided_y: The current y co-ordinate.
    :param provided_x: The current x co-ordinate.
    :param provided_mode: The mode generated by 'developer_mode()'.
    :param provided_map_list: The list of all available game maps.
    :param provided_foe_y: The current foe y co-ordinate.
    :param provided_foe_x: The current foe x co-ordinate.
    :param provided_turn_count: The current turn number of the game.
    :param provided_foe_appear: The turn the foe is set to appear for the map.
    :param provided_d_map: The current discoverable map for the game.
    :param provided_last_move: The last move the foe made.
    :param provided_foe_status: Whether the foe is present or has disappeared.
    :param provided_reappear_count: The turn when the foe will reappear.
    :param provided_evidence_list: The list of discoverable evidence in game.
    :param provided_found_list: The current collected evidence.
    :return: Function passes data, calls other functions and returns 'None'.
    """
    # The following functions only produce output in "developer" mode.
    example_maps(provided_mode)
    iterate_maps(
        provided_mode,
        provided_map_list,
        provided_foe_y,
        provided_foe_x,
        provided_turn_count,
        provided_foe_appear,
        provided_d_map,
        provided_foe_status
    )
    # Main list, some of these have "developer" mode diagnostics.
    # 'caught()' is run both after the player's turn and the foe's turn to \
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
                provided_found_list,
                provided_mode
            )
        provided_d_map = map_discover(
            current_map,
            provided_d_map,
            provided_y,
            provided_x
        )
        provided_evidence_list, provided_found_list = find_evidence(
            provided_y,
            provided_x,
            provided_evidence_list,
            provided_found_list
        )
        if provided_turn_count >= provided_foe_appear:
            provided_room, provided_y, provided_x, caught_flag = caught(
                provided_y,
                provided_x,
                provided_foe_y,
                provided_foe_x,
                current_map,
                provided_d_map,
                provided_foe_status
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
                    provided_reappear_count
                )
            provided_room, provided_y, provided_x, caught_flag = caught(
                provided_y,
                provided_x,
                provided_foe_y,
                provided_foe_x,
                current_map,
                provided_d_map,
                provided_foe_status
            )
        else:
            pass
        # Turn count updater.
        provided_d_map = map_discover(
            current_map,
            provided_d_map,
            provided_y,
            provided_x
        )
        provided_evidence_list, provided_found_list = find_evidence(
            provided_y,
            provided_x,
            provided_evidence_list,
            provided_found_list
        )
        provided_turn_count = turn_counter(provided_turn_count)
        provided_foe_status = foe_appearance(
            provided_turn_count,
            provided_foe_appear,
            provided_foe_status
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
        provided_room: tuple,
        provided_map: dict,
        provided_y: int,
        provided_x: int,
        provided_foe_y: int,
        provided_foe_x: int,
        provided_turn_count: int,
        provided_foe_appear: int,
        provided_d_map: tuple,
        provided_foe_status: str,
        provided_found_list: list,
        provided_mode: str
) -> tuple:
    """
    Allows a player or foe to choose a direction to move in and move in it.

    Function calculates both player movements and foe movements as well.

    :param provided_room: The current room.
    :param provided_map: The map being used in this iteration of the game.
    :param provided_y: The current y co-ordinate.
    :param provided_x: The current x co-ordinate.
    :param provided_foe_y: The current for y co-ordinate.
    :param provided_foe_x: The current foe x co-ordinate.
    :param provided_turn_count: The current turn count of the game.
    :param provided_foe_appear: The turn the foe is set to appear on this map.
    :param provided_d_map: The current game discoverable map.
    :param provided_foe_status: Whether the foe is present or had disappeared.
    :param provided_found_list: The list of evidence found by the player.
    :param provided_mode: Mode generated by 'developer_mode()'.
    :return: 'new_room', 'provided_y', 'provided_x' for use in later functions.
    """
    foe_close(
        provided_foe_y,
        provided_foe_x,
        provided_y,
        provided_x,
        provided_foe_status
    )
    directions = "up", "left", "right", "down", "outside",
    win_condition = evidence_count(provided_found_list)
    if win_condition == 1:
        print("\nYou have collected enough evidence!\n"
              "Get to the exit at the bottom of the map!")
    while True:
        display_available(provided_room)
        print("Which direction would you like to go in?\n"
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
                    if win_condition == 1:
                        you_win(provided_found_list)
                    else:
                        print("\nYou can't leave yet, you haven't gathered "
                              "enough evidence!")
                        new_room = \
                            provided_map["composition"][provided_y][provided_x]
                        continue
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
                provided_foe_status
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
            print("Are you sure you want to quit? 'y/yes', 'n/no'")
            quit_choice = input(">>>: ")
            quit_choice = quit_choice.casefold()
            if quit_choice == 'y':
                quit_choice = 'yes'
            if quit_choice == 'yes':
                print("Exiting game, see you next time!")
                exit()
            else:
                print("I didn't think you would quit so easily!")
                pass
        else:
            print("That is not a valid direction.")
    return new_room, provided_y, provided_x


# Displays available directions you can take from a room.
def display_available(provided_room: tuple) -> None:
    """
    Allows the display of all available directions to take from current room.

    Available directions are printed in a comma separated string for the user.

    :param provided_room: The current room.
    :return: Function prints messages and returns 'None'.
    """
    print("\nThe following directions are available:")
    # TODO: Fix the last comma appearing with the '.join' method
    for direction in provided_room[5]:
        print(direction, end=", ")
    print("\n")


# Streamlines 'display_position()' in previous builds and can also be used to \
# display the enemy position as well.
def position_check(
        provided_y: int,
        provided_x: int,
        working_y: int,
        working_x: int,
        provided_foe_y: int,
        provided_foe_x: int,
        provided_turn_count: int,
        provided_foe_appear: int,
        provided_foe_status: str
) -> str:
    """
    Function to check the position of the player and the foe character.

    This function will modify a room's 'middle_room_object', a graphic in the
    middle of a room object, that displays 'X' if the player is there, and '!'
    if the foe is there.

    :param provided_y: The current y co-ordinate.
    :param provided_x: The current y co-ordinate.
    :param working_y: The y co-ordinate of the map object.
    :param working_x: The x co-ordinate of the map object.
    :param provided_foe_y: The current foe y co-ordinate.
    :param provided_foe_x: The current foe x co-ordinate.
    :param provided_turn_count: The current turn number of the game.
    :param provided_foe_appear: The turn the foe is set to appear on the map.
    :param provided_foe_status: Whether the foe is present or has disappeared.
    :return: 'middle_room_object' for use by 'map_printer()'.
    """
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


# Prints a map by adding rows of room elements to a print string for each row \
# of rooms in the current map.
def map_printer(
        provided_map_id: str,
        provided_danger_level: str,
        provided_y: int,
        provided_x: int,
        provided_foe_y: int,
        provided_foe_x: int,
        provided_turn_count: int,
        provided_foe_appear: int,
        provided_d_map: tuple,
        provided_foe_status: str
) -> tuple:
    """
    Prints the map's room objects row by row.

    Constructs strings made of room objects in a row and then prints these
    strings to the output.

    :param provided_map_id: The current map's 'map _ID' value.
    :param provided_danger_level: The current map's 'danger_level' value.
    :param provided_y: The current y co-ordinate.
    :param provided_x: The current x co-ordinate.
    :param provided_foe_y: The current foe y co-ordinate.
    :param provided_foe_x: The current foe x co-ordinate.
    :param provided_turn_count: The current turn number of the game.
    :param provided_foe_appear: The turn the foe is set to appear on this map.
    :param provided_d_map: The current game discoverable map.
    :param provided_foe_status: Whether the foe is present or has disappeared.
    :return: 'provided_y', 'provided_x' for use in later functions.
    """
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
                            provided_foe_status
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
def initialize_foe_position(provided_map: dict) -> tuple:
    """
    Allows the placement of the foe at the start of the game.

    Data is mined from the game's data files to determine foe y x.

    :param provided_map: The current game map.
    :return: 'initial_foe_y', 'initial_foe_x' for use in later functions.
    """
    initial_foe_y = provided_map['foe_start'][0]
    initial_foe_x = provided_map['foe_start'][1]
    return initial_foe_y, initial_foe_x


# Allows the foe to appear in the game with a message to the player.
def foe_appearance(
        provided_turn_count: int,
        provided_foe_appear: int,
        provided_foe_status: str
) -> str:
    """
    Determines when the foe appears in the game.

    Determined by the 'foe_appear' value in the game map's dictionary.
    When the foe appear and current turn are equal the foe appears.

    :param provided_turn_count: The current turn number of the game.
    :param provided_foe_appear: The turn the foe appears for this map.
    :param provided_foe_status: Whether the foe is present or has disappeared.
    :return: 'new_foe_status' / 'provided_foe_status' for use in later
    functions.
    """
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


# TODO: Add features to make the foe more intelligent.
# Determines the direction the foe takes each turn and ensures it is a valid \
# direction, the foe does not move directly after a player escape.
def foe_behave(
        provided_map: dict,
        provided_foe_y: int,
        provided_foe_x: int,
        provided_mode: str,
        provided_last_move: str,
        provided_turn_count: int,
        provided_foe_status: str,
        provided_y: int,
        provided_x: int,
        provided_reappear_count: int
) -> tuple:
    """
    Determines the moves made and behaviour of the foe.

    Chooses the direction the foe will move in from valid directions. The last
    move the foe made is taken into account to avoid the foe alternating a lot.
    Developer mode prints diagnostic information.

    :param provided_map: The current game map.
    :param provided_foe_y: The current foe y co-ordinate.
    :param provided_foe_x: The current foe x co-ordinate.
    :param provided_mode: Mode generated by 'developed_mode()'.
    :param provided_last_move: The last move the foe made.
    :param provided_turn_count: The current turn number of the game.
    :param provided_foe_status: Whether the foe is present or has disappeared.
    :param provided_y: The current y co-ordinate.
    :param provided_x: The current x co-ordinate.
    :param provided_reappear_count:
    :return: 'provided_foe_y', 'provided_foe_x', 'provided_last_move',
    'provided_foe_status', 'provided_reappear_count' for use in later functions.
    """
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
                provided_mode
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
                provided_mode
            )
        if provided_foe_status == "gone":
            print("There is no sign of the mysterious foe!")
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

                random_float = random()
                foe_choice = int(random_float * available_directions)
                choice_made = foe_room[5][foe_choice]

                # An attempt to mitigate the foe alternating too much between \
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
            if reappear_flag == 1:
                if provided_mode == "developer":
                    print("\nDEVELOP DIAGNOSTICS 'foe_behave()'")
                    print("Foe reappear condition triggered.")
                    print("\n")
                pass
            else:
                print("The mysterious foe bides their time...")
        provided_last_move = choice_made
        return provided_foe_y, provided_foe_x, provided_last_move, \
            provided_foe_status, provided_reappear_count


# Allows the foe to randomly disappear and surprise the player around the map.
def foe_disappear(
        provided_turn_count: int,
        provided_foe_status: str,
        provided_reappear_count: int,
        provided_mode: str
) -> tuple:
    """
    Handles the disappearance of the foe.

    The foe will randomly disappear and reappear in the map at random turns.
    Developed mode will print diagnostic information.

    :param provided_turn_count: The current turn number of the game.
    :param provided_foe_status: Whether the foe is present or has disappeared.
    :param provided_reappear_count: When the foe is set to reappear.
    :param provided_mode: Mode generated by 'developer_mode()'.
    :return: 'provided_foe_status', 'provided_reappear_count'/ 'reappear_count'
    for use in later functions.
    """
    if provided_foe_status == 'present':
        disappear_chance = randint(1, 6)
        if disappear_chance == 6:
            print("\nYou lose track of your mysterious foe!\n")
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
        provided_turn_count: int,
        provided_reappear_count: int,
        provided_map: dict,
        provided_y: int,
        provided_x: int,
        provided_foe_y: int,
        provided_foe_x: int,
        provided_foe_status: str,
        provided_mode: str
) -> tuple:
    """
    Allows the reappearance of the foe after they have disappeared.

    The foe will reappear when gone when 'foe_reappear_count' matches current
    turn number. If the foe is present, this code just returns data unchanged.
    Code handles foe placement in invalid rooms and attempts reassignment.
    Developer mode prints diagnostic information.

    :param provided_turn_count: The current turn number of the game.
    :param provided_reappear_count: The turn the foe is set to reappear.
    :param provided_map: The current game map.
    :param provided_y: The current y co-ordinate.
    :param provided_x: The current x co-ordinate.
    :param provided_foe_y: The current foe y co-ordinate.
    :param provided_foe_x: The current foe x co-ordinate.
    :param provided_foe_status: Whether the foe is present or has disappeared.
    :param provided_mode: Mode generated by 'developer_mode()'.
    :return: 'new_foe_y', 'new_foe_x', 'new_foe_status', 'caught_flag',
    'reappear_flag' to be used in later functions.
    """
    if provided_mode == 'developer':
        print("\nDEVELOPER DIAGNOSTICS foe_reappear()'")
        print("'provided_turn_count' =", provided_turn_count)
        print("'provided_reappear_count' =", provided_reappear_count)
        print("\n")
    if provided_turn_count == provided_reappear_count:
        print("\nThe mysterious foe reappears all of a sudden!\n")
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


# Determines whether the foe is close to the player when present and prints a \
# warning for the player.
def foe_close(
        provided_foe_y: int,
        provided_foe_x: int,
        provided_y: int,
        provided_x: int,
        provided_foe_status: str
) -> None:
    """
    Alerts the player if the foe is close to the player character.

    The alert triggers if the foe is one square in any 8-direction around them.

    :param provided_foe_y: The current foe y co-ordinate.
    :param provided_foe_x: The current foe x co-ordinate.
    :param provided_y: The current y co-ordinate.
    :param provided_x: The current x co-ordinate.
    :param provided_foe_status: Whether the foe is present or has disappeared.
    """
    if provided_foe_status == 'present':
        y_difference = abs(provided_foe_y - provided_y)
        if y_difference <= 1:
            x_difference = abs(provided_foe_x - provided_x)
            if x_difference <= 1:
                print("\nThe mysterious foe is close!\nLook out!")


# Handles situations where the player and foe end up in the same place, the \
# player either dies or gets away from the foe.
def caught(
        provided_y: int,
        provided_x: int,
        provided_foe_y: int,
        provided_foe_x: int,
        provided_map: dict,
        provided_d_map: tuple,
        provided_foe_status: str
) -> tuple:
    """
    Determines handling if the player and foe occupy the same room.

    The 'caught_flag' goes to 1 if the player and foe shared a room, this will
    cause the foe not to make a move the next turn to allow player escape.
    If the player is caught there is a 50% chance of death and a 50% chance of
    the code moving to 'forced_move()' for escape.

    :param provided_y: The current y co-ordinate.
    :param provided_x: The current x co-ordinate.
    :param provided_foe_y: The current foe y co-ordinate.
    :param provided_foe_x: The current foe x co-ordinate.
    :param provided_map: The current game map.
    :param provided_d_map: The current game discoverable ,map.
    :param provided_foe_status: Whether the foe is present of has disappeared.
    :return: 'new_room', 'provided_y', 'provided_x', 'caught_flag' for use in
    later functions.
    """
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
                    provided_x
                )
            caught_flag = 1
        else:
            print("You cannot get away!")
            print("The mysterious foe chokes the life out of you!\n")
            input(">>>:")
            art_printer(game_over_art)
            exit()
    return new_room, provided_y, provided_x, caught_flag


# Forcibly moves the player by one valid space if they manage to get away from \
# the foe, the foe does not move again that turn in this case.
def forced_move(
        provided_map: dict,
        provided_d_map: tuple,
        provided_y: int,
        provided_x: int
) -> tuple:
    """
    Moves the player to a valid neighboring room in case of player and foe
    interaction where the player can escape.

    The code is written to avoid any impossible directional moves from the room.

    :param provided_map: The current game map.
    :param provided_d_map: The current game discoverable map.
    :param provided_y: The current y co-ordinate.
    :param provided_x: The current x co-ordinate.
    :return: 'new_room', 'provided_y', 'provided_x', 'provided_d_map'
     for use in later functions.
    """
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
            provided_x
        )
    return new_room, provided_y, provided_x, provided_d_map


# Provides an integer for the turn the game is on.
def turn_counter(provided_turn_count: int) -> int:
    """
    Counts the current turn number of the game.

    Adds to the turn count when called every turn.

    :param provided_turn_count: The current number of the game turn.
    :return: 'provided_turn_count' to be used in the next turn.
    """
    provided_turn_count += 1
    return provided_turn_count


# Allows the map of the level to be discovered room by room upon visit.
def map_discover(
        provided_map: dict,
        provided_d_map: tuple,
        provided_y: int,
        provided_x: int
) -> tuple:
    """
    Allows the discoverable (blank) map to updated with new rooms when found.

    The game maps 'discoverable' map will be updated with the normal map.

    :param provided_map: The current game map.
    :param provided_d_map: The discoverable blank version oif the game pma.
    :param provided_y: The current y co-ordinate.
    :param provided_x: The current x co-ordinate.
    :return: 'altered_d_map' returned for use by 'map-printer()'.
    """
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


# Assigns evidence to three non-starting or null rooms in the map and stores \
# the co-ordinates to the list of lists 'evidence_yx'.
def assign_evidence(
        provided_evidence_list: list,
        provided_map: dict,
        provided_mode: str
) -> list:
    """
    Assigns evidence items to valid rooms at game start.

    Invalid item placements result in another attempt to place the item until
    successful. Runs at the start of the game only.
    Developer mode prints diagnostic information.

    :param provided_evidence_list: List of evidence in the game.
    :param provided_map: Current game map.
    :param provided_mode: Mode generated by 'developer_mode()'.
    :return: 'provided_evidence_list' for use in the game.
    """
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
                if provided_map['composition'][working_y][working_x]\
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


# This function should show you the evidence when you enter the same room as \
# it, and delete that piece of evidence from the 'provided_evidence_list' so \
# that it cannot be 'found' again.
def find_evidence(
        provided_y: int,
        provided_x: int,
        provided_evidence_list: list,
        provided_found_list: list
) -> tuple:
    """
    Allows handling when player finds a piece of evidence in the game.

    Displays a picture of the collected evidence and then calls 'delete_by_yx()'
    to delete that piece of evidence from the game's evidence list.

    :param provided_y: Current y co-ordinate.
    :param provided_x: Current x co-ordinate.
    :param provided_evidence_list: List of evidence in the game.
    :param provided_found_list: list of player found evidence.
    :return: 'provided_evidence_list', 'provided_found_list' to be used in later
    turns of the game.
    """
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


# Called by 'find_evidence()' to delete the evidence found from the findable \
# list by filtering it out by its matching ['yx'] value.
def delete_by_yx(
        provided_evidence_list: list,
        provided_target_yx: tuple
) -> list:
    """
    Deletes a found piece of evidence from the game's evidence list.

    Uses an inline expression to delete from the list, so it cannot be
    discovered in the game again.

    :param provided_evidence_list: The list of evidence in the game.
    :param provided_target_yx: The current room co-ordinates of the evidence.
    :return: Function deletes from a list and returns 'None'.
    """
    return list(filter(lambda d: d.get('yx')
                != provided_target_yx, provided_evidence_list))


# Initialize the evidence to be used in the game from 'game_maps_test.py'.
def initialize_evidence() -> tuple:
    """
    Allows the game evidence to be initialized.

    Mines the evidence data from the game's data files.

    :return: 'game_evidence', 'initial_collected_evidence' for use in game.
    """
    game_evidence = evidence_list
    initial_collected_evidence = evidence_collected_list
    return game_evidence, initial_collected_evidence


# Allows inspection of player collected evidence items.
def evidence_inspect(
        provided_found_list: list,
        provided_mode: str
) -> None:
    """
    Allows the player to inspect their found evidence and pocket book.

    Opens a sub menu that allows looking at collected evidence art and info.
    Developer mode allows diagnostics to be printed.

    :param provided_found_list: list of evidence the player has found in game.
    :param provided_mode: Mode generated by 'developer_mode()'.
    """
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
def evidence_count(provided_found_list: list) -> int:
    """
    Counts the evidence found by the player, triggering win condition.

    After collecting 3 pieces of evidence the count will be at 4 and this will
    trigger 'win_condition' to be returned.

    :param provided_found_list: List of evidence found by the player.
    :return: Function returns 'win_condition' if checks are passed.
    """
    while True:
        if len(provided_found_list) == 4:
            win_condition = 1
            break
        else:
            win_condition = 0
            break
    return win_condition


# Prints art provided to it, art is kept in 'game_maps_test.py'.
def art_printer(provided_art: str) -> None:
    """
    Function to print ASCII art from the game's data files.

    Art is listed at the bottom of the game data files.

    :param provided_art: The art to be printed.
    """
    print(provided_art)


# Handles the output in the case of a game win.
def you_win(provided_found_list: list) -> None:
    """
    Handles a player win situation.

    Calls on 'art_printer()' to print victory art from game data.
    Prints the found evidence in a list for the player.

    :param provided_found_list: The list of found evidence in the game.
    :return: Function exits the program and returns 'None'.
    """
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
def game_initialize() -> tuple:
    """
    Sets up game data starting values for use in the game.

    All needed variables are set or defined with a default here to avoid
    problems with the rest of the code.

    :return: 'i_mode', 'i_current_map', 'i_current_room', 'i_current_y',
    'i_current_x', 'i_foe_appear', 'i_d_map', 'i_foe_y', 'i_foe_x',
    'i_turn_count', 'i_initial_last_move', 'i_foe_status', 'i_reappear_count',
     'i_evidence_list', 'i_game_found_evidence' for use in the game.
    """
    i_mode = developer_mode()
    i_current_map = choose_game(map_list)
    i_current_room, i_current_y, i_current_x, i_foe_appear, i_d_map \
        = initialize_map(i_current_map)
    i_foe_y, i_foe_x = initialize_foe_position(i_current_map)
    i_game_evidence, i_game_found_evidence = initialize_evidence()
    i_evidence_list = assign_evidence(
        i_game_evidence,
        i_current_map,
        i_mode
    )
    how_to_play(game_art)
    i_turn_count = 0
    i_initial_last_move = ''
    i_foe_status = "gone"
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
        i_foe_status
    )
    i_reappear_count = 999999999999999
    return i_mode, i_current_map, i_current_room, i_current_y, i_current_x, \
        i_foe_appear, i_d_map, i_foe_y, i_foe_x, i_turn_count, \
        i_initial_last_move, i_foe_status, i_reappear_count, i_evidence_list, \
        i_game_found_evidence


# RTP, this code calls the functions to set up the game and get it going.
mode, current_map, current_room, current_y, current_x, foe_appear, \
    d_map, foe_y, foe_x, turn_count, initial_last_move, foe_status, \
    initial_reappear_count, game_evidence_list, game_found_evidence \
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
    game_found_evidence
)
