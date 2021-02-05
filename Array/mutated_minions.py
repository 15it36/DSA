try:
	T = int(input())
	while(T):
		n, k = map(int, input().split())
		arr = [int(i) + k for i in input().split()]
		count = 0
		for i in range(len(arr)):
			if arr[i] % 7 == 0:
				count += 1
		print(count)
		T -= 1
except Exception as err:
	print(str(err))