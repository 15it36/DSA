def nextGap(gap):
	if (gap <= 1): 
		return 0
	return (gap // 2) + (gap % 2)


def merge(arr1, arr2, n, m):
	gap = n + m 
	gap = nextGap(gap) 
	print("Initial Gap",gap)
	while gap > 0 : 
	
		i = 0
		while i + gap < n : 
			if (arr1[i] > arr1[i + gap]): 
				arr1[i], arr1[i + gap] = arr1[i + gap], arr1[i] 
				
			i += 1

		j = gap - n if gap > n else 0
		while i < n and j < m: 
			if (arr1[i] > arr2[j]): 
				arr1[i], arr2[j] = arr2[j], arr1[i] 
				
			i += 1
			j += 1

		if (j < m): 
			
			
			j = 0
			while j + gap < m : 
				if (arr2[j] > arr2[j + gap]): 
					arr2[j], arr2[j + gap] = arr2[j + gap], arr2[j] 
					
				j += 1
				
		gap = nextGap(gap)
		print(arr1, arr2)
		print(gap)

if __name__ == '__main__':
	T = int(input())
	while T:
		n, m = map(int, input().split())

		arr1 = list(map(int, input().split()))
		arr2 = list(map(int, input().split()))

		ans = merge(arr1, arr2, n, m)
		print(*(arr1 + arr2))

		T = T - 1