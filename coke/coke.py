amount_due = 50
while amount_due > 0:
   print('Amount Due: ', amount_due)
   insert= int(input("Insert coin: "))
   if insert in [5,10,25]:
      amount_due = amount_due - insert















def main():
    print(f'Amount due: 50')
    insert= int(input("Insert coin: "))
    amount_due = 50
    while insert not in [5,10,25]:
       print(f'Amount due: 50')
       insert= int(input("Insert coin: "))
    print(f'Amount due: {amount_due - insert}')
    coincal(insert, amount_due)

def coincal(insert,amount_due):
    insert= int(input("Insert coin: "))
    while amount_due > insert:
       amount_due = amount_due - insert
       insert= int(input("Insert coin: "))
       if amount_due - insert == 0:
        print('Change owed: 0')
       elif amount_due > insert:
        print(f'Amount due: {amount_due - insert}')
    if insert > amount_due:
        print(f'Change owed: {insert - amount_due}')

main()