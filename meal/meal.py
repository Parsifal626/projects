def main():
    time = input("What time is it? ")
    check = convert(time)


    if 7<=check<=8:
        print('Breakfast time')
    elif 12<=check<=13:
        print('lunch time')
    elif 18<=check<=19:
        print('dinner time')

def convert(time):
    hours, minutes = time.split(':')
    hours = int(hours)
    minutes = int(minutes) / 60
    convert = hours + minutes
    return convert


if __name__ == "__main__":
    main()