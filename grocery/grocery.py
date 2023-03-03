def main():
    grocery = {}

    while True:
        try:
            s = input('List: ').lower()
            if s in grocery:
                grocery[s] += 1
            else:
                grocery[s] = 1
        except EOFError:
            for key in sorted(grocery.keys()):
                print(grocery[key], key.upper())
            break

main()