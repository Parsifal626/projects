def main ():

    d = {
        "Baja Taco": 4.00,
        "Burrito": 7.50,
        "Bowl": 8.50,
        "Nachos": 11.00,
        "Quesadilla": 8.50,
        "Super Burrito": 8.50,
        "Super Quesadilla": 9.50,
        "Taco": 3.00,
        "Tortilla Salad": 8.00
            }
    amount = 0
    while True:
            try:
                s = input("Item: ").title()
                if s in d:
                    amount += d[s]
                    print ('Total: $', end = '')
                    print ('{:.2f}'.format(amount))
            except (EOFError, KeyError):
                print()
                break


main()











