""" Find a sum of Subset """

def sum_of_subset(arr: list, arr_size: int, arr_sum: int):
	"""
	Find sum of subset
	"""
	if arr_size == 0:
		return arr_sum == 0
	
	return sum_of_subset(arr, arr_size - 1, arr_sum) + \
		   sum_of_subset(arr, arr_size - 1, arr_sum - arr[arr_size - 1])


subset_sum = 0


if __name__ == '__main__':
	"""
	Main Method
	"""
	n = int(input())
	sub_set_list = list()

	for _ in range(0, n):
		value = int(input())
		sub_set_list.append(value)

	subset_sum = int(input())

	print(sum_of_subset(sub_set_list, len(sub_set_list), subset_sum))