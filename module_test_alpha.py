# This is a very early build of the battle system, which loops around and is \
# comprised of functions calling one another, at the moment it provides a lot \
# of debugging data which would not be present in the finished article, I \
# tried to make it a lot more dependent on the master dictionary , but it \
# seems that having some data in a list is so much easier for indexing.

# A checking function could be called at the end of each turn if the number of \
# active player characters or enemies reaches zero, which would send an \
# argument back to another function somewhere else that handles the ending of \
# battles.

from data_test import initial_battlers, battlers_data as bd
from random import randint
import operator


def main_loop():
    """
    Main loop handles the sequence of function in the battle system.

    This does not quite work yet. DO NOT USE.
    :return: Function passes data on to 'init()' and returns 'None'.
    """
    while True:
        init()
        active_turn()
        battle_turn(active_turn_list="")
        print_stats(active_turn_list="")
        print_statuses(active_turn_list="")


# This function assigns initiative values to each participant in the battle.
def init():
    """
    Determines the initiative score for the active character.

    Initiative score is determined by the characters speed and statuses.

    :return: Function prints messages, calls 'active_turn()', and returns
    'None'.
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
            battler['init_mod'] = ((battler['speed'] * 2) / 1.5) \
                                  + randint(0, 20)
        battler['init_mod'] = battler['init_mod'].__round__()
        battler['init'] = battler['init_mod']
        data = battler['name'], battler['init'], battler['statuses']
        init_list.append(data)
    else:
        init_list = sorted(init_list, key=operator.itemgetter(1),
                           reverse=True)
        for item in init_list:
            print_string += str.ljust(item[0] + "'s initiative: ", 30) \
                            + str(item[1]) + "\n"
            if 'KO' in item[2]:
                print_string += "{0} is KOed!\n".format(item[0])
            elif 'slow' in item[2]:
                print_string += "{0} is slowed!\n".format(item[0])
            elif 'haste' in item[2]:
                print_string += "{0} is moving fast!\n".format(item[0])
        print(print_string)
        active_turn()


# This function sorts the 'active_turn_list' based on the initiative values \
# generated in the prior function.
def active_turn():
    """
    Determines which player will act next in the turn order.

    This order is a reverse sorted list of the battlers based on their
    initiative score.

    :return: Function prints a sorted list, calls 'battle_turn()', and returns
    'None'.
    """
    active_turn_list = []
    for battler in initial_battlers:
        battler_initiative = battler['ref'], battler['name'], \
                             battler['init'], battler['init_mod'], \
                             battler['statuses']
        active_turn_list.append(battler_initiative)

    active_turn_list = sorted(active_turn_list, key=operator.itemgetter(2),
                              reverse=True)
    battle_turn(active_turn_list)


# This function applies damage etc. in order and would probably be changed in \
# future to handle only damage and assigning the 'KO' status, another function \
# should be made to handle the choices player characters and enemies will make \
# and that can call this one when needed.
def battle_turn(active_turn_list):
    """
    Determines attack and damage calculation for the active character.

    In battle handling characters take damage and apply new HP totals.

    :param active_turn_list: The ordered list of active battlers.
    :return: Function prints messages, calls 'print_stats()', and returns
    'None'.
    """
    i = 0
    condition = True
    while condition:
        for i in range(len(active_turn_list)):
            active_character_dict = active_turn_list[i]
            print("\nThe active character is: ", active_character_dict[1])
            input(">>>")
            character_ref = (active_character_dict[0])
            cr = character_ref
            print(bd[cr]['name'], "'s HP: ", bd[cr]['current_HP'], sep="")
            if 'KO' in bd[cr]['statuses']:
                print(bd[cr]['name'], 'is knocked out!')
                continue
            else:
                damage = randint(25, 75) - bd[cr]['defence']
                if damage < 0:
                    print('{0} was unharmed!'.format(bd[cr]['name']))
                else:
                    bd[cr]['current_HP'] = bd[cr]['current_HP'] - damage
                    print('{0} took {1} damage!'.format(bd[cr]['name'], damage))
                if bd[cr]['current_HP'] <= 0:
                    print("{0} is KOed!".format(bd[cr]['name']))
                    bd[cr]['current_HP'] = 0
                    bd[cr]['statuses'].append(str('KO'))
                else:
                    print(bd[cr]['name'], 'now has', bd[cr]['current_HP'],
                          'HP!')
                input(">>>")
        i += 1
        if i == len(active_turn_list):
            print()
            condition = False
            print_stats(active_turn_list)


# This is a debugging function to check changes to stats are being applied, \
# but could be repurposed to produce character stats as displayed in a stats \
# screen or menu etc.
def print_stats(active_turn_list):
    """
    Prints the stats of the active character in battle handling.

    Prints all active character stats from their dictionary list.

    :param active_turn_list: A list of active characters for battle handling.
    :return: Function prints messages and returns 'None'.
    """
    stat_list = []
    for i in range(len(active_turn_list) + 1):
        stats = []
        try:
            ref = initial_battlers[i]['ref']
            for k, v in bd[ref].items():
                add = k, v
                stats.append(add)
            else:
                stat_list += (str.ljust(
                    "{0}'s stats: ".format(bd[ref]['name']), 30), stats,)
        except IndexError:
            continue
        except KeyError:
            continue
    else:
        for line in stat_list:
            print(line)
    print()
    print_statuses(active_turn_list)


# This is a debugging function to check changes to statuses are being applied, \
# but could be called later as a 'check party status' action in a menu or in \
# a battle etc.
def print_statuses(active_turn_list):
    """
    Allows the printing of battler status effects as a list.

    Looks at each battler's dictionary and prints statuses in a list.

    :param active_turn_list: List of active characters in battle handling.
    :return: Function prints messages and returns 'None'.
    """
    statuses_list = []
    for i in range(len(active_turn_list) + 1):
        statuses = []
        try:
            ref = initial_battlers[i]['ref']
            for v in bd[ref]['statuses']:
                statuses += [v]
            else:
                statuses_list += (str.ljust(
                    "{0}'s statuses: ".format(bd[ref]['name']), 30),
                                  statuses)
        except IndexError:
            continue
        except KeyError:
            continue
    else:
        for line in statuses_list:
            print(line)
    print("\nNext turn!\n")
    init()


# This function starts the process for now, but in future it would all be \
# called by the central game engine.
main_loop()
