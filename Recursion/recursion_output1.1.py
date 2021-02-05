# recursion Output Program

def func(num: int) -> None:
	"""
	Recrsive Function
	"""
	if num == 0:
		return
	func(num - 1)
	print("func call", num)
	func(num - 1)


if __name__ == '__main__':
	func(2)