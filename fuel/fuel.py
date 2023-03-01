while True:
    s = input("What fractions? ")
    try:
        x,y = s.split('/')
        x = float(x)
        y = float(y)
        percent_fuel= percent() * 100
def main():


    if percent_fuel == 0:
        print('E')
    elif percent_fuel == 100:
        print('F')
    else:
        print(f"{percent_fuel}%")

def percent():
    while True:
        try:
            s = input("What fractions? ")

            fraction = x / y
            if fraction <= 1:
                break

                return False
            else:
                return fraction




        except (ValueError, ZeroDivisionError):
            s = input("What fractions? ")
            pass

main()




