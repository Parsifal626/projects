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
    ...


if __name__ == "__main__":
    main()