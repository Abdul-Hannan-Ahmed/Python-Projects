import random

name = input("Enter your name: ").upper()

points_num = int(input("Enter the number of points you want in the game: "))
weapons = ["rock", "paper", "scissor"]
computer_points = []
player_points = []


def main():
    def game():
        computer = random.choice(weapons)
        player = None

        while player not in weapons:
            player = input("Enter rock, paper, or scissor: ").lower()

        if player == computer:
            print(name + ": " + player)
            print("COMPUTER: " + computer)
            print("DRAW!")

        elif player == "rock":
            if computer == "paper":
                print(name + ": " + player)
                print("COMPUTER: " + computer)
                print("COMPUTER WINS!")
                computer_points.append(1)
            elif computer == "scissor":
                print(name + ": " + player)
                print("COMPUTER: " + computer)
                print(name + " WINS!")
                player_points.append(1)

        elif player == "paper":
            if computer == "scissor":
                print(name + ": " + player)
                print("COMPUTER: " + computer)
                print("COMPUTER WINS!")
                computer_points.append(1)
            elif computer == "rock":
                print(name + ": " + player)
                print("COMPUTER: " + computer)
                print(name + " WINS!")
                player_points.append(1)

        elif player == "scissor":
            if computer == "rock":
                print(name + ": " + player)
                print("COMPUTER: " + computer)
                print("COMPUTER WINS!")
                computer_points.append(1)
            elif computer == "paper":
                print(name + ": " + player)
                print("COMPUTER: " + computer)
                print(name + " WINS!")
                player_points.append(1)

    def check_points():
        print("---------------------------------------------------------")
        print(name + "'S POINTS: " + str(len(player_points)))
        print("COMPUTER'S POINTS: " + str(len(computer_points)))

    def display_results():
        print("---------------------------------------------------------")
        if len(player_points) > len(computer_points):
            print(name + " WINS THE GAME!")
        if len(computer_points) > len(computer_points):
            print(name + " WINS THE GAME!")
        if len(player_points) == len(computer_points):
            print("DRAW!")

    def replay():
        print("---------------------------------------------------------")
        play_again = input("Do you want to play again?(yes/no): ").lower()

        while True:
            if play_again != "yes":
                print("BYE! WE HOPE TO SEE YOU AGAIN!")
                break
            else:
                points_num = int(
                    input("Enter the number of points you want in the game: "))
                for k in range(points_num):
                    game()
                check_points()
                display_results()
                replay()

    for k in range(points_num):
        game()
    check_points()
    display_results()
    replay()

main()
