if __name__ == '__main__':
	arr = list(map(int, input().split()))
	size = len(arr)
	count_arr_length = max(arr) + 1
	output = [0] * size
	
	count_arr = [0] * count_arr_length

	for i in range(0, size):
		count_arr[arr[i]] += 1

	print(count_arr)

	for i in range(1, count_arr_length):
		count_arr[i] += count_arr[i-1]

	print(count_arr)

	for i in range(size-1, -1, -1):
		print(count_arr[arr[i]])
		output[count_arr[arr[i]] - 1] = arr[i]
		count_arr[arr[i]] -= 1

	print(count_arr)
	print(output)