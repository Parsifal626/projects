import random
# input level of prompts
# if x<0 should prompt again

#random integer between 1 an 100

while True:
    level = input("Level: ")

    if (int(level) < 0 or not level.isdecimal()):
        level = input("Level: ")

    guess = input("Guess: ")
    if not int(guess.isdecimal()) or int(guess) < 0:
        guess = input("Guess: ")


    number = random.randint(1, int(level))
    while True:
        if int(guess) > number:
            print("Too large!")
            continue
        elif int(guess) < number:
            print("Too small!")
            continue
        else:
            print("Just right!")
            break











