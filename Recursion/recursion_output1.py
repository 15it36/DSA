# Recursion Output sample codes
def fun1(num: int):
	"""
	Recursive function
	"""
	if num == 0:
		return

	print("Before call",num)
	num = num - 1
	fun1(num)
	print("After call", num)

if __name__ == '__main__':
	fun1(3)