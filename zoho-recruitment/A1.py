def Mergesort(arr: list):
	if len(arr) > 1:
		mid = len(arr) // 2
		L = arr[:mid]
		R = arr[mid:]
		Mergesort(L)
		Mergesort(R)
		i = j = k = 0

		while i < len(L) and j < len(R):
			if L[i] < R[j]:
				arr[k] = L[i]
				i += 1
			else:
				arr[k] =R[j] 
				j += 1
			k += 1

		while i < len(L):
			arr[k] = L[i]
			i += 1
			k += 1

		while j < len(R):
			arr[k] = R[j]
			j += 1
			k += 1


if __name__ == '__main__':
	N = int(input())
	count_dict = dict()
	for i in range(N):
		value = input()
		if count_dict.get(len(value), None):
			count_dict[len(value)].append(value)
		else:
			count_dict[len(value)] = [value]
	
	for key, val in count_dict.items():
		Mergesort(count_dict[key])
		print(*val, end=" ")
