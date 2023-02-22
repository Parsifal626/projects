def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    # min 2 and max 6 characters
    s = input("Type your vanity place. (min 2 and max 6): ")
    if 6<len(s)<2:
        return False
    # minimum 2 letters
    if s[0].isalpha() == False or s[1].isalpha() == False:
        return False

    i=0
    while i < len(s):
        if s[i].isalpha() == False:
            if s[i] == '0':
                return False
            else:
                break
        i +=1

    # No periods, spaces, or punctuation marks are allowed
    for c in s:
        if c in ['.',' ', '!', '?']:
            return False

    return True


main()