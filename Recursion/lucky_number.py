def lucky_number(n):
	if n == 0:
		return 0
	if n < 0:
		return 1
	return lucky_number(n)

c = 2

if __name__ == '__main__':
	n = int(input())
	print(lucky_number(n))