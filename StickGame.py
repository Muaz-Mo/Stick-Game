import random


def stick_game():
    while True:
        try:
            sticks = int(input("\nHow many stick you want to play with: "))
            break
        except ValueError:
            print("\nPlease enter a number.")
    while True:
        try:
            max_num_stick = int(input("\nHow many stick you want to be removed when playing the game: "))
            break
        except ValueError:
            print("\nPlease enter a number.")
    while sticks <= 0:
        print("\nPlease insert a valid number of stick which is greater than 0 or positive number.\n")
        stick_game()
    print(f"\nThere are {sticks} sticks:")
    x = sticks
    while x >= 10:
        x -= 10
        print("|  " * 10)
    print("|  " * x)
    print(f"\nChoose the number of sticks you want to remove.\nYou can only move 1 - {max_num_stick} sticks\n")
    choice = input("Do you want to go first, say yes or no: ")
    while sticks != 0:
        if choice.lower()[0] == "y":
            human = int(input("How many sticks you want to remove: "))
            while 0 >= human or human > max_num_stick or human > sticks:
                print(f"\nPlease insert valid integer which is in the range of 1 - {max_num_stick}. "
                      "\nAnd also you can't take sticks that are not available.")
                human = int(input("How many sticks you want to remove: "))
            sticks -= human
            if sticks == 0:
                print("\n" + "|" + "-" * 40 + "|")
                print("|{:^39}|".format("🎉 CONGRATULATION YOU WIN 🎉"))
                print(f"|" + "-" * 40 + "|")
                print("|{:^40}|".format("Well played!!"))
                print("|" + "_" * 40 + "|")
                break
            print(f"\nThere are {sticks} sticks:")
            x = sticks
            while x >= 10:
                x -= 10
                print("|  " * 10)
            print("|  " * x)
            if sticks % (max_num_stick + 1) == 0:
                computer = random.randrange(1, (max_num_stick + 1))
            else:
                computer = sticks % (max_num_stick + 1)
            print(f"\nOk the computer choose {computer}")
            sticks -= computer
            if sticks == 0:
                print("\n" + "|" + "-" * 40 + "|")
                print("|{:^40}|".format("UNFORTUNATELY YOU LOST"))
                print("|" + "-" * 40 + "|")
                print("|{:^40}|".format("NEVER GIVE UP!!"))
                print("|" + "_" * 40 + "|")
                break
            print(f"\nThere are {sticks} sticks:")
            x = sticks
            while x >= 10:
                x -= 10
                print("|  " * 10)
            print("|  " * x)
        else:
            if sticks % (max_num_stick + 1) == 0:
                computer = random.randrange(1, (max_num_stick + 1))
            else:
                computer = sticks % (max_num_stick + 1)
            print(f"\nOk the computer choose {computer}")
            sticks -= computer
            if sticks == 0:
                print("\n" + "|" + "-" * 40 + "|")
                print("|{:^40}|".format("UNFORTUNATELY YOU LOST"))
                print("|" + "-" * 40 + "|")
                print("|{:^40}|".format("NEVER GIVE UP!!"))
                print("|" + "_" * 40 + "|")
                break
            print(f"\nThere are {sticks} sticks:")
            x = sticks
            while x >= 10:
                x -= 10
                print("|  " * 10)
            print("|  " * x)
            human = int(input("How many sticks you want to remove: "))
            while 0 >= human or human > max_num_stick or human > sticks:
                print("\nPlease insert valid integer which is in the range of 1 - 3. "
                      "\nAnd also you can't take sticks that are not available.")
                human = int(input("How many sticks you want to remove: "))
            sticks -= human
            if sticks == 0:
                print("\n" + "|" + "-" * 40 + "|")
                print("|{:^39}|".format("🎉 CONGRATULATION YOU WIN 🎉"))
                print("|" + "-" * 40 + "|")
                print("|{:^40}|".format("Well played!!"))
                print("|" + "_" * 40 + "|")
                break
            print(f"\nThere are {sticks} sticks:")
            x = sticks
            while x >= 10:
                x -= 10
                print("|  " * 10)
            print("|  " * x)
    while True:
        play = input("\nDo you want to play again? \nsay yes or no: ")
        if play.lower()[0] == "y":
            decision = input("\nDo you want to play with computer or with your friend."
                             "\n\nIf you want to play with computer say C, else say F:")
            if decision.lower()[0] == "c":
                stick_game()
            else:
                stick_game_with_friend()
        elif play.lower()[0] == "n":
            print("\nGood Bye :)")
            break
        else:
            print("\nPlease say yes or no only.")
            continue


