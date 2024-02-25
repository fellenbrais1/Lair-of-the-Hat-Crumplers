
import csv


def save_game():
    complete = False
    char_classes = ["Warrior", "Mage", "Archer", "Cleric"]
    file = open("savegame.csv", "w")
    writer = csv.writer(file)
    while not complete:
        answer = ""
        print("Would you like to save your game?")
        answer = input(str("Y or N: "))
        if answer.casefold().lstrip().rstrip() == "y":
            print("Saving game...")
            charname_1 = "Bobbo"
            charname_2 = "Julius"
            charname_3 = "Michael"
            charname_4 = "Jonas"
            charclass_1 = char_classes[1]
            charclass_2 = char_classes[0]
            charclass_3 = char_classes[3]
            charclass_4 = char_classes[2]
            chardata1 = {charname_1, charclass_1}
            chardata2 = [charname_2, charclass_2]
            chardata3 = [charname_3, charclass_3]
            chardata4 = [charname_4, charclass_4]
            writer.writerows(chardata1)
            writer.writerows(chardata2)
            writer.writerows(chardata3)
            writer.writerows(chardata4)
            # file.write(charname_1 + " " + charclass_1 + "\n")
            # file.write(charname_2 + " " + charclass_2 + "\n")
            # file.write(charname_3 + " " + charclass_3 + "\n")
            # file.write(charname_4 + " " + charclass_4 + "\n")
            file.close()
            print("Your game is now saved, try to load it in the other program!")
            complete = True
            exit()
        elif answer.casefold().lstrip().rstrip() == "n":
            print("Okay then, see you the next time you want to save!")
            complete = True
            exit()
        else:
            print("Please enter a choice between Y and N!")
            pass


save_game()
