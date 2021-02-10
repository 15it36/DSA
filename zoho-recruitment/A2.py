def closeFib(num: int):
	if num == 0 or num == 1:
		return num
	f1 = 0 
	f2 = 1
	f3 = 1
	while f3 <= num:
		f1 = f2
		f2 = f3
		f3 = f1 + f2

	return f2


if __name__ == '__main__':
	num = int(input())
	while num:
		near_value = closeFib(num)
		num -= near_value
		print(near_value, end=" ")