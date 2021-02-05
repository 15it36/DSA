try:
	T = int(input())
	while(T):
		n = int(input())
		arr = list(map(int, input().split()))

		new_arr = []

		for i in range(len(arr)):
			arr[i] not in new_arr:
			new_arr.append(arr[i])

		new_arr.sort()

		if new_arr == [1,2,3,4,5,6,7] and arr == arr[::-1]:
			print("yes")
		else:
			print("no")

		T -= 1
except Exception as arr:
	print(str(arr))