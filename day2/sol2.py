# 14-15 v: vdvvvvvsvvvvvfpv

def is_valid(policy, char, password):
	pos1 = policy[0] - 1
	pos2 = policy[1] - 1
	if password[pos1] == char:
		if password[pos2] == char:
			return False
		return True
	if password[pos2] == char:
		return True
	return False


with open('input.txt', 'r') as f:
	entries = f.read().split('\n')
	entries = entries[0:-1]
	count = 0
	for entry in entries:
		entry = entry.split(' ')
		policy = list(map(lambda n: int(n), entry[0].split('-')))
		char = entry[1][0]
		if is_valid(policy, char, entry[2]):	
			count += 1
	print(count)
