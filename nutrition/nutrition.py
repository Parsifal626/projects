fruit = input('Item: ').lower()


fruits = {
    "apple": '130',
    "avocado":'50',
    "banana": '110',
    "sweet cherries": '100',
    "kiwifruit": '90',
    "pear": '100'
}

if fruit in fruits:
    print (f'Calories: ', fruits[fruit])

