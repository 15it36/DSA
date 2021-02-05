try:
	T = int(input())
	while(T):
		cops, x, y = map(int, input().split())
		max_covered = x*y
		cops_pos = list(map(int, input().split()))
		default_pos = [1]*101
		for cop in cops_pos:
			new_initial_pos = max(1, cop-max_covered)
			new_end_position = min(100, cop+max_covered)
			
			while new_initial_pos <= new_end_position:
				default_pos[new_initial_pos] = 0
				new_initial_pos += 1
		count = 0
		for i in range(1, 101):
			count += default_pos[i]

		print(count, end="\n")
		T -= 1

except Exception as e:
	print(str(e))