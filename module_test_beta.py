from data_test import initial_battlers
from random import randint
import operator


def main_loop(provided_battlers: dict) -> None:
    """
    Main loop handles the sequence of function in the battle system.

    Calls other functions in order for turn operation and then goes back round.

    :param: provided_battlers: A list of active characters for battle handling.
    """
    while True:
        init(provided_battlers)
        provided_battlers = sorted(initial_battlers,
                                   key=operator.itemgetter('init'),
                                   reverse=True)
        print_init(initial_battlers)
        battle_turn(initial_battlers)
        print_stats(initial_battlers)
        print_statuses(initial_battlers)


def init(provided_battlers: dict) -> dict:
    """
    Determines the initiative scores for active characters in battle handling.

    Initiative score is determined by the characters speed and statuses.

    :param provided_battlers: A list of active characters for battle handling.
    :return: returns 'provided_battlers'.
    """
    init_list = []
    for battler in provided_battlers:
        if 'KO' in battler['statuses']:
            battler['init_mod'] = 0
        elif 'haste' in battler['statuses']:
            battler['init_mod'] = (battler['speed'] + 20) + randint(0, 20)
        elif 'slow' in battler['statuses']:
            battler['init_mod'] = (battler['speed'] - 20) + randint(0, 20)
        else:
            battler['init_mod'] = (((battler['speed'] * 2) / 1.5)
                                   + randint(0, 20)).__round__()
        battler['init'] = battler['init_mod']
        data = battler['name'], battler['init'], battler['statuses']
        init_list.append(data)
    else:
        return provided_battlers


def print_init(provided_battlers: dict) -> dict:
    """
    Prints the initiative scores for the active character.

    Initiative score is determined by the characters speed and statuses.

    :param provided_battlers: A list of active characters for battle handling.
    :return: Function prints messages, calls 'active_turn()', and returns
    'provided_battlers'.
    """
    print_string = ""
    for battler in provided_battlers:
        print_string += str.ljust(battler['name'] + "'s initiative: ", 30) \
                        + str(battler['init']) + "\n"
        if 'KO' in battler['statuses']:
            print_string += "{0} is KOed!\n".format(battler['name'])
        elif 'slow' in battler['statuses']:
            print_string += "{0} is slowed!\n".format(battler['name'])
        elif 'haste' in battler['statuses']:
            print_string += "{0} is moving fast!\n".format(battler['name'])
    print(print_string)
    return provided_battlers


def battle_turn(provided_battlers: dict) -> dict:
    """
    Determines attack and damage calculation for the active character.

    In battle handling characters take damage and apply new HP totals.

    :param provided_battlers: A list of active characters for battle handling.
    :return: Function prints messages, calls 'print_stats()', and returns
    'provided_battlers'.
    """
    for battler in provided_battlers:
        print("\nThe active character is: ", battler['name'])
        input(">>>")
        print(battler['name'], "'s HP: ", battler['current_HP'], sep="")
        if 'KO' in battler['statuses']:
            print(battler['name'], 'is knocked out!')
            continue
        else:
            damage = randint(25, 75) - battler['defence']
            if damage < 0:
                print('{0} was unharmed!'.format(battler['name']))
            else:
                battler['current_HP'] = battler['current_HP'] - damage
                print('{0} took {1} damage!'.format(battler['name'],
                                                    damage))
            if battler['current_HP'] <= 0:
                print("{0} is KOed!".format(battler['name']))
                battler['current_HP'] = 0
                battler['statuses'].append(str('KO'))
            else:
                print(battler['name'], 'now has', battler['current_HP'],
                      'HP!')
            input(">>>")
    else:
        print()
        return provided_battlers


def print_stats(provided_battlers: dict) -> dict:
    """
    Prints the stats of the active characters in battle handling.

    Prints all active character stats from their dictionary list.

    :param provided_battlers: A list of active characters for battle handling.
    :return: Function prints messages and returns 'provided_battlers'.
    """
    stat_list = []
    for battler in provided_battlers:
        stats = []
        for k, v in battler.items():
            add = k, v
            stats.append(add)
        else:
            stat_list += (str.ljust(
                "{0}'s stats: ".format(battler['name']), 30), stats,)
    else:
        for line in stat_list:
            print(line)
    print()
    return provided_battlers


def print_statuses(provided_battlers: dict) -> dict:
    """
    Allows the printing of battler status effects as a list.

    Looks at each battler's dictionary and prints statuses in a list.

    :param provided_battlers: A list of active characters for battle handling.
    :return: Function prints messages and returns 'provided_battlers'.
    """
    statuses_list = []
    for battler in provided_battlers:
        statuses = []
        for v in battler['statuses']:
            statuses += [v]
        else:
            statuses_list += (str.ljust(
                "{0}'s statuses: ".format(battler['name']), 30),
                              statuses)
    else:
        for line in statuses_list:
            print(line)
    print("\nNext turn!\n")
    return provided_battlers


battlers_sorted = []

main_loop(initial_battlers)
