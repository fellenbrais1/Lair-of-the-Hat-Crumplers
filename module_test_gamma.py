from data_test import initial_battlers
from random import randint
import operator


def main_loop():
    party = start(initial_battlers)
    while True:
        modified_party = initiative_calc(party)
        sorted_party = sort_party(modified_party)
        print_init(sorted_party)
        battle_turn(sorted_party)
        print_stats(sorted_party)
        print_statuses(sorted_party)
        party = next_turn(sorted_party)


def start(party_list):
    print("Welcome to the battle test system.")
    input('>>>')
    print("Would you like to import save file data?")
    choice = None
    while choice != '1' or '2':
        choice = input("1. Import save data.\n"
                       "2. Use initialised data\n"
                       ": ")
        if choice == "1":
            # Choice 1 does not work yet as I am not sure how to do it now
            print("This choice does not work yet, please check back later.")
            # party = data_import(save_data.csv)
            # return party
            choice = None
        elif choice == "2":
            print("Using initialized data.\n")
            party = party_list
            return party
        else:
            print("That is not a valid input.")
            continue


# Not sure how this works yet, but just an idea for now
def data_import(accessed_file):
    file = accessed_file
    try:
        file.open(file, 'r')
        party = file.read()
        print("Loaded party data successfully!")
        file.close()
        return party
    except ImportError:
        print("There is no save data present, importing initialised data.")
        party = initial_battlers
        return party


def initiative_calc(party_list):
    for member in party_list:
        if 'KO' in member['statuses']:
            member['init_mod'] = -100
        elif 'haste' in member['statuses']:
            member['init_mod'] = (member['speed'] + 20) + randint(0, 20)
        elif 'slow' in member['statuses']:
            member['init_mod'] = (member['speed'] - 20) + randint(0, 20)
        else:
            member['init_mod'] = (((member['speed'] * 2) / 1.5)
                                  + randint(0, 20)).__round__()
        member['init'] = member['init_mod']
    else:
        modified_party = party_list
        return modified_party


def sort_party(party_list):
    sorted_party = sorted(party_list, key=operator.itemgetter('init'),
                          reverse=True)
    return sorted_party


def print_init(party_list):
    print_string = ""
    for member in party_list:
        print_string += str.ljust(member['name'] + "'s initiative: ", 30) \
                        + str(member['init']) + "\n"
        if 'KO' in member['statuses']:
            print_string += "{0} is KOed!\n".format(member['name'])
        elif 'slow' in member['statuses']:
            print_string += "{0} is slowed!\n".format(member['name'])
        elif 'haste' in member['statuses']:
            print_string += "{0} is moving fast!\n".format(member['name'])
    print(print_string)
    sorted_party = party_list
    return sorted_party


def battle_turn(party_list):
    for member in party_list:
        print("\nThe active character is: ", member['name'])
        input(">>>")
        print(member['name'], "'s HP: ", member['current_HP'], sep="")
        if 'KO' in member['statuses']:
            print(member['name'], 'is knocked out!')
            continue
        else:
            damage = randint(25, 75) - member['defence']
            if damage < 0:
                print('{0} was unharmed!'.format(member['name']))
            else:
                member['current_HP'] = member['current_HP'] - damage
                print('{0} took {1} damage!'.format(member['name'],
                                                    damage))
            if member['current_HP'] <= 0:
                print("{0} is KOed!".format(member['name']))
                member['current_HP'] = 0
                member['statuses'].append(str('KO'))
            else:
                print(member['name'], 'now has', member['current_HP'],
                      'HP!')
            input(">>>")
    else:
        print()
        party = party_list
        return party


def print_stats(party_list):
    stat_list = []
    for member in party_list:
        stats = []
        for k, v in member.items():
            add = k, v
            stats.append(add)
        else:
            stat_list += (str.ljust(
                "{0}'s stats: ".format(member['name']), 30), stats,)
    else:
        for line in stat_list:
            print(line)
    print()
    sorted_party = party_list
    return sorted_party


def print_statuses(party_list):
    statuses_list = []
    for member in party_list:
        statuses = []
        for v in member['statuses']:
            statuses += [v]
        else:
            statuses_list += (str.ljust(
                "{0}'s statuses: ".format(member['name']), 30),
                              statuses)
    else:
        for line in statuses_list:
            print(line)
    sorted_party = party_list
    return sorted_party


def next_turn(party_list):
    print("\nNext turn!\n")
    party = party_list
    return party


main_loop()
