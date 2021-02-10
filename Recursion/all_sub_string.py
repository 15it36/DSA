def find_all_sub_string(input_str: str, new_str: str, str_len: int = 0):
	"""
	Find all posible sub string from given string
	"""
	if str_len == len(input_str):
		print(new_str, end=" ")
		return

	find_all_sub_string(input_str, new_str, str_len + 1)
	find_all_sub_string(input_str, new_str + input_str[str_len], str_len + 1)

 
if __name__ == '__main__':
	input_str = input()
	find_all_sub_string(input_str, "")
