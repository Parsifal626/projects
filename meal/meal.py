def main():
    time = input("What time is it? ")
    hours, minutes = time.split(':')
    hours = float(hours)
    minutes = float(minutes)

    if 7<=hours<=8:
        print('Breakfast time')
    elif 12<=hours<=13:
        print('lunch time')
    elif 18<=hours<=19:
        print('lunch time')

def convert(time):
    time = [hours, minutes]
    minutes = minutes / 60
    if hours > 12:
        hours = [hours - 12]
    else:
        hours = [hours]






if __name__ == "__main__":
    main()