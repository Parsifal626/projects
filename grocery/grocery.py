def main():
    grocery = {}

    while True:
        try:
            s = input('List: ')
            if s.upper() in grocery:
                grocery[s] += 1
            else:
            grocery[s] = 1

        except EOFError:
            print()
            break
        if s.upper() in grocery:
            grocery[s] += 1
        else:
            grocery[s.upper()] = 1

        for s in sorted(grocery.keys()):
            print(grocery[s], s)



main()