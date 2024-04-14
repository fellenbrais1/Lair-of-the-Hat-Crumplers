# A few tests to run all the functions in a loop without calling one another /
# so far none of these methods work, please comment out others to try each one /
# out.

# I have actually solved the issue now in 'module_test_beta.py'.

from data_test import initial_battlers
from random import randint
import operator


def main_loop():
    """
    Main loop handles the sequence of function in the battle system.

    Calls other functions in order for turn operation and then goes back round.

    :return: Function passes data on to other functions, and returns 'None'.
    """
    # METHOD ONE, DOESN'T WORK.
    # Just continuously runs init() and then prints "Next turn!" from /
    # print_statuses() for some reason without calling the other functions.

    while True:
        init()
        battle_turn(battlers_sorted="")
        print_stats(battlers="")
        print_statuses(battlers="")

    # METHOD TWO, DOESN'T WORK.
    # Also just continuously runs init() and then prints "Next turn!" from /
    # print_statuses() for some reason without calling the other functions.

    # COMMENTED OUT FOR NOW
    # while True:
    #     a = b = c = d = True
    #     while a:
    #         init()
    #         a = False
    #     while b:
    #         battle_turn(battlers_battle="")
    #         b = False
    #     while c:
    #         print_stats(battlers="")
    #         c = False
    #     while d:
    #         print_statuses(battlers="")
    #         d = False

    # METHOD THREE, DOESN'T WORK.
    # This was a recommended solution online, but I must not be using it /
    # correctly as it triggers my first actual stack overflow! Hooray! I /
    # got this not to overflow, but it just does the same as the other two /
    # methods so far. I have tried about twenty different suggested ways to /
    # fix this but all with no good results, it looks like the formatting of /
    # functions is wrong, and it can't be easily iterated through.

    # COMMENTED OUT FOR NOW
    # functions = (
    #     init(),
    #     battle_turn(battlers_battle=""),
    #     print_stats(battlers=""),
    #     print_statuses(battlers=""),
    # )
    # while True:
    #     for function in functions:
    #         function()


def init():
    """
    Determines active character initiative scores in battle handling.

    Determines the score based on 'init_mod' and statuses, and reverse sorts the
    list of battlers to determine them in order of high to low initiative.
    :return: Function reverse sorts 'battlers' and returns 'battlers_sorted'.
    """
    print_string = ""
    init_list = []
    for battler in initial_battlers:
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
        battlers_sorted = sorted(initial_battlers, key=operator
                                 .itemgetter('init'), reverse=True)
        for battler in battlers_sorted:
            print_string += str.ljust(battler['name'] + "'s initiative: ", 30) \
                            + str(battler['init']) + "\n"
            if 'KO' in battler['statuses']:
                print_string += "{0} is KOed!\n".format(battler['name'])
            elif 'slow' in battler['statuses']:
                print_string += "{0} is slowed!\n".format(battler['name'])
            elif 'haste' in battler['statuses']:
                print_string += "{0} is moving fast!\n".format(battler['name'])
        print(print_string)
        return battlers_sorted


def battle_turn(battlers_sorted):
    """
    Determines attack and damage calculation for the active character.

    In battle handling characters take damage and apply new HP totals.

    :param battlers_sorted: A list of active battlers in battle handling sorted
    by their initiative scores.
    :return: Function prints messages and returns 'battlers'.
    """
    battlers = battlers_sorted
    for battler in battlers:
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
        return battlers


def print_stats(battlers):
    """
    Prints the stats of the active characters in battle handling.

    Prints all active character stats from their dictionary list.

    :param battlers: A list of active characters for battle handling.
    :return: Function prints messages and returns 'battlers'.
    """
    stat_list = []
    for battler in battlers:
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
    return battlers


def print_statuses(battlers):
    """
    Allows the printing of battler status effects as a list.

    Looks at each battler's dictionary and prints statuses in a list.

    :param battlers: A list of active characters for battle handling.
    :return: Function prints messages and returns 'battlers'.
    """
    statuses_list = []
    for battler in battlers:
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
    return battlers


main_loop()
