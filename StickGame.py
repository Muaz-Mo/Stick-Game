import random


def stick_game():
    while True:
        try:
            sticks = int(input("\nHow many stick you want to play with: "))
            break
        except ValueError:
            print("\nPlease enter a number.")
    while sticks <= 0:
        print("\nPlease insert a valid number of stick which is greater than 0 or positive number.\n")
        stick_game()
    print(f"\nThere are {sticks}" + "|  " * sticks)
    print("\nChoose the number of sticks you want to remove.\nYou can only move 1,2 or 3 sticks\n")
    choice = input("Do you want to go first, say yes or no: ")
    while sticks != 0:
        if choice.lower()[0] == "y":
            human = int(input("Make your choice: "))
            while 0 >= human or human > 3 or human > sticks:
                print("\nPlease insert valid integer which is in the range of 1 - 3. "
                      "\nAnd also you can't take sticks that are not available.")
                human = int(input("How many sticks you want to remove: "))
            sticks -= human
            if sticks == 0:
                print("You win !!")
                break
            print(f"There are {sticks} " + "|  " * sticks + "sticks left")
            if sticks % 4 == 0:
                computer = random.randrange(1, 4)
            else:
                computer = sticks % 4
            print(f"\nOk the computer choose {computer}")
            sticks -= computer
            if sticks == 0:
                print("\nYou lost!!")
                break
            print(f"\nThere are {sticks} " + "|  " * sticks + "sticks left")
        else:
            if sticks % 4 == 0:
                computer = random.randrange(1, 4)
            else:
                computer = sticks % 4
            print(f"\nOk the computer choose {computer}")
            sticks -= computer
            if sticks == 0:
                print("\nYou lost!!")
                break
            print(f"\nThere are {sticks} " + "|  " * sticks + "sticks left")
            human = int(input("Make your choice: "))
            while 0 >= human or human > 3 or human > sticks:
                print("\nPlease insert valid integer which is in the range of 1 - 3. "
                      "\nAnd also you can't take sticks that are not available.")
                human = int(input("Make your choice: "))
            sticks -= human
            if sticks == 0:
                print("\nYou win!!\n")
                break
            print(f"\nThere are {sticks} " + "|  " * sticks + "sticks left")
    while True:
        play = input("Do you want to play again? \nsay yes or no: ")
        if play.lower()[0] == "y":
            stick_game()
            break
        elif play.lower()[0] == "n":
            print("Good Bye :)")
            break
        else:
            print("Please say yes or no only.")
            continue


def stick_game_with_friend():
    while True:
        try:
            sticks = int(input("\nHow many stick you want to play with: "))
            break
        except ValueError:
            print("Please enter a number.")
    while sticks <= 0:
        print("\nPlease insert a valid number of stick which is greater than 0 or positive number.")
        stick_game()
    print(f"\nThere are {sticks}" + "|  " * sticks)
    print("\nChoose the number of sticks you want to remove.\nYou can only move 1,2 or 3 sticks")

    while sticks != 0:
        player1 = int(input("PLAYER1: How many sticks you want to remove: "))
        while 0 >= player1 or player1 > 3 or player1 > sticks:
            print("\nPlease insert valid integer which is in the range of 1 - 3. "
                  "\nAnd also you can't take sticks that are not available.")
            player1 = int(input("PLAYER 1: How many sticks you want to remove: "))
        sticks -= player1
        if sticks == 0:
            print("\nPlayer 1 WON THE GAME!!")
            break
        print(f"\nThere are {sticks} " + "|  " * sticks + "sticks left")
        player2 = int(input("PLAYER 2: How many sticks you want to remove: "))
        while 0 >= player2 or player2 > 3 or player2 > sticks:
            print("\nPlease insert valid integer which is in the range of 1 - 3. "
                  "\nAnd also you can't take sticks that are not available.")
            player2 = int(input("\nPLAYER1: How many sticks you want to remove: "))
        sticks -= player2
        if sticks == 0:
            print("\nPlayer 2 WON THE GAME!!")
            break
        print(f"\nThere are {sticks} " + "|  " * sticks + "sticks left")


co = input("\nDo you want to play with computer or with your friend."
           "\n\nIf you want to play with computer say C, else say F:")
if co.lower()[0] == "c":
    stick_game()
    while True:
        play = input("\nDo you want to play again? \nsay yes or no: ")
        if play.lower()[0] == "y":
            stick_game()
            break
        elif play.lower()[0] == "n":
            print("\nGood Bye :)")
            break
        else:
            print("\nPlease say yes or no only.")
            continue
else:
    stick_game_with_friend()
    while True:
        play = input("\nDo you want to play again? \nsay yes or no: ")
        if play.lower()[0] == "y":
            stick_game_with_friend()
            break
        elif play.lower()[0] == "n":
            print("\nGood Bye :)")
            break
        else:
            print("\nPlease say yes or no only.")
            continue
