s = input("You got a greeting that starts with an 'h', how does $20 sound " ).lower().strip()
if s[0:5] == "hello":
    print ("$0")
elif s[0] == 'h':
    print('$20')
else:
    print ('$100')
