""" Digital Root """
def digitalRoot(n: int):
	if n < 10:
		return n
	else:
		return n % 10 + digitalRoot(int(n/10))


def main():
	number = int(input())
	print(digitalRoot(number))


if __name__ == '__main__' :
	"""
	Main Method
	"""
	main()