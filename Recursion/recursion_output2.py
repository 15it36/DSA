# Recursive Output

def func(num: int) -> int:
	"""
	Recrsive function
	"""
	if int(num) == 1:
		return 0
	else:
		return 1 + func(num/2)


if __name__ == '__main__':

	print(func(10000))