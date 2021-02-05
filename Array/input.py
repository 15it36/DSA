class Pair:
	def __init__(self, first, second):
		self.first = first
		self.second = second


arr = [Pair(i) for i, j in input().split()]
print(v.first, v.second)