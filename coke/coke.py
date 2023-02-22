def coincal(insert,amount_due)
    while amount_due > insert:
       amount_due = amount_due - insert
       insert= int(input("Insert coin: "))
       if amount_due - insert == 0:
           print('Changed owed:0')
        elif amount_due > insert:
           print(f'Changed owed: {amount_due - insert}')
    if insert > amount_due:
        print




 = 50
s = ()

while  insert() <= amount_due():
     if insert == 5:
         s= amount_due() - 5
     s = amount_due() - insert()
        print ("Amount Due:" s)
