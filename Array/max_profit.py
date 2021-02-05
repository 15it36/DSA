try:
	nums = list(map(int, input().split()))
	n = len(nums)
	max_profit = 0
	buy_price = nums[0]
	
	for i in range(1, n, 1):
		print(nums[i])
		if buy_price < nums[i]:
			new_profit = nums[i] - buy_price
			if new_profit > max_profit:
				max_profit = new_profit
		else:
			buy_price = nums[i]
	
	print(max_profit)

except Exception as e:
	raise e