""" Little Elephant Candies Problem """

if __name__ == '__main__':
	test_case = int(input())
	while(test_case):
		no_of_eliphant, total_candies = map(int, input().split())

		arr = [int(i) for i in input().split()]

		for i in range(0, no_of_eliphant):
			total_candies = total_candies - arr[i]

		if total_candies >= 0:
			print("Yes")
		else:
			print("No")

		test_case = test_case - 1
