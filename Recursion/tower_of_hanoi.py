def toh(n: int, a: int, b: int, c: int):
	if n == 1:	
		print("dist {} moved from {} to {}".format(n, a, b))
		return
	toh(n-1, a, c, b)
	print("dist {} moved from {} to {}".format(n, a, b))
	toh(n-1, c, b, a)

if __name__ == '__main__':
	number = int(input())
	toh(number, 1, 3, 2)