def stick_game_with_friend():
    while True:
        try:
            sticks = int(input("\nHow many stick you want to play with: "))
            break
        except ValueError:
            print("Please enter a number.")
    while True:
        try:
            max_num_stick = int(input("\nHow many stick you want to be removed when playing the game: "))
            break
        except ValueError:
            print("\nPlease enter a number.")
    while sticks <= 0:
        print("\nPlease insert a valid number of stick which is greater than 0 or positive number.")
        stick_game()
    print(f"\nThere are {sticks} sticks:")
    x = sticks
    while x >= 10:
        x -= 10
        print("|  " * 10)
    print("|  " * x)
    print(f"\nChoose the number of sticks you want to remove.\nYou can only move 1 - {max_num_stick} sticks")

    while sticks != 0:
        player1 = int(input("PLAYER1: How many sticks you want to remove: "))
        while 0 >= player1 or player1 > max_num_stick or player1 > sticks:
            print(f"\nPlease insert valid integer which is in the range of 1 - {max_num_stick}. "
                  "\nAnd also you can't take sticks that are not available.")
            player1 = int(input("PLAYER 1: How many sticks you want to remove: "))
        sticks -= player1
        if sticks == 0:
            print("\n" + "|" + "-" * 40 + "|")
            print("|{:^39}|".format("🎉 PLAYER 1 WINS 🎉"))
            print("|" + "-" * 40 + "|")
            print("|{:^40}|".format("Well played, Player 1!"))
            print("|" + "_" * 40 + "|")
            break
        x = sticks
        while x >= 10:
            x -= 10
            print("|  " * 10)
        print("|  " * x)
        player2 = int(input("PLAYER 2: How many sticks you want to remove: "))
        while 0 >= player2 or player2 > max_num_stick or player2 > sticks:
            print(f"\nPlease insert valid integer which is in the range of 1 - {max_num_stick}. "
                  "\nAnd also you can't take sticks that are not available.")
            player2 = int(input("\nPLAYER1: How many sticks you want to remove: "))
        sticks -= player2
        if sticks == 0:
            print("\n" + "|" + "-" * 40 + "|")
            print("|{:^39}|".format("🎉 PLAYER 2 WINS 🎉"))
            print("|" + "-" * 40 + "|")
            print("|{:^40}|".format("Well played, Player 2!"))
            print("|" + "_" * 40 + "|")
            break
        print(f"\nThere are {sticks} sticks:")
        x = sticks
        while x >= 10:
            x -= 10
            print("|  " * 10)
        print("|  " * x)
    while True:
        play = input("\nDo you want to play again? \nsay yes or no: ")
        if play.lower()[0] == "y":
            decision = input("\nDo you want to play with computer or with your friend."
                             "\n\nIf you want to play with computer say C, else say F:")
            if decision.lower()[0] == "c":
                stick_game()
            else:
                stick_game_with_friend()
        elif play.lower()[0] == "n":
            print("\nGood Bye :)")
            break
        else:
            print("\nPlease say yes or no only.")
            continue


co = input("\nDo you want to play with computer or with your friend."
           "\n\nIf you want to play with computer say C, else say F:")
if co.lower()[0] == "c":
    stick_game()
else:
    stick_game_with_friend()
