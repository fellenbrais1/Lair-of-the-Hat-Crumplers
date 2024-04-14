import operator
from data_test import initial_battlers
from module_test import init, print_statuses


def main_loop():
    """
    Main loop handles the sequence of function in the battle system.

    This does not quite work yet. DO NOT USE.
    :return: Function passes data on to 'init()' and returns 'None'.
    """
    for battler in initial_battlers:
        active_name = battler
        init(active_name)


def active_turn():
    """
    Determines which player will act next in the turn order.

    This order is a reverse sorted list of the battlers based on their
    initiative score.

    :return: Function sorts a list, prints it, and returns 'None'.
    """
    active_turn_list = []
    for battler in initial_battlers:
        if 'KO' in battler['statuses']:
            continue
        else:
            battler_initiative = battler['ref'], battler['name'], \
                                 battler['init'], battler['init_mod'], \
                                 battler['statuses']
            active_turn_list.append(battler_initiative)

    active_turn_list = sorted(active_turn_list, key=operator.itemgetter(2),
                              reverse=True)
    print(active_turn_list)


if __name__ == 'main':
    main_loop()
