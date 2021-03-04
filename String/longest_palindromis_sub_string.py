try:
	value = input()
	n = len(value)
	table = [[0 for x in range(n)] for y in range(n)]
	
	"""
	Finding Substring for length 1
	"""
	max_length = 1
	i = 0
	while(i < n):
		table[i][i] = True
		i = i+1
	
	"""
	Finding Substring for length 2
	"""
	start = 0
	i = 0
	while i < n-1:
		if value[i] == value[i+1]:
			table[i][i+1] = True
			start = i
			max_length = 2
		i = i + 1

	"""
	Finding Substring Grater than length 2
	"""
	k = 3
	while k <= n:
		i = 0
		while i < (n-k+1):
			j = i + k - 1
			if table[i + 1][j - 1] and value[i] == value[j]:
				table[i][j] = True

				if k > max_length:
					start = i
					max_length = k
			i = i + 1
		k = k + 1

	print(max_length, value[start: start+max_length+1])
except Exception as e:
	raise e