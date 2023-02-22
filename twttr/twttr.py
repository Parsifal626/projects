s = (input("Type Something: "))
for i in s:
    if not i in ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]:
        print(i, end="")


