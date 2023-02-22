amount_due = 50
while amount_due > 0:
   print('Amount Due: ', amount_due)
   insert= int(input("Insert coin: "))
   if insert in [5,10,25]:
      amount_due = amount_due - insert
change = abs(amount_due)
print('Change owed: ', change)