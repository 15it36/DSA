def rope_cutting(rope_len: int, a: int, b: int, c: int):
    if rope_len == 0:
        return 0

    if rope_len <= -1:
        return -1

    result = max(rope_cutting(rope_len - a, a, b ,c),
		    	 rope_cutting(rope_len - b, a, b, c),
		    	 rope_cutting(rope_len - c, a, b, c))

    if result == -1:
    	return -1

    return result + 1


if __name__ == '__main__':
    rope_len = int(input())
    a = int(input())
    b = int(input())
    c = int(input())
    print(rope_cutting(rope_len, a, b, c))
