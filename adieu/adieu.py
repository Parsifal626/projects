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
    except EOFError:
        print()





        # new line. If line is empty stop the loop


#printing