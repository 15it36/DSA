if __name__ == '__main__':
	value = input()
	n = len(value)
	for x in range(n):
		for y in range(x, n):
			print(value[x:y])