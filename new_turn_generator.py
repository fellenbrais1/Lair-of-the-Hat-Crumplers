# This test doesn't work for now, there is still more I need to learn here.

from data_test import initial_battlers
from random import randint
import operator


# Initiative order calculation.
def initiative_generator() -> list:
    """
    Generates a reverse sorted list of battlers based on initiative scores.

    Makes use of battlers data from 'data_test.py'.

    :return: Function sorts list of battlers and returns it as
    'active_turn_list'.
    """
    active_turn_list = []
    for battler in initial_battlers:
        battler_initiative = battler['ref'], battler['name'], \
                             battler['initiative']
        active_turn_list.append(battler_initiative)

    active_turn_list = sorted(active_turn_list, key=operator.itemgetter(2))
    print(active_turn_list)
    return active_turn_list


# Active character in turn generation.
def turn_order() -> None:
    """
    Determines the turn order of battlers based on their initiative scores.

    Puts battlers in order of their initiative for use in battle handling.
    """
    while True:
        i = 0
        for i in range(len(battlers)):
            active_character_dict = active_turn_list[i]
            print("The active character is: ", active_character_dict[1])
            input(">>>")
            i += 1
            if i == len(battlers):
                print("\nNext turn!")
                break
                i = 0


for item in initial_battlers:
    item['initiative'] = randint(0, 10)

if __name__ == " __main__":
    initiative_generator()
    turn_order()
