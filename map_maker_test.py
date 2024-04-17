# This is a system to make maps and display them for the player with \
# the ability to move around the map and track the player's position.

# Functions have been ordered in the loose order they are called by the program.
from random import random
from game_maps_test import *


# Displays instructions to the player at game start.
def how_to_play() -> None:
    """
    Prints a list of instructions for the player.

    The instructions contain the story of the game and controls.
    """
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


# Allows the user to specify "developer" mode or not, which displays \
# diagnostic information in some functions.
def developer_mode() -> str:
    """
    Allows functions to print diagnostic data if 'develop mode; is enabled.

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

    :param provided_current_map:
    :return: 'initial_room', 'initial_y', initial_x' forming the player's
    starting room and yx co-ordinates.
    """
    initial_y = provided_current_map["start_pos"][0]
    initial_x = provided_current_map["start_pos"][1]
    initial_room = provided_current_map["composition"][initial_y][initial_x]
    initial_foe_appear = provided_current_map["foe_appear"]
    return initial_room, initial_y, initial_x, initial_foe_appear


# Displays some examples of what rooms should look like in "developer" mode.
def example_maps(provided_mode: str) -> None:
    """
    Prints example maps while in 'developer mode'.

    Code does not do anything in 'player mode'.

    :param provided_mode: Mode provided by 'developer_mode()'.
    :return: prints example maps for the user and returns 'None'.
    """
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
        provided_mode: str,
        provided_map_list: list,
        provided_foe_y: int,
        provided_foe_x: int,
        provided_turn_count: int,
        provided_foe_appear: int
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
    """
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
                provided_turn_count,
                provided_foe_appear
            )


# TODO: Add a win condition to allow an end to the game.
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
        provided_foe_appear: int
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
    """
    # The following functions only produce output in "developer" mode.
    example_maps(provided_mode)
    iterate_maps(
        provided_mode,
        provided_map_list,
        provided_foe_y,
        provided_foe_x,
        provided_turn_count,
        provided_foe_appear
    )
    # Main list, some of these have "developer" mode diagnostics.
    # 'caught()' is run both after the player's turn and the foe's turn to \
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
                provided_turn_count,
                provided_foe_appear
            )
        if provided_turn_count >= provided_foe_appear:
            provided_y, provided_x, caught_flag = caught(
                provided_y,
                provided_x,
                provided_foe_y,
                provided_foe_x,
                current_map
            )
            provided_foe_y, provided_foe_x = foe_behave(
                current_map,
                provided_foe_y,
                provided_foe_x,
                mode,
                caught_flag
            )
            provided_y, provided_x, caught_flag = caught(
                provided_y,
                provided_x,
                provided_foe_y,
                provided_foe_x,
                current_map
            )
        else:
            pass
        # Turn count updater.
        provided_turn_count = turn_counter(provided_turn_count)
        foe_appearance(
            provided_turn_count,
            provided_foe_appear
        )
        if provided_mode == "developer":
            print(current_room)
            print("Current_y is:", provided_y)
            print("Current_x is:", provided_x)
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
        provided_foe_appear: int
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
    :return: 'new_room', 'provided_y', 'provided_x' for use in the next part 
    of the game's main loop.
    """
    directions = "up", "left", "right", "down",
    while True:
        display_available(provided_room)
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
                provided_map['composition'],
                provided_map['id'],
                provided_map['danger'],
                provided_y,
                provided_x,
                provided_foe_y,
                provided_foe_x,
                provided_turn_count,
                provided_foe_appear
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
def display_available(provided_room: tuple) -> None:
    """
    Allows the display of all available directions to take from current room.
    
    Available directions are printed in a comma seperated string for the user.
    
    :param provided_room: The current room.
    """
    print("The following directions are available:")
    # TODO: Fix the last comma appearing with the '.join' method
    for direction in provided_room[5]:
        print(direction, end=", ")


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
        provided_foe_appear: int
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
    :return: 'middle_room_object' is returned for 'map_printer()' to use.
    """
    if provided_y == working_y and provided_x == working_x:
        middle_room_object = "X"
    elif provided_foe_y == working_y and provided_foe_x == working_x:
        if provided_turn_count >= provided_foe_appear:
            middle_room_object = "!"
        else:
            middle_room_object = " "
    else:
        middle_room_object = " "
    return middle_room_object


