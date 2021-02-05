try:
	arr = list(map(int, input().split()))
	k = int(input())
	n = len(arr)
	counter_dict = dict()
	n_k = int(n/k)
	print(n_k)
	final_result = []

	for i in range(0, n):
		if arr[i] in counter_dict:
			counter_dict[arr[i]] += 1
		else:
			counter_dict[arr[i]] = 1

	for key, value in counter_dict.items():
		if value > n_k:
			final_result.append(key)

	print(sorted(final_result))

except Exception as e:
	raise e