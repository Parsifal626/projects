fruit = input('Item: ')


fruits = {
    "apple": '130',
    "avocado":'50',
    "banana": '110',
    "sweet cherries": '100'
}

if fruit in fruits:
    print (f'Calories: ', fruits[fruit])

