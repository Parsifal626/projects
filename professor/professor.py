import random


def main():
    ...


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
    else level == 3:
        x = random.randint(100,999)
        y = random.randint(100,999)
    return x,y



if __name__ == "__main__":
    main()