import random
# input level of prompts
# if x<0 should prompt again

#random integer between 1 an 100

while True:
    try:
        level =int(input("Level: "))
        if level > 0:
            break
    except:
        pass

number = random.randint(1, level)

while True:
    try:
        guess = int(input("Guess: "))
        if guess>0:
            if guess > number:
                print("Too large!")
            elif guess < number:
                print("Too small!")
            else:
                print("Just right!")
                break
    except:
        pass










