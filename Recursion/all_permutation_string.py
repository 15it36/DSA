def swap(arr, i, j):
	arr = list(arr)
	arr[i], arr[j] = arr[j], arr[i]
	# string = ''.join(string)
	return arr


def all_permutation(arr: list, index: int = 0):
	global arr_set
	if index == len(arr) -1 :
		arr_set.append(arr)
		print(arr, end="\n")
		return

	for j in range(index, len(arr)):
		arr = swap(arr, index, j)
		all_permutation(arr, index+1)
		arr = swap(arr, j, index)


if __name__ == '__main__':
	arr_set = []
	input_arr = list(map(int, input().split()))
	print("\n")
	all_permutation(input_arr)
	arr = list(arr_set)
	arr.sort()
	print(arr)