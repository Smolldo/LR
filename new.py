def func(a, b = 5, c = 10):
	print('a = ',a, 'b = ',b, 'c = ',c)

def maximum(x, y):
	if x > y:
		return x
	elif x == y:
		return "They r equal"
	else:
		return y
print(maximum(2, 3))

func(3, 7)