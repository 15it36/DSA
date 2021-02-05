""" Jose Problem """

def jose(n: int, k: int):
	"""
	Find a survivor
	"""
	if n == 1:
		return 1

	return (jose(n-1, k) + k-1) % n + 1


if __name__ == '__main__':
	"""
	Main Method
	"""
	n = int(input())
	k = int(input())
	print(jose(n, k))