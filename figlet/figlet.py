import sys


if len(sys.argv) == 1:
    isRandomFont = True
elif len(sys.argv) == 3:
    isRandomFont = False

print(isRandomFont)
