class node:
	def __init__(self, directory_name):
		self.directory_name = directory_name
		self.child_directory = list()
		self.parent = None

	def findNode(self, dir_name):
		for dirrectory in range(0, len(self.child_directory)):
			if self.child_directory[i] == directory_name:
				return self.child_directory[i]
		return None


if __name__ == '__main__':
	root = node('~')
	current_pos = root
	while True:
		cmd = input()
		cmd, directory_name = cmd.split(' ')
		
		if cmd == "md":
			temp = node(directory_name)
			temp.parent = current_pos
			temp.child_directory.append(temp)
		else:
			print("Enter a valid Comment")
		
		if cmd == "cd":
			if directory_name == '..':
				if current_pos.directory_name == '~':
					print("No parent available")
				else:
					current_pos = current_pos.parent
			else:
				temp =	current_pos.findNode(directory_name)
				if not temp:
					print("No File available")

			if directory_name[0] == '~':
				all_dir = directory_name.split('/')
				current_temp = root
				flag = False

				for i in range(0, len(all_dir)):
					t = current_temp.findNode(all_dir[i])
					if not t:
						print("no such file dirrectory")
						break
					
