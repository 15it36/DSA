def insertionSort(arr: list):
	for i in range(1, n):
		key = arr[i]

		j = i - 1
		while j >= 0 and key < arr[j]:
			arr[j+1] = arr[j]
			j -= 1;
		arr[j+1] = key


if __name__ == '__main__':
	arr = list(map(int, input().split()))
	n = len(arr)
	insertionSort(arr)
	for value in arr:
		print(value, end=" ")
	