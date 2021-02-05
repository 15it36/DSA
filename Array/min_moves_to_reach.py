def calc_min_jump(arr, N):
	if arr[0] == 0:
		return -1

	if N <= 1:
		return 0

	max_range = steps = arr[0]
	jumps = 1

	i = 1
	while i < N:
		
		if i == N - 1:
			return jumps
		
		max_range = max(max_range, i+arr[i])

		steps -= 1

		if steps == 0:
			
			jumps += 1
			
			if i >= max_range:
				return -1
			
			step = max_range - i

		i += 1
	
	return -1


if __name__ == '__main__':
	T = int(input())
	while T:
		N = int(input())
		arr = list(map(int, input().split()))
		print(calc_min_jump(arr, N))
		T -= 1
