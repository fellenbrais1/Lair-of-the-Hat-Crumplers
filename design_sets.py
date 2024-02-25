# Defining the default settings when initialising a new game
# This test doesn't work for now, there is still more I need to learn here

import operator
from random import randint
from char_select_test import active_character_select, testo

active_character_object = 0

character_base_data = {
    'character_number': 0,
    'name': '',
    'class': '',
    'level': 1,
    'max_HP': 100,
    'current_HP': 100,
    'max_MP': 50,
    'current_MP': 50,
    'attack': 10,
    'defence': 10,
    'speed': 10,
    'magic': 10,
    'initiative': 0,
}

characters_data = {
    'c_1': {
        'ref': 'c_1',
        'number': 1,
        'name': 'Johnny Johns',
        'class': '',
        'level': 1,
        'max_HP': 100,
        'current_HP': 100,
        'max_MP': 50,
        'current_MP': 50,
        'attack': 10,
        'defence': 10,
        'speed': 10,
        'magic': 10,
        'initiative': 7,
    },
    'c_2': {
        'ref': 'c_2',
        'number': 2,
        'name': 'Bibbs',
        'class': '',
        'level': 1,
        'max_HP': 100,
        'current_HP': 100,
        'max_MP': 50,
        'current_MP': 50,
        'attack': 10,
        'defence': 10,
        'speed': 10,
        'magic': 10,
        'initiative': 2,
    },
    'c_3': {
        'ref': 'c_3',
        'number': 3,
        'name': 'Chobby Bobba',
        'class': '',
        'level': 1,
        'max_HP': 100,
        'current_HP': 100,
        'max_MP': 50,
        'current_MP': 50,
        'attack': 10,
        'defence': 10,
        'speed': 10,
        'magic': 10,
        'initiative': 10,
    }
}

e_1 = {
    'ref': 'e_1',
    'number': 0,
    'name': 'Mad Hatter',
    'class': 'Hatter',
    'level': 1,
    'max_HP': 100,
    'current_HP': 100,
    'max_MP': 50,
    'current_MP': 50,
    'attack': 10,
    'defence': 10,
    'speed': 10,
    'magic': 10,
    'initiative': 3,
}

battlers = [
    characters_data['c_1'],
    characters_data['c_2'],
    characters_data['c_3'],
    e_1,
]

for item in battlers[0]:
    print(item)

active_turn_list = []
for item in battlers:
    item_initiative = item['ref'], item['name'], item['initiative']
    active_turn_list.append(item_initiative)
print(active_turn_list)

active_turn_list = sorted(active_turn_list, key=operator.itemgetter(2))

print(active_turn_list)

while True:
    try:
        active_character_object = next(active_character_select(battlers))
        print(active_character_object)
        break
    except StopIteration:
        break

active_character_object = int(active_character_object)
active_character_dict = active_turn_list[active_character_object]

print("The active character is: ", active_character_dict[1])

accessed_dict = active_character_dict
print(accessed_dict)

status_effects = [
    'KO',
    'Sleep',
    'Poison',
    'Silence',
    '',
]

game_data = {
    'save_file_name': 'Save File 1',
    'world_position': 0,
    'map_position': 0,
    'story_trigger': 0,
    'time_elapsed': 0,
    'reputation': 0,
    'character_data': character_base_data,
}

character_health = characters_data['c_1']['current_HP']

print(character_health)

damage = randint(1, 25) - characters_data['c_1']['defence']
if damage < 0:
    damage = 0


print('{0} took {1} damage!'.format(characters_data['c_1']['name'], damage))
characters_data['c_1']['current_HP'] \
    = characters_data['c_1']['current_HP'] - damage

print(characters_data['c_1']['name'], 'now has',
      characters_data['c_1']['current_HP'], 'HP!')

# for value in active_character_object:

print()

# while True:
#     i = 0
#     for i in range(len(battlers)):
#         active_character_dict = active_turn_list[i]
#         print("The active character is: ", active_character_dict[1])
#         i += 1
#         if i > len(battlers):
#             i = 0

# for i in range(len(battlers)):
#     active_character_dict = next(testo(active_turn_list, battlers))
#     print("The active character is: ", active_character_dict[1])

    # else:
    #     print("Finished!")

#     try:
#         active_character_object = next(active_character_select(battlers))
#         print(active_character_object)
#         active_character_object = int(active_character_object)
#         active_character_dict = active_turn_list[active_character_object]
#         print("The active character is: ", active_character_dict[1])
#         i += 1
#     except StopIteration:
#         break
# else:
#     print("Finished!")

# while True:
#     try:
#         active_character_object = next(active_character_select(battlers))
#         print(active_character_object)
#         break
#     except StopIteration:
#         break
#
# active_character_object = int(active_character_object)
# active_character_dict = active_turn_list[active_character_object]
#
# print("The active character is: ", active_character_dict[1])
#
#
# while True:
#     try:
#         active_character_object = next(active_character_select(battlers))
#         print(active_character_object)
#         break
#     except StopIteration:
#         break
#
# active_character_object = int(active_character_object)
# active_character_dict = active_turn_list[active_character_object]
#
# print("The active character is: ", active_character_dict[1])
#
#
# while True:
#     try:
#         active_character_object = next(active_character_select(battlers))
#         print(active_character_object)
#         break
#     except StopIteration:
#         break
#
# active_character_object = int(active_character_object)
# active_character_dict = active_turn_list[active_character_object]
#
# print("The active character is: ", active_character_dict[1])
#
#
# while True:
#     try:
#         active_character_object = next(active_character_select(battlers))
#         print(active_character_object)
#         break
#     except StopIteration:
#         break
#
# active_character_object = int(active_character_object)
# active_character_dict = active_turn_list[active_character_object]
#
# print("The active character is: ", active_character_dict[1])
