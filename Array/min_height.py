try:
	K, N = map(int, input().split())
	arr = list(map(int, input().split()))
	_min = float("inf")
	_max = 0
	
	for idx, val in enumerate(arr):
		arr[idx] = (val + K) if val - K <= 0 else (val-K)
		if arr[idx] > _max:
			_max = arr[idx]
		if arr[idx] < _min:
			_min = arr[idx]
	print(arr)
	print(_min, _max)
	
except Exception as e:
	raise e