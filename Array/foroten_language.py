try:
	T = int(input())
	while(T):
		n, k = map(int, input().split())
		string_arr = list(map(str, input().split()))
		common_set = set()
		for i in range(k):
			words = list(map(str, input().split()))
			words.pop(0)
			common_set.update(words)

		for i in string_arr:
			if i in common_set:
				print("YES", end=" ")
			else:
				print("NO", end=" ")
		print()
		T -= 1

except Exception as e:
	print(str(e))