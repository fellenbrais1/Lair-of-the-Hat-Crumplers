from data_test import battlers, battlers_data as bd
from random import randint
import operator
from odict import odict


def init():
    print_string = ""
    init_list = []
    for battler in battlers:
        active_name = battler
        r = active_name
        if 'slow' in r['statuses']:
            r['init_mod'] = r['speed'] - 20 + randint(0, 20)
        elif 'haste' in r['statuses']:
            r['init_mod'] = r['speed'] + 20 + randint(0, 20)
        elif 'KO' in r['statuses']:
            r['init_mod'] = 0
        else:
            r['init_mod'] = r['speed'] * 2 / 1.5 + randint(0, 20)
        r['init_mod'] = r['init_mod'].__round__()
        r['init'] = r['init_mod']
        data = r['name'], r['init'], r['statuses']
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
                print_string += "{0}, is moving fast!\n".format(item[0])
    for item in print_string:
        print(item, end="")
    else:
        active_turn()


def active_turn():
    active_turn_list = []
    for battler in battlers:
        battler_initiative = battler['ref'], battler['name'], \
                             battler['init'], battler['init_mod'], \
                             battler['statuses']
        active_turn_list.append(battler_initiative)

    active_turn_list = sorted(active_turn_list, key=operator.itemgetter(2),
                              reverse=True)
    print(active_turn_list)
    battle_turn(active_turn_list)


def battle_turn(active_turn_list):
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
                break
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
                print("\nNext turn!\n")
                condition = False
                print_stats(active_turn_list)


def print_stats(active_turn_list):
    od = odict(bd)
    stats = []
    for i in range(len(active_turn_list)):
        stats = []
        ref = active_turn_list[0]
        for k, v in bd[ref].items():
            stats += k, v
        # else:
            print((str.ljust(
                "{0} + 's statuses: ".format(bd['name']), 30),
                   stats))
    else:
        for line in stats:
            print(line)

    # a = []
    # b = []
    # c = []
    # d = []
    # for k, v in bd['c_1'].items():
    #     a += k, v
    # else:
    #     pass
    # for k, v in bd['c_2'].items():
    #     b += k, v
    # else:
    #     pass
    # for k, v in bd['c_3'].items():
    #     c += k, v
    # else:
    #     pass
    # for k, v in bd['e_1'].items():
    #     d += k, v
    # else:
    #     pass
    # print(str.ljust(bd['c_1']['name'] + "'s stats: ", 30) + str(a) + "\n",
    #       str.ljust(bd['c_2']['name'] + "'s stats: ", 30) + str(b) + "\n",
    #       str.ljust(bd['c_3']['name'] + "'s stats: ", 30) + str(c) + "\n",
    #       str.ljust(bd['e_1']['name'] + "'s stats: ", 30) + str(d) + "\n",
    #       sep="")

    print_statuses()


def print_statuses():
    od = odict(bd)
    statuses = ""
    for i in range(len(battlers) + 1):
        status = ""
        item_to_search = od[i]
        for status in item_to_search['statuses']:
            statuses += status
        else:
            print((str.ljust("{0} + 's statuses: "
                             .format(item_to_search[i]['name'], 30), status
                             + "\n")))
    else:
        for line in statuses:
            print(line)
    #     status =
    # for item in bd['c_1']['statuses']:
    #     a += [item]
    # else:
    #     pass
    # for item in bd['c_2']['statuses']:
    #     b += [item]
    # else:
    #     pass
    # for item in bd['c_3']['statuses']:
    #     c += [item]
    # else:
    #     pass
    # for item in bd['e_1']['statuses']:
    #     d += [item]
    # else:
    #     pass
    # print(str.ljust(bd['c_1']['name'] + "'s statuses: ", 30) + str(status) + "\n",
    #       str.ljust(bd['c_2']['name'] + "'s statuses: ", 30) + str(status) + "\n",
    #       str.ljust(bd['c_3']['name'] + "'s statuses: ", 30) + str(status) + "\n",
    #       str.ljust(bd['e_1']['name'] + "'s statuses: ", 30) + str(status) + "\n",
    #       sep="")


init()

# init()
#
# a = []
# b = []
# c = []
# d = []
# for item in bd['c_1']['statuses']:
#     a += [item]
# else:
#     pass
# for item in bd['c_2']['statuses']:
#     b += [item]
# else:
#     pass
# for item in bd['c_3']['statuses']:
#     c += [item]
# else:
#     pass
# for item in bd['e_1']['statuses']:
#     d += [item]
# else:
#     pass
# print(str.ljust(bd['c_1']['name'] + "'s statuses: ", 30) + str(a) + "\n",
#       str.ljust(bd['c_2']['name'] + "'s statuses: ", 30) + str(b) + "\n",
#       str.ljust(bd['c_3']['name'] + "'s statuses: ", 30) + str(c) + "\n",
#       str.ljust(bd['e_1']['name'] + "'s statuses: ", 30) + str(d) + "\n",
#       sep="")
