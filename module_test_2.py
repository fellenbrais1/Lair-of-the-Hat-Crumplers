from data_test import battlers
from module_test import init, print_statuses


def main_loop():
    for battler in battlers:
        active_name = battler
        init(active_name)


def active_turn():
    active_turn_list = []
    for battler in battlers:
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
