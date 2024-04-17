# Coding challenge to create a loop and let users select actions each time \
# round.

from random import randint
from time import sleep


def battle_options() -> None:
    """
    Allows a user to choose the next action they will take in battle.

    Also determines the action the active enemy will take in battle. This
    function runs in a loop broken by an 'Escape' action.

    :return: Function prints messages and returns 'None'.
    """

    available_actions = [
        "Attack",
        "Defend",
        "Magic",
        "Items",
        "Draw",
        "Mug",
        "GF",
        "Card",
        "Escape",
    ]

    number = 1

    while True:
        print("What is your next action in battle:")
        for item in available_actions:
            print(number, ". ", item, sep="")
            number += 1
        print("Please type a number between 1 and 9, or 0 to quit.")
        number = 1
        enemy_choice = randint(1, 9)
        try:
            answer = int(input("Your choice: "))
            if answer == 0:
                print("\nExiting the program...")
                exit()
            elif answer == 9:
                print("\nYou Escape from the battle like a coward!")
                exit()
            else:
                action_chosen = available_actions[answer - 1]
                print("\nYou have chosen to do the {0} action!"
                      .format(action_chosen))
                sleep(1.5)
                print("\nThe enemy takes their turn...")
                sleep(1.5)
                print("The enemy does the {0} action!"
                      .format(available_actions[enemy_choice - 1]))
                if enemy_choice == 9:
                    print("\nThe enemy runs away in terror!")
                    print("You win the battle!")
                    exit()
                print("\nWhat will you do next?")
        except ValueError:
            print()


battle_options()