# Prints a map by adding rows of room elements to a print string for each row \
# of rooms in the current map.
def map_printer(
        provided_map: dict,
        provided_map_id: str,
        provided_danger_level: str,
        provided_y: int,
        provided_x: int,
        provided_foe_y: int,
        provided_foe_x: int,
        provided_turn_count: int,
        provided_foe_appear: int
) -> tuple:
    """
    Prints the map's room objects row by row.

    Constructs strings made of room objects in a row and then prints these
    strings to the output.
    
    :param provided_map: The current game map.
    :param provided_map_id: The current map's map ID value.
    :param provided_danger_level: The current map's danger_level value.
    :param provided_y: The current y co-ordinate.
    :param provided_x: The current x co-ordinate.
    :param provided_foe_y: The current foe y co-ordinate.
    :param provided_foe_x: The current foe x co-ordinate.
    :param provided_turn_count: The current turn number of the game.
    :param provided_foe_appear: The turn the foe is set to appear for the map.
    :return: 'current_y', 'current_x' for use in positional functions later.
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
                            provided_turn_count,
                            provided_foe_appear
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
    return current_y, current_x


# TODO: Make and implement the 'foe_system'


# Provides co-ordinates for where the foe start the game on each map.
def initialize_foe_position(provided_map: dict) -> tuple:
    """
    Determines where the foe will start on the game map.

    Data is mined from the game map's data dictionary.

    :param provided_map: The current game map.
    :return: 'initial_foe_y', 'initial_foe_x' used to place the foe in the map.
    """
    initial_foe_y = provided_map['foe_start'][0]
    initial_foe_x = provided_map['foe_start'][1]
    return initial_foe_y, initial_foe_x


# Allows the foe to appear in the game with a message to the player.
def foe_appearance(
        provided_turn_count: int,
        provided_foe_appear: int
) -> None:
    """
    Determines when the foe appears in the game.

    Determined by the 'foe_appear' value in the game map's dictionary.
    When the foe appear and current turn are equal the foe appears.

    :param provided_turn_count: The current turn number of the game.
    :param provided_foe_appear: The turn the foe appears for this map.
    """
    if provided_turn_count < provided_foe_appear:
        return
    elif provided_turn_count == provided_foe_appear:
        print("\nYour mysterious foe returns to the crime scene!")
        print("Don't let them catch up to you!")
        input(">>>:")
        return
    else:
        return


# Determines the direction the foe takes each turn and ensures it is a valid \
# direction, the foe does not move directly after a player escape.
def foe_behave(
        provided_map: dict,
        provided_foe_y: int,
        provided_foe_x: int,
        provided_mode: str,
        caught_flag: int
) -> tuple:
    """
    Program to determine the foe's behaviour and moves.

    If the player was bumped into by the foe last turn, the foe will not make
    a move this turn to allow player escape, determined by the 'caught_flag'.

    :param provided_map: The current map.
    :param provided_foe_y: The current foe y co-ordinate.
    :param provided_foe_x: The current foe x co-ordinate.
    :param provided_mode: Mode generated by 'developer_mode()'.
    :param caught_flag: A flag to indicate player/foe interaction last turn.
    :return: 'provided_foe_y', 'provided_foe_x' to be used in generating the
    foe's new position next turn.
    """
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


# Handles situations where the player and foe end up in the same place, the \
# player either dies or gets away from the foe.
def caught(
        provided_y: int,
        provided_x: int,
        provided_foe_y: int,
        provided_foe_x: int,
        provided_map: dict
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
    :return: 'provided_y', 'provided_x', 'caught_flag' for use in later
    functions.
    """
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
                = forced_move(
                    provided_map,
                    provided_y,
                    provided_x
                )
            caught_flag = 1
        else:
            print("You cannot get away!")
            print("The mysterious foe chokes the life out of you!\n")
            input(">>>:")
            print("GAME OVER!")
            exit()
    return provided_y, provided_x, caught_flag


# Forcibly moves the player by one valid space if they manage to get away from \
# the foe, the foe does not move again that turn in this case.
def forced_move(
        provided_map: dict,
        provided_y: int,
        provided_x: int
) -> tuple:
    """
    Moves the player to a valid neighboring room in case of player and foe
    interaction where the player can escape.

    The code is written to avoid any impossible directional moves from the room.

    :param provided_map: The current game map.
    :param provided_y: The current y co-ordinate.
    :param provided_x: The current x co-ordinate.
    :return: 'provided_y', 'provided_x' for use in later functions.
    """
    danger_room = provided_map["composition"][provided_y][provided_x]
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
    return provided_y, provided_x


def turn_counter(provided_turn_count: int) -> int:
    """
    Counts the current turn number of the game.

    Adds to the turn count when called every turn.

    :param provided_turn_count: The current number of the game turn.
    :return: 'provided_turn_count' to be used in the next turn.
    """
    provided_turn_count += 1
    return provided_turn_count


def map_discover(
        provided_map: dict,
        provided_d_map: dict,
        provided_y: int,
        provided_x: int
) -> dict:
    """
    Allows the discoverable (blank) map to updated with new rooms when found.

    The game maps 'discoverable' map will be updated with the normal map.

    :param provided_map: The current game map.
    :param provided_d_map: The discoverable blank version oif the game pma.
    :param provided_y: The current y co-ordinate.
    :param provided_x: The current x co-ordinate.
    :return: 'provided_d_map' returned for use by 'map-printer()'.
    """
    provided_d_map['composition'][provided_y][provided_x] \
        = provided_map['composition'][provided_y][provided_x]
    return provided_d_map


# RTP, this code calls the functions to set up the game and get it going.
mode = developer_mode()
current_map = choose_game(
    map_list
)
current_room, current_y, current_x, foe_appear = initialize_map(
    current_map
)
foe_y, foe_x = initialize_foe_position(
    current_map
)
how_to_play()
turn_count = 0
map_printer(
    current_map['composition'],
    current_map['id'],
    current_map['danger'],
    current_y,
    current_x,
    foe_y,
    foe_x,
    turn_count,
    foe_appear
)
main_loop(
    current_room,
    current_y,
    current_x,
    mode,
    map_list,
    foe_y,
    foe_x,
    turn_count,
    foe_appear
)
