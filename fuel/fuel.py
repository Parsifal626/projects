def main():
    percent_fuel= percent() * 100

    if percent_fuel == 0:
        print('E')
    elif percent_fuel == 100:
        print('F')
    else:
        print(f"{percent_fuel}%")

def percent():
    try:
        s = input("What fractions? ")
        x,y = s.split('/')
        x = float(x)
        y = float(y)
        fraction = x / y
        if fraction <= 1:
                return fraction
        else:
            continue

    except (ValueError, ZeroDivisionError):
        pass

main()




