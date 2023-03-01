def main():
    while True:
        s = input("What fractions? ")
        try:
            x,y = s.split('/')
            x = float(x)
            y = float(y)
            fraction = x / y
            if fraction <=1:
                break
        except (ValueError, ZeroDivisionError):
            pass
    percent_fuel = fraction * 100
    if  percent_fuel <= 1:
            print('E')
    elif percent_fuel >= 99:
            print('F')
    else:
            print(f"{percent_fuel}%")

main()




