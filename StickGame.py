print('''{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}
{}██╗    ██╗███████╗██╗      ██████╗ ██████╗ ███╗   ███╗███████╗    ████████╗ ██████╗ {}
{}██║    ██║██╔════╝██║     ██╔════╝██╔═══██╗████╗ ████║██╔════╝    ╚══██╔══╝██╔═══██╗{}
{}██║ █╗ ██║█████╗  ██║     ██║     ██║   ██║██╔████╔██║█████╗         ██║   ██║   ██║{}
{}██║███╗██║██╔══╝  ██║     ██║     ██║   ██║██║╚██╔╝██║██╔══╝         ██║   ██║   ██║{}
{}╚███╔███╔╝███████╗███████╗╚██████╗╚██████╔╝██║ ╚═╝ ██║███████╗       ██║   ╚██████╔╝{}
{} ╚══╝╚══╝ ╚══════╝╚══════╝ ╚═════╝ ╚═════╝ ╚═╝     ╚═╝╚══════╝       ╚═╝    ╚═════╝ {}
{}████████╗██╗  ██╗███████╗                                                           {}
{}╚══██╔══╝██║  ██║██╔════╝                                                           {}
{}   ██║   ███████║█████╗                                                             {}
{}   ██║   ██╔══██║██╔══╝                                                             {}
{}   ██║   ██║  ██║███████╗                                                           {}
{}   ╚═╝   ╚═╝  ╚═╝╚══════╝                                                           {}
{}███████╗████████╗██╗ ██████╗██╗  ██╗ ██████╗  █████╗ ███╗   ███╗███████╗            {}
{}██╔════╝╚══██╔══╝██║██╔════╝██║ ██╔╝██╔════╝ ██╔══██╗████╗ ████║██╔════╝            {}
{}███████╗   ██║   ██║██║     █████╔╝ ██║  ███╗███████║██╔████╔██║█████╗              {}
{}╚════██║   ██║   ██║██║     ██╔═██╗ ██║   ██║██╔══██║██║╚██╔╝██║██╔══╝              {}
{}███████║   ██║   ██║╚██████╗██║  ██╗╚██████╔╝██║  ██║██║ ╚═╝ ██║███████╗            {}
{}╚══════╝   ╚═╝   ╚═╝ ╚═════╝╚═╝  ╚═╝ ╚═════╝ ╚═╝  ╚═╝╚═╝     ╚═╝╚══════╝            {}
{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}''')
#let's introduce how to win this stick game
#winning strategy revolves around leaving your opponent with a multiple of 4 sticks after your turn.
#The player who takes the last stick wins.
import random
player = input('what is you name? ')
print(f'welcome to stick game {player} lets start the game: ')

def get_valid_stick_count(prompt, max_sticks):
    while True:
        try:
            count = int(input(prompt))
            if 1 <= count <= 3 and count <= max_sticks:
                return count
            print(f"Invalid input. Choose 1, 2, or 3 sticks and not more than {max_sticks}.")
        except ValueError:
            print("Please enter a valid number.")

def play_with_computer():
    while True:
        try:
            sticks = int(input("\nHow many sticks do you want to play with? "))
            if sticks > 0:
                break
            print("Please enter a positive number of sticks.")
        except ValueError:
            print("Please enter a valid number.")

    print(f"\nThere are {sticks} sticks: " + "|  " * sticks)
    choice = input("Do you want to go first? (yes/no): ").strip().lower()
    user_turn = choice.startswith("y")

    while sticks > 0:
        if user_turn:
            human = get_valid_stick_count("Your turn. How many sticks do you want to remove? ", sticks)
            sticks -= human
            if sticks == 0:
                print("You win!! 🎉")
                break
            print(f"There are {sticks} sticks left: " + "|  " * sticks)
        else:
            computer = sticks % 4 if sticks % 4 != 0 else random.randint(1, 3)
            print(f"\nComputer removes {computer} stick(s).")
            sticks -= computer
            if sticks == 0:
                print("Computer wins! You lost. 😢")
                break
            print(f"There are {sticks} sticks left: " + "|  " * sticks)
        user_turn = not user_turn

def play_with_friend():
    while True:
        try:
            sticks = int(input("\nHow many sticks do you want to play with? "))
            if sticks > 0:
                break
            print("Please enter a positive number of sticks.")
        except ValueError:
            print("Please enter a valid number.")

    print(f"\nThere are {sticks} sticks: " + "|  " * sticks)

    player = 1
    while sticks > 0:
        move = get_valid_stick_count(f"PLAYER {player}: How many sticks do you want to remove? ", sticks)
        sticks -= move
        if sticks == 0:
            print(f"\nPLAYER {player} wins! 🎉")
            break
        print(f"\nThere are {sticks} sticks left: " + "|  " * sticks)
        player = 2 if player == 1 else 1

def main():
    while True:
        choice = input("\nDo you want to play with the Computer or with a Friend? (C/F): ").strip().lower()
        if choice.startswith("c"):
            play_with_computer()
        elif choice.startswith("f"):
            play_with_friend()
        else:
            print("Invalid choice. Please enter 'C' or 'F'.")
            continue

        again = input("\nDo you want to play again? (yes/no): ").strip().lower()
        if not again.startswith("y"):
            print(f"Goodbye! {player} 👋")
            break
main()
