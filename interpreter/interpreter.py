expression = input("Type xyz ")
x,y,z = expression.split(' ')
x = float(x)
z = float(z)

if y == "+":
    result = z + x

if y == "-":
    result = x - z
if y == "*":
    result = x*z
if y == '/':
    result = x / z

print (f'{result.f}')
