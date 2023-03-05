import sys


if len(sys.argv) == 1:
    isRandomFont = True
elif len(sys.argv) == 3 and (sys.argv[1] == '-f' or sys.argv[1] == '--font'):
    isRandomFont = False
else:
    sys.exit(1)

s = input('Input: ')


#List of fonts
figlet.getFonts()

if isRandomFont == False:
    try:
        figlet.setFont(font=sys.argv[2])
        print(figlet.renderText(s))
    except:
        sys.exit("Invalid usage")
