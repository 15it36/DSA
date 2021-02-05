""" Count Number of Digits """ 
def find_no_of_digts(number: int, count:int = 0):
	if number == 0:
		return count
	return find_no_of_digts(int(number/10), count+1)


def main():
	number = int(input())
	print(find_no_of_digts(number))


if __name__ == '__main__':
	"""
	Main Method
	"""
	main()