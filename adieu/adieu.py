import inflect
p = inflect.engine()


# Create List
names = []
# Loop forever
while True:
    try:
        # input
        name = input("Name:  ")
        names.append(name)
        output = p.join(names)
    except EOFError:
        print('\n')
        print("Adieu, adieu, to " + output)
        break
    else:
        continue

#printing