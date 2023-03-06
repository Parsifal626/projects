import random


def main():
    # level = get_level()
    math_problem(2,8)


def get_level():
    while True:
        try:
            level =int(input("Level: "))
            if level in [1,2,3]:
                break
        except:
            pass
    return level


def generate_integer(level):
    if level == 1:
        x = random.randint(0,9)
        y = random.randint(0,9)
    elif level == 2:
        x = random.randint(10,99)
        y = random.randint(10,99)
    else:
        x = random.randint(100,999)
        y = random.randint(100,999)
    return x,y

def math_problem(x, y):
    tries = 1
    while tries <=3:
        try:
            answer = int(input(f"{x} + {y} = "))
            if answer == (x+y):
                return True
            else:
                tries +=1
                print("EEE")
        except:
                tries +=1
                print("EEE")



if __name__ == "__main__":
    main()