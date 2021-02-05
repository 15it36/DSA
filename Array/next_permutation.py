try:
	nums = list(map(int, input().split()))
	n = len(nums)
	flag = False
	for i in range(n-1, 0, -1):
		if nums[i] > nums[i-1]:
			flag = True
			new_idx = i-1
			next_upper = upper_idx = float('inf')
			for j in range(new_idx+1, n):
				if nums[j] > nums[new_idx]:
					if nums[j] < next_upper:
						next_upper = nums[j]
						upper_idx = j
			# print(new_idx, next_upper)
			nums[new_idx], nums[upper_idx] = nums[upper_idx], nums[new_idx]
			nums[new_idx+1:n] = sorted(nums[new_idx+1:n])
			break
	if flag:
		print(flag, nums)
	else:
		nums.sort()
		print(flag, nums)

except Exception as e:
	raise e