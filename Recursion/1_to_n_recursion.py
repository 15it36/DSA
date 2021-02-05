def reverse_print(num: int):
	"""
	Print value in reverse
	"""
	if num == 0:
		return
	print(num, end=" ")
	reverse_print(num-1)


def print_value(num: int, k: int):
	"""
	Print the values
	"""
	if num == 0:
		return
	print(k, end=" ")
	print_value(num-1, k+1)


def factorial(num: int):
	"""
	Print factorial
	"""
	if num == 0 | num == 1:
		return 1
	return num * factorial(num-1)


def tail_factorial(num: int, k: int):
	"""
	Print factorial using tail recrisive
	"""
	if num == 0 | num == 1:
		return k
	return tail_factorial(num - 1, k * num)


def fibonnasi_series(num: int):
	"""
	Fibonaci series
	"""
	if num == 0:
		return 0
	if num == 1:
		return 1
	return fibonnasi_series(num - 1) + fibonnasi_series(num - 2)


def sum_of_real_number(num: int, k: int):
	"""
	Sum of real numbers
	"""
	if num <= 1:
		return k
	return sum_of_real_number(num - 1, num + k)


def reverse_str(str1: str, new_str: str):
	"""
	Palindrome recursion
	"""	
	if len(str1) == 0:
		return new_str

	return reverse_str(str1[:-1], new_str + str1[-1:])


def isPalindrome(word: str):
	"""
	Check Palindrome
	"""
	if len(word) <= 1:
		return True
	if word[0] != word[-1]:
		return False
	return isPalindrome(word[1:-1])


def sum_of_digits(num: int, current_value: int):
    if num == 0:
        return current_value

    return sum_of_digits(int(num / 10), int(current_value + int(num % 10)))


if __name__ == '__main__':
	reverse_print(5)
	print("\n")
	print_value(5, 1)
	print("\n")
	print(factorial(5))
	print("\n")
	print(tail_factorial(5, 1))
	print("\n")
	print(fibonnasi_series(4))
	print("\n")
	print(sum_of_real_number(4, 1))
	print("\n")
	print(reverse_str('abba', ''))
	print("\n")
	print(isPalindrome("cababac"))
	print("\n")
	print(sum_of_digits(0, 0))
