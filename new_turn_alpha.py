# This doesn't quite work yet, I think my design is poor. It would be a lot \
# cleaner to do everything with the base dictionary instead of making a load \
# of extra lists etc. to handle the data.

import operator
from random import randint
from data_test import character_base_data, party_data, initial_battlers, \
    battlers_data as bd

battle = True

while battle:

    for item in initial_battlers:
        # In a real game, this type of assignment would be done everytime the \
        # character's speed changes in some way.
        if 'slow' in item['statuses']:
            item['speed'] //= 4
            item['speed'].__round__()
        if 'KO' in item['statuses']:
            item['speed'] = item['init_mod'] = 0
        item['init_mod'] = item['speed'] * 2 / 1.5
        item['init_mod'] = item['init_mod'].__round__()
        item['init'] = randint(0, 20) + item['init_mod']

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

    condition = True
    while condition:
        i = 0
        for i in range(len(active_turn_list)):
            active_character_dict = active_turn_list[i]
            print("The active character is: ", active_character_dict[1])
            input(">>>")
            character_ref = (active_character_dict[0])
            print(bd[character_ref]['name'], ": ",
                  bd[character_ref]['current_HP'], sep="")
            if 'KO' in bd[character_ref]['statuses']:
                print(bd[character_ref]['name'], 'is knocked out!')
                bd[character_ref]['speed'] = -100
                continue
            else:
                damage = randint(25, 75) - bd[character_ref]['defence']
                if damage < 0:
                    damage = 0
                print('{0} took {1} damage!'.format(bd[character_ref]
                                                    ['name'], damage))
                bd[character_ref]['current_HP'] \
                    = bd[character_ref]['current_HP'] - damage
                if bd[character_ref]['current_HP'] <= 0:
                    print("{0} is KO'ed".format(bd[character_ref]['name']))
                    bd[character_ref]['statuses'].append('KO')
                    # active_character_dict[15].append('KO')
                else:
                    print(bd[character_ref]['name'], 'now has',
                          bd[character_ref]['current_HP'], 'HP!')
                input(">>>")
            i += 1
            if i == len(active_turn_list):
                print("\nNext turn!")
                i = 0
                condition = False

# This is another list that will be used to apply certain affects to actors.
status_effects = [
    'KO',
    'Sleep',
    'Poison',
    'Silence',
    'etc.',
]

# This is an example list of the kind of variables I would track in terms of \
# saving the player's progress etc.
game_data = {
    'save_file_name': 'Save File 1',
    'world_position': 0,
    'map_position': 0,
    'story_trigger': 0,
    'time_elapsed': 0,
    'reputation': 0,
    'character_base_stats': character_base_data,
    'party_stats': party_data,
}
