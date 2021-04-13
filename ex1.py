#1. FLOAT
x = int(str(float(5)))
#2. STRING
x = 'aa' == 'AA'
#3. INT
x = {i: i**2 for i in range(5)}
#4. LIST
x = set(list((5, 6, 7)))
#5. DICT
a = {1: 1, 2: 4, 3: 9}
x = a.get(4)
#6. LIST
x = [].append('j')
#7. BOOL
for i in range(10):
		if i < 5:
				x = 'hello'
		else:
				x = 5
#8. STRING
x = input('Enter and integer: ')
#9. LIST
a = 5
b = [1, 3, 5, ]
x = 'x'
a, b, x = x, a, b
#10. STRING
def func(x, y=5):
		return x + y
x = func('Jaguar ', 'hunter')
