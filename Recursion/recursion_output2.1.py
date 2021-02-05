def fun(num: int):
	if int(num) == 0:
		return
	fun(num/2)
	print(int(num)%2)


if __name__ == '__main__':
	fun(13)