from data_test import battlers
from random import randint
import operator


def init():
    print_string = ""
    init_list = []
    for battler in battlers:
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
        battlers_battle = sorted(battlers, key=operator.itemgetter('init'),
                                 reverse=True)
        for battler in battlers_battle:
            print_string += str.ljust(battler['name'] + "'s initiative: ", 30) \
                            + str(battler['init']) + "\n"
            if 'KO' in battler['statuses']:
                print_string += "{0} is KOed!\n".format(battler['name'])
            elif 'slow' in battler['statuses']:
                print_string += "{0} is slowed!\n".format(battler['name'])
            elif 'haste' in battler['statuses']:
                print_string += "{0} is moving fast!\n".format(battler['name'])
        print(print_string)
        battle_turn(battlers_battle)


def battle_turn(battlers_battle):
    battlers = battlers_battle
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
        print_stats(battlers)


def print_stats(battlers):
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
    print_statuses(battlers)


def print_statuses(battlers):
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
    init()


init()
