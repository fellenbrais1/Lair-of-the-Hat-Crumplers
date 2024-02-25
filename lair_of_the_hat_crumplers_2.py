# Experimental text based adventure 'Lair of the Hat-Crumplers' Mk.2
# Modified with some big improvements over the last version

# Defining these assets, so they can be re-defined later in the code \
# class selection/ character names
char_1_class = char_2_class = char_3_class = 0

# Defining the char_class list
char_class = [
    "Crimper",
    "Measurer",
    "Fitter",
    "Hat Thrower",
    "Trichomancer",
]

# The character selection text to be displayed
char_selection = ("1.Crimper - A mighty crimper of edges and disarmer of "
                  "traps.\n"
                  "2.Measurer - A mighty combatant who measures up their "
                  "opponents.\n"
                  "3.Fitter - An agile fitter of hats and accessories.\n"
                  "4.Hat Thrower - A deadly arm with hats for all.\n"
                  "5.Trichomancer - A wielder of powerful scalp-itching "
                  "magic.\n")

# Introduction
print("\nWelcome, player, to the chilling tale of the \"Lair of the "
      "Hat-Crumplers\", prepare for danger\n"
      "amazement, wonder, and much much more!\n\n"
      "\t\t___________________________\n"
      "\t\t!                         /\n"
      "\t\t!          LAIR          /\n"
      "\t\t!           OF           \\\n"
      "\t\t \\        THE HAT         !\n"
      "\t\t /       CRUMPLERS        !\n"
      "\t\t!                         !\n"
      "\t-----------------------------------\n")

input("Please press enter to continue >>> ")
print("\nThe kingdom of Bromsgrove is in need of help! The evil Hat-Crumplers "
      "have taken\nover the dungeons under the city, and are using them to "
      "continue their reign of\nhat-crumpling terror. Not a hat in the "
      "land is safe! >>> ")
input()
print("A team of three of the kingdom's finest should be able to enter the "
      "dungeons and\nstop the Hat-Crumplers once and for all. Will you be the "
      "ones to end their reign of terror?\n")

# Choice0, starting the game
choice = ""
while choice != "Y" or "N":
    print("Are you ready to choose your characters?\n")
    choice = input("Y/N:\t\t")
    choice.casefold()
    if choice == "y":
        print("\nThen let us set start off on a terrifying adventure,\n"
              "but do not say you have not been warned...\n")
        break
    elif choice == "n":
        print("\nThen run away back to your knitting coward! Be gone!\n")
        print("GAME OVER!\n")
        exit()
    else:
        print("\nI'm sorry, please choose between 'Y' and 'N'.\n")
        continue

# Made this code more efficient by using a for range to initialize all the \
# characters and their information assigning it all to a list

char_1_name = char_2_name = char_3_name = ""

char_name_list = [
    char_1_name,
    char_2_name,
    char_3_name,
]

char_1_type = char_2_type = char_3_type = 0

char_type_list = [
    char_1_type,
    char_2_type,
    char_3_type,
]

char_1_class = char_2_class = char_3_class = char_class[0]

char_class_list = [
    char_1_class,
    char_2_class,
    char_3_class,
]

for i in range(0, 3):
    active_char_name = char_name_list[i]
    active_char_type = char_type_list[i]
    active_char_class = char_class_list[i]
    if i == 0:
        active_char_name = input("What is the name of your first character?:\t")
    elif i == 1:
        active_char_name = input("What is the name of your second character?:"
                                 "\t")
    else:
        active_char_name = input("What is the name of your third character?:\t")
    active_char_name = active_char_name.capitalize()
    char_name_list[i] = active_char_name
    print("\nWhat class would you like "
          + active_char_name
          + " to be?\n")
    print(char_selection)
    active_char_type = 0
    while active_char_type == 0:
        try:
            active_char_type = int(input("Please type a number:\t"))
        except ValueError:
            active_char_type = 0
        if active_char_type in range(1, 6):
            break
        else:
            print(
                "\nI'm sorry, that is not a valid number, please choose from "
                "'1-5'.\n"
                "Enter '6' to see the class list again.\n")
            if active_char_type == 6:
                print("\nWhat class would you like "
                      + active_char_name
                      + " to be?\n")
                print(char_selection)
            active_char_type = 0
            continue
    active_char_class = char_class[active_char_type - 1]
    char_class_list[i] = active_char_class
    print("So be it, "
          + char_name_list[i]
          + " will be a "
          + char_class_list[i]
          + ".\n")
    i += 1

# Defining the text displayed from char_list
char_list = char_name_list[0] \
            + ", the mighty and incomparable " \
            + char_class_list[0] \
            + ",\n" + char_name_list[1] \
            + ", the most formidable " \
            + char_class_list[1] \
            + " this world has ever seen, and,\n" \
            + char_name_list[2] \
            + ", the most deadly " \
            + char_class_list[2] \
            + " in the western court.\n".format(char_class)

# Party composition text and start
print("\nYour party is composed of:\n"
      + char_list)

# Choice1
choice = ""
while choice != "Y" or "N":
    print("Are you ready to begin your adventure? It's not too late to quit,\n"
          "or to go back and re-select your characters!\n")
    choice = input("Y/N:\t\t")
    choice.casefold()
    if choice == "y":
        print(
            "\nYour make your way down into the caverns of the hat-crumplers"
            "...\n"
            "Moisture drips from walls that seem to press in on your from "
            "every side.\n"
            "You can smell the fetid stench of the Hat-Crumplers who have been "
            "here recently\n"
            "on the air. The floor is littered with hats that have been "
            "crumpled, and you\n"
            "can almost feel the pain of their previous owners, cruelly forced "
            "to buy new hats.\n"
            "The terror of such a fate almost stops you in your tracks >>> ")
        break
    elif choice == "n":
        print("\nPlease begin again to re-select your characters!\n"
              "But if cowardice has overtaken your feeble heart then be "
              "gone!\n")
        print("PLEASE TRY AGAIN!")
        exit()
    else:
        print("\nI'm sorry, please choose between 'Y' and 'N'.\n")
        continue

# The hat-crumplers' dastardly hat-crumpling trap
input()
print("Suddenly, a hat-crumpling trap springs from the sides of the corridor!\n"
      "You have mere seconds before it ruins your hats! >>>")
input()

# Refined code for checking if one of characters is a 'Crimper' or not

if char_class[0] in char_class_list:
    print("Ah good! You have a "
          + char_class[0]
          + " in your party.\n"
          + "They effortlessly crimp down the edges of a dastardly "
            "hat-crumpling trap!\n")
    print("You are safe, for now...")
else:
    print("Good gracious! Without a Crimper present, the hat-crumpling trap "
          "thoroughly crumples your hats!\n"
          "\nGAME OVER!\n\nPlease try again!")
    exit()

print("To be continued!")
