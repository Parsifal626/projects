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

#         if int(guess) > number:
#             print("Too large!")

#         elif int(guess) < number:
#             print("Too small!")
#             continue
#         else:
#             print("Just right!")
#             break











