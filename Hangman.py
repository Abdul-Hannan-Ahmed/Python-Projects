import random
import time

name = input("Enter your name: ")
print("Hello {}! Let's play hangman".format(name))

time.sleep(3)

words = ["january", "blindness", "diamond", "whale"]

word_to_guess = random.choice(words)
guesses = ""
chances = 10

while chances > 0:
    failed = 0

    for char in word_to_guess:
        if char in guesses:
            print(char, end="  ")
        else:
            print("_", end="  ")
            failed += 1

    if failed == 0:
        print("\nYou win!")
        break

    print("\n")

    if word_to_guess == "february":
        print("HINT: It is a name of a month.")
    if word_to_guess == "blindness":
        print("HINT: It is a name of a physical disability.")
    if word_to_guess == "diamond":
        print("HINT: It is a name of a mineral.")
    if word_to_guess == "whale":
        print("HINT: It is a name of a sea mammal.")

    user = input("\nEnter a letter: ").lower()

    guesses += user

    if user not in word_to_guess:
        chances -= 1
        print("Wrong! You have {} more chances left!".format(chances))

    if chances == 0:
        print("You loose! The word was: "+word_to_guess)
        break