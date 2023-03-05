import sys
from pyfiglet import Figlet
import random

figlet = Figlet()
figlet.getFonts()
if len(sys.argv) == 1:
    isRandomFont = True
elif len(sys.argv) == 3 and (sys.argv[1] == '-f' or sys.argv[1] == '--font') and (sys.argv[2] in figlet.getFonts()):
    isRandomFont = False
else:
    print("Invalid usage")
    sys.exit(1)

#List of fonts


s = input('Input: ')


if isRandomFont == False:
    try:
        figlet.setFont(font=sys.argv[2])
    except:
        print("Invalid usage")
        sys.exit(1)
else:
    font = random.choice(figlet.getFonts())


print('Output: ')
print(figlet.renderText(s))

