
import csv


def load_game():
    answer = ""
    complete = False
    char_1 = ""
    char_classes = ["Warrior", "Mage", "Archer", "Cleric"]
    file = open("savegame.csv", "r")
    while not complete:
        print("Would you like to load your game?")
        answer = input(str("Y or N: "))
        if answer.casefold().lstrip().rstrip() == "y":
            print("Loading game...")
            data = file.read()
            print(data)
            file.close()
            print("Your game is now loaded, try to use the data in another program!")
            complete = True
            exit()
        elif answer.casefold().lstrip().rstrip() == "n":
            print("Okay then, see you the next time you want to load!")
            complete = True
            exit()
        else:
            print("Please enter a choice between Y and N!")
            pass


load_game()
