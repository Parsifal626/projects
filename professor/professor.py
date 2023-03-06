import random


def main():
    ...


def get_level():
    while True:
        try:
            level =int(input("Level: "))
            if level > 0:
                break
        except:
            pass


def generate_integer(level):
    ...


if __name__ == "__main__":
    main()