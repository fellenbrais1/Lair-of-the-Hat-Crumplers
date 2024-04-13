# This is a bit of an experiment, basically it imports character data from \
# 'data_test.py' and uses it to generate an order that characters and enemies \
# can take in a battle. I have added a very basic system of changing the \
# health of the actors as well, though this doesn't do anything yet.
# There is probably some redundancy in the data lists and dictionaries that \
# could be cleaned up later.

import operator
from random import randint
from data_test import character_base_data, party_data, battlers, \
    battlers_data as bd

battle = True

while battle:

    for item in battlers:
        # In a real game, this type of assignment would be done everytime the \
        # character's speed changes in some way.
        item['init_mod'] = item['speed'] * 2 / 1.5
        item['init_mod'] = item['init_mod'].__round__()
        item['init'] = randint(0, 20) + item['init_mod']

    active_turn_list = []
    for battler in battlers:
        if 'KO' not in battler['statuses']:
            battler_initiative = battler['ref'], battler['name'], \
                                 battler['init'], battler['init_mod'], \
                                 battler['statuses']
            active_turn_list.append(battler_initiative)

    active_turn_list = sorted(active_turn_list, key=operator.itemgetter(2),
                              reverse=True)
    print(active_turn_list)

    del_char_list = []

    condition = True
    while condition:
        i = 0
        for i in range(len(battlers)):
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
                del_char_list.append(active_turn_list[i])
            else:
                print(bd[character_ref]['name'], 'now has',
                      bd[character_ref]['current_HP'], 'HP!')
            input(">>>")
            i += 1
            if i == len(battlers):
                end_of_turn = True
                while end_of_turn:
                    for item in active_turn_list:
                        if item in del_char_list:
                            active_turn_list.remove(item)
                        for battler in battlers:
                            if battler == character_ref:
                                battlers.remove(battler)
                            break
                    else:
                        print("\nNext turn!")
                        i = 0
                        condition = False
                        end_of_turn = False

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
