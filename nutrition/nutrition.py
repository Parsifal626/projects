fruit = input('Type fruit ').lower


fruits = [
    {'fruit': "Apple", 'calories' : '130'},
    {'fruit': "Avocado", 'calories': '50'},
    {'fruit': "Banana", 'calories': '110'},
    {'fruit': "Sweet Cherries" , 'calories': '100'}
    ]

for fruit in fruits:
    print(fruits['fruit'])